from elasticsearch import Elasticsearch

# Elasticsearch 서버에 연결 설정
es = Elasticsearch(
	"https://localhost:9200",
	basic_auth=("elastic", "nXKRF+BdNWYHhSAfuY3w"),
	verify_certs=False
)


def search_by_brand(brand_name, index_name="luxury"):
    response = es.search(
        index=index_name,
        body={
            "query": {
                "match": {
                    "brand": brand_name
                }
            }
        }
    )
    print(f"Documents with brand '{brand_name}':")
    for hit in response["hits"]["hits"]:
        print(hit["_source"])

# "GUCCI" 브랜드로 검색
search_by_brand("GUCCI")
