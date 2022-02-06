from urllib.request import urlopen
import json
import numpy as np

URL = "https://mach-eight.uc.r.appspot.com/"


def clean_data(data):
    number = 139

    a = {}
    for i in data["values"]:
        if i["h_in"] not in a:
            a[i["h_in"]] = list()
        a[i["h_in"]].append(f'{i["first_name"]} {i["last_name"]}')

    a = dict(sorted(a.items()))

    return a


def get_data(url):
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json


def order_players(data, number):
    # data and couple_ of players are dictionaries because the hash tables have a Time Complexity getting elements in
    # average cases of O(1)

    couple_of_players = {}

    # the key in data has O(1) in average cases, here we take any of the players(O(n)) and find in the dictionary the
    # remaining height, this is a problem of combinations without repetitions taking this into account doesn't really
    # matter if we have (a,b) or (b,a), we use the couple_of_players dictionary to set an id to each combination and
    # not repeat it

    for key in data:
        choice = number - int(key)
        if str(choice) in data and f'{key}-{choice}' not in couple_of_players and f'{choice}-{key}' not in couple_of_players:
            couple_of_players[f'{key}-{choice}'] = [data[str(choice)], data[key]]

    print(couple_of_players)

    # we use numpy to get all the combinations in an "optimal" way
    for key in couple_of_players:
        mesh = np.array(np.meshgrid(couple_of_players[key][0], couple_of_players[key][1]))
        combinations = mesh.T.reshape(-1, 2)

        print('\n'.join('- {}         {}'.format(*k) for k in combinations))


if __name__ == '__main__':
    number = int(input())
    m_data = get_data(URL)
    m_data = clean_data(m_data)
    order_players(m_data, number)
