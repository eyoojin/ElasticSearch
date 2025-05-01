# pip install "elasticsearch>=8, <9"
from elasticsearch import Elasticsearch, helpers
from faker import Faker
import random

es = Elasticsearch(
    ['https://localhost:9200'],
    basic_auth=('elastic', 'password'),
    # verify_certs=False
    ca_certs='/home/ubuntu/elasticsearch-8.18.0/config/certs/http_ca.crt'
)

fake = Faker()

movies = []

for i in range(1000):
    movies.append({
        '_index': 'movie',
        '_source': {
            'movieNm': fake.sentence(nb_words=3),
            'prdtYear': random.randint(1990, 2025),
        }
    })

helpers.bulk(es, movies)