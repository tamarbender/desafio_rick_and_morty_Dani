import requests, urllib.request, json

def get_episodes(page=1, page_size=20):
    url = f"https://rickandmortyapi.com/api/episode?page={page}&page_size={page_size}"
    response = requests.get(url)
    data = response.json()
    episodes = data["results"]
    return episodes, data["info"]["pages"]


def get_episode_by_id(
     page=1, page_size=10):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = requests.get(url)
    episode_details = response.json()
    data = episode_details['episode'].split('E')

    episode_details['season'] = data[0][1:]
    episode_details['episode'] = data[1]

    return episode_details


def get_locations(page=1, page_size=20):
    url = f"https://rickandmortyapi.com/api/location?page={page}&page_size={page_size}"
    response = requests.get(url)
    data = response.json()
    locations = data["results"]
    return locations, data["info"]["pages"]
    

def get_location_by_id(id, page=1, page_size=10):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = requests.get(url)
    location_details = response.json()

    return location_details

def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url) 
    data = response.read()
    characters_dict = json.loads(data)

    return characters_dict['results']


# print(get_locations())