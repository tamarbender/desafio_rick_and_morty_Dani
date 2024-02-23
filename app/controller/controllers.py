import requests

def get_episodes(page=1, page_size=20):
    url = f"https://rickandmortyapi.com/api/episode?page={page}&page_size={page_size}"
    response = requests.get(url)
    data = response.json()
    episodes = data["results"]
    return episodes, data["info"]["pages"]


def get_episode_by_id(id, page=1, page_size=10):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = requests.get(url)
    episode_details = response.json()
    data = episode_details['episode'].split('E')

    episode_details['season'] = data[0][1:]
    episode_details['episode'] = data[1]

    return episode_details


def get_locations():
    pass


def get_location_by_id():
    pass