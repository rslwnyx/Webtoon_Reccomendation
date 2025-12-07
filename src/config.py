import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_PATH = os.path.join(BASE_DIR, 'datasets')
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'processed', 'data_processed.csv')
WEBTOON_DATA_PATH = os.path.join(DATA_PATH, 'raw', 'webtoon_data.csv')
WEBTOON_DATA_PATH_JSON = os.path.join(DATA_PATH, 'raw', 'webtoon_data.json')

MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
PARAM_PATH = os.path.join(BASE_DIR, 'models', 'best_params.json')

TFIFD_VEC_PATH = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.pkl')
TAGS_VEC_PATH = os.path.join(BASE_DIR, 'models', 'tags_vectorizer.pkl')
GENRES_VEC_PATH = os.path.join(BASE_DIR, 'models', 'genres_vectorizer.pkl')

TFIFD_MATRIX_PATH = os.path.join(BASE_DIR, 'models', 'tfidf_matrix.pkl')
TAGS_MATRIX_PATH = os.path.join(BASE_DIR, 'models', 'tags_matrix.pkl')
GENRES_MATRIX_PATH = os.path.join(BASE_DIR, 'models', 'genres_matrix.pkl')

MAX_FEATURES = 5000
NUM_RECS = 5

RANDOM_SEED = 42
