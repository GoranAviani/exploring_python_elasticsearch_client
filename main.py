from elasticsearch import Elasticsearch
from datetime import datetime


def main():
    es = Elasticsearch()

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
