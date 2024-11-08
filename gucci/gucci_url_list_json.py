import json

urls = {
	'women/bag': 'https://www.gucci.com/kr/ko/ca/women/handbags-c-women-handbags',
	'women/travel': 'https://www.gucci.com/kr/ko/ca/women/travel-bags-for-women-c-women-accessories-luggage-lifestyle-bags',
	'women/wallets_leather': 'https://www.gucci.com/kr/ko/ca/women/wallet-leather-acc-for-women-c-women-small-leathergoods',
	'women/clothes': 'https://www.gucci.com/kr/ko/ca/women/ready-to-wear-for-women-c-women-readytowear',
	'women/shoes': 'https://www.gucci.com/kr/ko/ca/women/shoes-for-women-c-women-shoes',
	'women/fashion_accessories': 'https://www.gucci.com/kr/ko/ca/women/accessories-for-women-c-women-accessories',
	'women/jewelry_gold': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/gold-jewelry-c-jewelry-watches-fine-jewelry',
	'women/jewelry_silver': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/silver-jewelry-c-jewelry-watches-silver-jewelry',
	'women/watch': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/watches/watches-for-her-c-jewelry-watches-watches-her',
	'man/bag': 'https://www.gucci.com/kr/ko/ca/men/bags-for-men-c-men-bags',
	'man/travel': 'https://www.gucci.com/kr/ko/ca/men/travel-bags-for-men-c-men-bags-luggage',
	'man/wallets_leather': 'https://www.gucci.com/kr/ko/ca/men/wallet-leather-acc-for-men-c-men-small-leathergoods',
	'man/clothes': 'https://www.gucci.com/kr/ko/ca/men/ready-to-wear-for-men-c-men-readytowear',
	'man/shoes': 'https://www.gucci.com/kr/ko/ca/men/shoes-for-men-c-men-shoes',
	'man/belt': 'https://www.gucci.com/kr/ko/ca/man/accessories-for-man/belts-for-men-c-men-accessories-belts',
	'man/fashion_jewelry': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/fashion-jewelry/fashion-jewelry-for-men-c-jewelry-watches-fashion-jewelry-men',
	'man/eyewear': 'https://www.gucci.com/kr/ko/ca/men/accessories-for-men/eyewear-for-mens-c-men-eyewear',
	'man/ties': 'https://www.gucci.com/kr/ko/ca/men/accessories-for-men/ties-for-men-c-men-accessories-ties',
	'man/hat': 'https://www.gucci.com/kr/ko/ca/men/accessories-for-men/hats-for-men-c-men-hats',
	'man/scarves_gloves': 'https://www.gucci.com/kr/ko/ca/men/accessories-for-men/scarves-gloves-soft-accessories-for-men-c-men-accessories-hats-soft-accessories',
	'man/jewelry_gold': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/gold-jewelry/gold-jewelry-for-men-c-jewelry-watches-fine-jewelry-men',
	'man/jewelry_silver': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/silver-jewelry/silver-jewelry-for-men-c-jewelry-watches-silver-jewelry-men',
	'man/watch': 'https://www.gucci.com/kr/ko/ca/jewelry-watches/watches/watches-for-him-c-jewelry-watches-watches-him'
}

with open('gucci_url.json', 'w', encoding='utf-8') as json_file:
	json.dump(urls, json_file, ensure_ascii=False, indent=4)
