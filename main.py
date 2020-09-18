from elasticsearch import Elasticsearch
from datetime import datetime


def main():
    es = Elasticsearch()
    print("Elasticsearch client version:", es.info()["version"], "\n")


    #check if index already exists:
    index_exists = es.indices.exists(index="test-index")
    print('{} index exists: {}'.format("test-index", index_exists))
    index_exists = es.indices.exists(index="test-index1111")
    print('{} index exists: {}'.format("test-index1111", index_exists))

    doc = {
        'company_name': 'Goran',
        'Address': 'Stockholm',
        'timestamp': datetime.now(),
    }

    res = es.index(index="test-index", id=1, body=doc)
    print(res['result'])

    res = es.get(index="test-index", id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")
    print(res['_source'])

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(company_name)s: %(Address)s" % hit["_source"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
