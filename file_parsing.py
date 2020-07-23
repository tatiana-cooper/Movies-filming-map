from geopy.geocoders import Nominatim
import collections


def file_parsing(file, year):
    """
    The function parsing film's information from the .list file
    (.list, int) -> (dict)
    :param file: location.list
    :param year: year of film's information we wanted
    :return:  {tuple(locations, coordinates of locations) : list(film's names of corresponding location)}
    """

    film_dict = collections.defaultdict(list)  # dict for parsed information
    year = '(' + year + ')'  # str year with '(' and ')' for finding in the file
    geo_locator = Nominatim(user_agent="my-application", timeout=100)  # to get coordinates of the Country

    # Cut out the name of the film's given year and the location of filming:
    films = [(i[:i.find(')') + 1].strip(), i[i[:i.rfind('\t(')].rfind('\t') + 1:i.rfind('\t(')].strip()) for i in
             open(file) if year in i]

    set_loc = list(set([i[1] for i in films]))  # part of future dict's keys — locations of filming

    # converts location to coordinates and makes future dict's key — tuple(locations, tuple(coordinates of locations))
    for index, location in enumerate(set_loc):
        try:
            coordinate = geo_locator.geocode(location)
            set_loc[index] = (location, (coordinate.latitude, coordinate.longitude))

        # exception for impossible decoding cases (German, Turkish), takes only country from the whole location name
        except AttributeError:
            try:
                coordinate = geo_locator.geocode(location.split()[-1])
                set_loc[index] = (location, (coordinate.latitude, coordinate.longitude))

            # if name of country also impossible to decode — del country
            except AttributeError:
                del set_loc[index]

    # make dict {tuple(locations, tuple(coordinates of locations)) : list(film's names of corresponding location)}:

    for _, item in enumerate(films):
        for key in set_loc:
            if item[1] == key[0]:  # if the same country — forms key and value
                film_dict[key].append(item[0])

    return film_dict


