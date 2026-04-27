from flask import Blueprint, jsonify
import random
import requests

from .config import Config


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'Hello, World!'


@main.route('/movie/<mood>')
def movie(mood): 
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
    movies = data.get('results', [])
    random.shuffle(movies)

    return jsonify(movies[:Config.TMDB_RESULTS_LIMIT])


@main.route('/genres')
def list_genres():
    url = f'{Config.TMDB_BASE_URL}/genre/movie/list'
    headers = {
        'Authorization': f'Bearer {Config.TMDB_API_TOKEN}',
    }
    response = requests.get(url, headers=headers)

    return jsonify(response.json())

