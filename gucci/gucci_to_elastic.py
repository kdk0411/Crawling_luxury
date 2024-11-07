from elasticsearch import Elasticsearch, helpers
import json

# Local Elasticsearch 서버에 연결 설정
# es = Elasticsearch(
#     "https://localhost:9200",
#     basic_auth=("elastic", "nXKRF+BdNWYHhSAfuY3w"),
#     verify_certs=False
# )

es = Elasticsearch("http://116.37.91.221:9200/", verify_certs=False)


def upload_data_to_elasticsearch():
    with open("gucci_raw_data/gucci.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)

    actions = []
    for i in range(0, len(json_data), 2):  # 인덱스 메타데이터와 문서 데이터가 번갈아 나옴
        index_action = json_data[i]
        document = json_data[i + 1]

        actions.append(index_action)  # 인덱스 메타데이터 추가
        actions.append(document)  # 문서 데이터 추가

    # Elasticsearch에 데이터 업로드
    response = es.bulk(body=actions)
    print(response)


# 데이터 업로드 실행
upload_data_to_elasticsearch()
