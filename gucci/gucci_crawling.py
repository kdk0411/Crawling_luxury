import asyncio
import json
from playwright.async_api import async_playwright


async def worker(queue, context, results):
	while True:
		key, url = await queue.get()
		if key is None:
			break
		print(f"Processing {key}")
		result = await crawling_page(context, key, url)
		results.append(result)
		queue.task_done()
		print(f"Complete {key}")


async def crawling_page(context, key, url):
	gender, category = key.split('/')
	data_list = []

	try:
		page = await context.new_page()
		await page.goto(url, wait_until="load", timeout=40000)
		position = 1

		if await page.locator("#onetrust-accept-btn-handler").is_visible():
			await page.locator("#onetrust-accept-btn-handler").click()

		if await page.locator("#productGridLoadMoreLnk").is_visible():
			await page.locator("#productGridLoadMoreLnk").click()

		await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

		while True:
			data = await page.query_selector(f"a[data-position='{position}']")

			if data is None:
				break

			href = 'www.gucci.com' + await data.get_attribute('href')
			name = (await data.get_attribute('aria-label')).replace('\n', '').strip()

			price = await page.evaluate("""
			    (data) => {
			        const spanElement = data.querySelector('span.sale');
			        if (spanElement) {
			            return spanElement.textContent.trim();
			        }
			        const pElement = data.querySelector('p.price');
			        return pElement ? pElement.textContent.trim() : null;
			    }
			""", data)

			if price:
				price = price.replace('₩', '').replace(',', '').strip()
				price = int(price)

			img_url = await page.eval_on_selector(
				'source[data-image-size="standard-retina"]',
				'element => element.getAttribute("srcset") || element.getAttribute("data-srcset")'
			)

			data_list.append({"name": name, "href": href, "price": price, "img_url": img_url})
			position += 1

		await page.close()
		return (gender, category, data_list)

	except Exception as e:
		print(f"Error processing {key}: {str(e)}")
		return (gender, category, [])


async def main_async(gucci_urls):
	async with async_playwright() as p:
		browser = await p.chromium.launch(
			headless=False,
			args=[
				'--disable-http2',  # HTTP/2 비활성화
				'--no-sandbox',
				'--disable-setuid-sandbox',
				'--disable-dev-shm-usage',
				'--disable-accelerated-2d-canvas',
				'--no-first-run',
				'--no-zygote',
				'--disable-gpu'
			]
		)
		context = await browser.new_context(
			user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
		)

		queue = asyncio.Queue()
		num_workers = 7
		results = []

		try:
			workers = [asyncio.create_task(worker(queue, context, results)) for _ in range(num_workers)]

			for key, url in gucci_urls.items():
				await queue.put((key, url))

			await queue.join()

			for _ in workers:
				await queue.put((None, None))

			await asyncio.gather(*workers)

			pcode_mapping = {
				"clothes": "cl", "wallets_leather": "cl", "ties": "cl", "hat": "cl",
				"eyewear": "cl", "belt": "cl", "scarves_gloves": "cl",
				"shoes": "sh",
				"fashion_jewelry": "ac", "fashion_accessories": "ac",
				"jewelry_gold": "ac", "jewelry_silver": "ac",
				"watch": "wa",
				"bag": "ba", "travel": "ba"
			}

			json_data = []

			for result in results:
				if result is not None:
					gender, category, data_list = result
					if data_list:
						for item in data_list:
							pcode = pcode_mapping.get(category, "unknown")
							json_data.append({"index": {"_index": "luxury"}})
							formatted_item = {
								'pname': item['name'],
								'brand': "GUCCI",
								"price": item["price"],
								"imageURL": item["img_url"],
								"option": None,
								"sex": "남성" if gender == "man" else "여성",
								"pcode": pcode
							}
							json_data.append(formatted_item)

			if json_data:
				with open("gucci_raw_data/gucci.json", 'w', encoding='utf-8') as json_file:
					json.dump(json_data, json_file, ensure_ascii=False, indent=4)
				print(f"Success saved {len(json_data)} items to gucci.json")

			return len(gucci_urls)

		finally:
			await context.close()
			await browser.close()


async def main():
	with open('gucci_url.json', 'r', encoding='utf-8') as json_file:
		gucci_urls = json.load(json_file)

	total_categories = await main_async(gucci_urls)
	print(f"Completed crawling {total_categories} categories")


if __name__ == "__main__":
	asyncio.run(main())
