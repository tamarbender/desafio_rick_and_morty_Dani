import concurrent.futures
import json
import urllib.request

import requests


def get_episodes(page=1):
    url = f"https://rickandmortyapi.com/api/episode?page={page}"
    response = requests.get(url)
    data = response.json()
    episodes = data["results"]
    return episodes, data["info"]["pages"]


def get_episode_by_id(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = requests.get(url)
    print(response)
    episode_details = response.json()
    data = episode_details['episode'].split('E')

    episode_details['season'] = data[0][1:]
    episode_details['episode'] = data[1]

    return episode_details


def get_locations(page=1):
    url = f"https://rickandmortyapi.com/api/location?page={page}"
    response = requests.get(url)
    data = response.json()
    locations = data["results"]
    return locations, data["info"]["pages"]
    

def get_location_by_id(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = requests.get(url)
    location_details = response.json()

    return location_details


def get_list_characters_page(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read()
    characters_dict = json.loads(data)

    return characters_dict


def get_character_data(character_urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(get_character_data_single, url): url for url in character_urls}
        character_data = []
        for future in concurrent.futures.as_completed(future_to_url):
            character_url = future_to_url[future]
            try:
                character_info = future.result()
                character_data.append(character_info)
            except Exception as exc:
                print(f'A requisição para {character_url} falhou: {exc}')
                character_data.append(None)
    return character_data


def get_character_data_single(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        character_data = response.json()
        return {
            'name': character_data['name'],
            'image': character_data['image'],
            'id': character_data['id']
        }
    else:
        return None
