from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TMDB_API_TOKEN = os.getenv('TMDB_API_TOKEN')
    TMDB_API_KEY = os.getenv('TMDB_API_KEY')
    TMDB_BASE_URL = os.getenv('TMDB_BASE_URL')

    TMDB_MIN_VOTE_AVERAGE = 6
    TMDB_MIN_VOTE_COUNT = 100
    TMDB_MAX_RANDOM_PAGE = 50
    TMDB_RESULTS_LIMIT = 20
    TMDB_SORT_BY = "popularity.desc"

    MOVIE_MOODS = {
        "curiosity": [9648, 12],
        "joy": [35, 10402, 16],
        "tension": [53, 80, 28, 27],
        "reflection": [99, 36, 37],
        "sadness": [18, 10749, 10752],
        "comfort": [10751, 10770],
        "fascination": [878, 14]
    }
