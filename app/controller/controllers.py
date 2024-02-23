import requests


def get_episodes(page=1, page_size=20):
    url = f"https://rickandmortyapi.com/api/episode?page={page}&page_size={page_size}"
    response = requests.get(url)
    data = response.json()
    episodes = data["results"]
    return episodes, data["info"]["pages"]


def get_episode_by_id():
    pass


def get_locations():
    pass


def get_location_by_id():
    pass