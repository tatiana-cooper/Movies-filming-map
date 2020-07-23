"""
This program builds the dots on the map according to:
1) countries were the movie was made in a given year
2) if these countries are English-speaking
3) if these countries are landlocked
"""
from string import digits
from file_parsing import file_parsing
from sort_countries import sort_countries
from folium import FeatureGroup, Marker, LayerControl, Map, TileLayer, Icon


def create_map(year):
    """
    (int) -> (.html)
    The function generates the map.
    :param year: year of filming
    :return: the map in .html file
    """

    if not 2025 > int(year) > 1889:
        raise ValueError('Error: Our database contains films from 1889 to the 2025 year')

    film_map = Map()  # the map creation
    films = file_parsing('locations.list', year)
    fg_1 = FeatureGroup(name="Film map")  # the dot's group creation
    fg_2 = FeatureGroup(name="Landlocked countries")
    fg_3 = FeatureGroup(name="English-speaking countries")
    TileLayer('Stamenwatercolor').add_to(film_map)  # adding one more layer to map

    # sorts countries for 'landlocked countries' map's layers and 'English-speaking countries'
    sorted_countries = sort_countries(films.keys())

    for key, values in films.items():
        """ Creating the map's dots of all films produced in a given year
            The marker contains names of the films and the number of films produced in this location"""

        # param key[1] contains coordinates
        fg_1.add_child(Marker(location=[key[1][0], key[1][1]],
                              # param values contains the names of films
                              popup=(*values, len(values)),
                              icon=Icon(icon='cloud', color='beige')))

        # finding of landlocked countries
        # param key[0] contains location in str format (key[0].split(',')[-1].strip() —
        # takes only country from the whole location name)
        country_name = key[0].split(',')[-1].strip()
        if 'landlocked' in sorted_countries[country_name]:
            fg_2.add_child(Marker(location=[key[1][0], key[1][1]], popup=(*values, len(values)),
                                  icon=Icon(icon='cloud', color='red')))

        # finding of English-speaking countries
        if 'eng' in sorted_countries[country_name]:
            fg_3.add_child(Marker(location=[key[1][0], key[1][1]], popup=(*values, len(values)),
                                  icon=Icon(icon='cloud', color='green')))

    # adding dots on the map:
    fg_1.add_to(film_map)
    fg_2.add_to(film_map)
    fg_3.add_to(film_map)

    LayerControl().add_to(film_map)
    film_map.save(f"Map_{year}.html")


if __name__ == '__main__':

    while True:
        user_input = input("Enter a year for research and map generation (for example — 2014): ")

        # Checks the user's input to consist only numbers
        if all(i in digits for i in user_input) and len(user_input) == 4:
            print('Please, wait a second..')
            break
        else:
            print('Enter only digits!')

    create_map(user_input)
