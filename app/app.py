from flask import Flask, render_template, request

from app.controller.controllers import (get_character_data, get_episode_by_id,
                                        get_episodes, get_list_characters_page,
                                        get_location_by_id, get_locations,
                                        get_list_characters)

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

@app.route('/locations')
def locations():
    page = request.args.get('page', 1, type=int)
    locations, total_pages = get_locations(page)
    return render_template('locations.html', locations=locations, current_page=page, total_pages=total_pages)


@app.route('/location/<int:id>')
def location(id):
    location = get_location_by_id(id)  
    residents_urls = location['residents']
    residents_data = get_character_data(residents_urls)

    return render_template('location.html', location=location, residents_data=residents_data)


@app.route('/profile/<int:id>')
def profile(id):
    response = get_list_characters_page(id)
    return render_template('profile.html', character=response)


@app.route('/profiles')
def profiles():
    page = request.args.get('page', 1, type=int)
    print(page)
    response,  total_pages = get_list_characters(page)
    return render_template('profiles.html', characters=response, current_page=page, total_pages=total_pages)

@app.route('/')
def home():
    return render_template('index.html')
