import json


def json_parsing():
    """
    The function loads data from 'countries.json' file
    Returns list of dicts of loaded elements
    """
    with open('countries.json') as f:
        countries = json.load(f)

    return countries


if __name__ == '__main__':
    json_parsing()
