from flask import render_template, Flask, request
from app.controller.controllers import get_episodes, get_episode_by_id, get_locations, get_location_by_id, get_list_characters_page
import requests
import concurrent.futures

app = Flask(__name__)

@app.route('/episodes')

def episodes():
    page = request.args.get('page', 1, type=int)
    episodes, total_pages = get_episodes(page)
    return render_template('episodes.html', episodes=episodes, current_page=page, total_pages=total_pages)

@app.route('/episode/<int:id>')
def episode(id):
    episode = get_episode_by_id(id)
    
    character_urls = episode['characters']
    character_data = get_character_data(character_urls)

    return render_template('episode.html', episode=episode, character_data=character_data)

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
            'image': character_data['image']
        }
    else:
        return None


@app.route('/locations')
def locations():
    page = request.args.get('pages', 1, type=int)
    locations, total_pages = get_locations(page)
    return render_template('locations.html', locations=locations, current_page=page, total_pages=total_pages)

@app.route('/location/<int:id>')
def location(id):
    location = get_location_by_id(id)
    
    residents_urls = location['residents']
    residents_data = get_character_data(residents_urls)

    return render_template('location.html', location=location, residents_data=residents_data)

@app.route("/")
def pageInicial():
    response = get_list_characters_page()
    return render_template('characters.html', characters=response)
