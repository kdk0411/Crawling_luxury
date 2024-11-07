from elasticsearch import Elasticsearch

# Local Elasticsearch 서버에 연결 설정
es = Elasticsearch(
	"https://localhost:9200",
	basic_auth=("elastic", "nXKRF+BdNWYHhSAfuY3w"),
	verify_certs=False
)


def check_all_data(index_name="luxury"):
	response = es.search(index=index_name, body={"query": {"match_all": {}}})
	print("Uploaded data:")
	for hit in response["hits"]["hits"]:
		print(hit["_source"])


def count_all_data(index_name="luxury"):
	# count API를 사용하여 문서 수 확인
	response = es.count(index=index_name)
	print(f"Total number of documents in '{index_name}': {response['count']}")


# 문서 수 확인 실행
count_all_data()
# 데이터 확인 실행
# check_all_data()
