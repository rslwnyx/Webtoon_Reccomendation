import pandas as pd
import numpy as np
import os
import sys
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import config

class WebtoonRecommender:
    def __init__(self):
        
        self.data_path = config.PROCESSED_DATA_PATH
        self.model_save_path = config.MODEL_PATH
        
        self.df = None 
        self.df_model = None 
        self.cosine_sim = None
        self.indices = None 

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"File not found: {self.data_path}")
            
        self.df = pd.read_csv(self.data_path)
        self.df["description"] = self.df["description"].fillna("")

    def preprocess_and_engineer(self):
        cols_to_drop = ['id', 'desc_word_count', 'favourites', 'Unnamed: 0'] 
        df_clean = self.df.drop(columns=cols_to_drop, errors='ignore')

        df_clean = df_clean.set_index('title_romaji')

        df_engineered = df_clean.copy()
        df_engineered['popularity'] = np.log1p(df_engineered['popularity'])

        for col in df_engineered.columns:
            if df_engineered[col].dtype == 'bool':
                df_engineered[col] = df_engineered[col].astype(int)

        self.df_model = df_engineered.select_dtypes(include=[np.number])

        genre_cols = [c for c in self.df_model.columns if 'is_' in c]
        for col in genre_cols:
            self.df_model[col] = self.df_model[col] * 2.0

        quality_cols = ['popularity', 'averageScore']
        for col in quality_cols:
            if col in self.df_model.columns:
                self.df_model[col] = self.df_model[col] * 5.0

    def build_model(self):

        self.cosine_sim = cosine_similarity(self.df_model)
        
        self.indices = pd.Series(range(len(self.df_model)), index=self.df_model.index)
        

    def get_recommendations(self, title, top_n=5):
    
        if self.cosine_sim is None or self.indices is None:
            return "Model is not trained yet. Please run build_model() first."

        if title not in self.indices:
            return f"ERROR: '{title}' is not in the dataset."
        
        idx = self.indices[title]

        sim_scores = list(enumerate(self.cosine_sim[idx]))

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:top_n+1]
        
        webtoon_indices = [i[0] for i in sim_scores]
        
        recommended_titles = self.df_model.index[webtoon_indices]
        
        results = self.df[self.df['title_romaji'].isin(recommended_titles)]
        
        return results[['title_romaji', 'popularity', 'averageScore', 'genres']]

    def save_model(self, overwrite=False):
        save_path = os.path.join(self.model_save_path, 'recommender_model.pkl')
        
        if os.path.exists(save_path) and not overwrite:
            return

        model_data = {
            'cosine_sim': self.cosine_sim,
            'indices': self.indices,
            'df_model': self.df_model
        }
        
        os.makedirs(self.model_save_path, exist_ok=True)
        
        with open(save_path, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Model is saved in: {save_path}")


if __name__ == "__main__":

    recommender = WebtoonRecommender()
    

    try:
        recommender.load_data()
        recommender.preprocess_and_engineer()
        recommender.build_model()
        
    
        print("-" * 30)
        chosen_title = input("Enter a title (Example: Chainsaw Man): ")
        print(f"Searching reccomendations for '{chosen_title}'...")
        
        recommendations = recommender.get_recommendations(chosen_title)
        print(recommendations)
        
        recommender.save_model()
        
    except Exception as e:
        print(f"Error: {e}")