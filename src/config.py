import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_PATH = os.path.join(BASE_DIR, 'datasets')
RAW_DATA_PATH = os.path.join(DATA_PATH, 'raw', 'data.csv')
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'processed', 'data_processed.csv')

MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'vectorizer.pkl')

MAX_FEATURES = 5000
NUM_RECS = 5

RANDOM_SEED = 42
