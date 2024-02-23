from flask import render_template, Flask, request
from app.controller.controllers import get_episodes

app = Flask(__name__)


@app.route('/episodes')
def episodes():
    page = request.args.get('page', 1, type=int)
    episodes, total_pages = get_episodes(page)

    return render_template('episodes.html', episodes=episodes, current_page=page, total_pages=total_pages)



@app.route('/episode/<int:id>')
def episode(id):
    return


@app.route('/locations')
def locations():
    return


@app.route('/location/<int:id>')
def location(id):
    return
