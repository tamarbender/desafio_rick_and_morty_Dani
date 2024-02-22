import requests


def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = requests.get(url)
    episodes = response.json()["results"]
    return episodes


def get_episode_by_id():
    pass


def get_locations():
    pass


def get_location_by_id():
    pass