from json_parsing import json_parsing
from collections import defaultdict


def sort_countries(country_name):
    """
    This function sorts countries for 'landlocked countries' map's layer and 'English-speaking countries' layer
    :param country_name: list of countries' names
    :return: dict of countries (key — land, value — list of one or two elements,
    which show if country is English-speaking and landlocked)
    """
    sorted_countries = defaultdict(list)  # dict for sorted countries
    print(type(country_name))

    # makes list of names of countries (without cities and streets)
    films_countries = list(map(lambda x: x[0].split(',')[-1].strip(), country_name))

    # loads countries information
    countries = json_parsing()

    for _, country in enumerate(countries):
        for _, land in enumerate(films_countries):

            if land in country['name']['common']:

                if country['landlocked']:
                    sorted_countries[land].append('landlocked')

                if 'eng' in country['languages'].keys() and 'eng' not in sorted_countries[land]:
                    sorted_countries[land].append('eng')

    return sorted_countries
