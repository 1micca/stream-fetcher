from flask import Blueprint, jsonify, render_template, request
import random
import requests

from .config import Config


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    MOVIE_MOODS_LIST = list(Config.MOVIE_MOODS.keys())
    return render_template('index.html', MOVIE_MOODS_LIST=MOVIE_MOODS_LIST)


@main_bp.route('/movie')
def movie():
    mood = request.args.get('mood')
    genres = Config.MOVIE_MOODS.get(str(mood).lower())
    
    if genres is None:
        return '404 Not found'

    url = f'{Config.TMDB_BASE_URL}/discover/movie'
    headers = {
        'Authorization': f'Bearer {Config.TMDB_API_TOKEN}',
    }
    params = {
        'with_genres': '|'.join(map(str, genres)),
        'vote_average.gte': Config.TMDB_MIN_VOTE_AVERAGE,
        'vote_count.gte': Config.TMDB_MIN_VOTE_COUNT,
        'sort_by': Config.TMDB_SORT_BY,
        'page': random.randint(1, Config.TMDB_MAX_RANDOM_PAGE)
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    movies_list = data.get('results', [])
    random.shuffle(movies_list)
    movies = movies_list[:Config.TMDB_RESULTS_LIMIT]

    return render_template('movies.html', movies=movies)

@main_bp.route('/genres')
def genres():
    url = f'{Config.TMDB_BASE_URL}/genre/movie/list'
    headers = {
        'Authorization': f'Bearer {Config.TMDB_API_TOKEN}',
    }
    response = requests.get(url, headers=headers)

    return jsonify(response.json())

