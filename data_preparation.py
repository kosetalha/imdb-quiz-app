# Description: This script loads the IMDb top 1000 movies dataset and cleans it for the game app.

# Downloaded from https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

import pandas as pd

def load_and_clean_data(file_path='data/imdb_top_1000.csv'):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Select relevant columns and handle any missing data
    columns = ['Series_Title', 'Released_Year', 'Genre', 'Director']
        
    # Drop rows with missing values
    df = df[columns].dropna()
    
    # Rename columns for convenience
    df.columns = ['title', 'year', 'genre', 'director']
    
    # Clean year column - keep only numeric values
    df = df[df['year'].str.isnumeric()]
    
    # Convert year to integer
    df['year'] = df['year'].astype(int)
       
    return df

