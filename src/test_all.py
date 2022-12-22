import pytest
from utils import map_reduce, denormalize


class TestUtils:
    def test_flat_map(self):
        assert map_reduce(lambda x: x + 1, list(range(1, 4))) == 9

        with pytest.raises(Exception):
            map_reduce(lambda x: x + 1, [])

    def test_denormalize(self):
        job = {
            "website": "https://www.elli.eco/de/startseite",
            "rating": 3.3,
            "remote": False,
            "name": "Elli",
            "speculative": True,
            "field": "Electric Mobility",
            "jobs": "https://elli.jobs.personio.de/",
            "geo": [
                {
                    "lat": 52.526286,
                    "country": "Germany",
                    "long": 13.4153968
                },
                {
                    "lat": 52.4210151,
                    "country": "Germany",
                    "long": 10.7433627
                }
            ],
            "review": "https://www.kununu.com/de/elli",
            "description": "Charging solutions by Volkswagen"
        }

        assert denormalize(job) == [
            {'country': 'Germany',
             'description': 'Charging solutions by Volkswagen',
             'field': 'Electric Mobility',
             'geo': {'lat': 52.526286,
                     'long': 13.4153968},
             'jobs': 'https://elli.jobs.personio.de/',
             'name': 'Elli',
             'rating': 3.3,
             'remote': False,
             'review': 'https://www.kununu.com/de/elli',
             'speculative': True,
             'website': 'https://www.elli.eco/de/startseite'},
            {'country': 'Germany',
             'description': 'Charging solutions by Volkswagen',
             'field': 'Electric Mobility',
             'geo': {'lat': 52.4210151,
                     'long': 10.7433627},
             'jobs': 'https://elli.jobs.personio.de/',
             'name': 'Elli',
             'rating': 3.3,
             'remote': False,
             'review': 'https://www.kununu.com/de/elli',
             'speculative': True,
             'website': 'https://www.elli.eco/de/startseite'},
        ]


class TestCreateReadme:
    pass


class TestCreateMapData:
    pass
