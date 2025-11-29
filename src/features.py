import pandas as pd
import numpy as np
from textblob import TextBlob

def clean_tags(tags):
    """Cleans and processes a list of tags."""
    if pd.isna(tags):
        return []
    return [tag.strip().lower() for tag in tags.split(',')]

def calculate_sentiment(description):
    """Calculates sentiment polarity of a given description."""
    if pd.isna(description):
        return 0.0
    analysis = TextBlob(description)
    return analysis.sentiment.polarity

def feature_eng_pipeline(df):
    """Applies feature engineering to obtain 10+ features."""

    df_processed = df.copy()

    df_processed.loc[df_processed['description'] == "This entry currently doesn't have a synopsis. Check back soon!", 'description'] = np.nan

    df_processed['desc_len'] = df_processed['description'].apply(lambda x: len(x) if pd.notna(x) else 0)

    df_processed['sentiment'] = df_processed['description'].apply(calculate_sentiment)

    df_processed['tags_list'] = df_processed['tags'].apply(clean_tags)

    df_processed['num_tags'] = df_processed['tags_list'].apply(len)

    target_genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Thriller']
    target_comic_types = ['Manga', 'Manhwa', 'Manhua']

    for genre in target_genres:
        df_processed[f"is_{genre}"] = df_processed['tag_list'].apply(lambda x: 1 if genre in x else 0)

    for comic_type in target_comic_types:
        df_processed[f"is_{comic_type}"] = df_processed['comic_type'].apply(lambda x: 1 if comic_type in x else 0)

    current_year = pd.Timestamp.now().year

    df_processed['age'] = current_year - df_processed['year']

    return df_processed