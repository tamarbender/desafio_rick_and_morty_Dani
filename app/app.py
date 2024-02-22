from flask import render_template, Flask
from app.controller.controllers import get_episodes

app = Flask(__name__)


@app.route('/episodes')
def episodes():
    episodes = get_episodes()
    return render_template('episodes.html', episodes=episodes)


@app.route('/episode/<int:id>')
def episode(id):
    return


@app.route('/locations')
def locations():
    return


@app.route('/location/<int:id>')
def location(id):
    return
