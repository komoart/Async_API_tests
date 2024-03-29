import backoff
from elasticsearch import Elasticsearch


@backoff.on_exception(backoff.expo, ConnectionError, max_tries=7)
def wait_elastic():
    elastic = Elasticsearch(hosts=[f"elastic:9200"])
    ping = elastic.ping()
    if not ping:
        raise ConnectionError()
    elastic.close()


if __name__ == "__main__":
    wait_elastic()
