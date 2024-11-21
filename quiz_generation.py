# Description: This script generates quiz questions based on the IMDb top 1000 movies dataset.

import random
import numpy as np

def generate_question(df, difficulty='medium'):
    # Randomly select a movie for the question
    movie = df.sample(1).iloc[0]
    
    # Question: "Who directed [Movie Title]?"
    question = f"Who directed '{movie['title']}'?"
    
    # Correct answer
    correct_answer = movie['director']
    
    # Generate incorrect answers based on difficulty
    if difficulty == 'easy':
        # Choose random directors from the entire dataset
        incorrect_answers = df['director'].sample(3).tolist()
    elif difficulty == 'medium':
        # Choose random directors from movies in the same genre
        genre_movies = df[df['genre'].apply(lambda x: any(g in movie['genre'] for g in x))]
        incorrect_answers = genre_movies['director'].sample(3).tolist()
    else:  # Hard difficulty
        # Choose random directors from movies released in the previous and the following 5 years
        similar_year_movies = df[(df['year'] >= movie['year'] - 5) & (df['year'] <= movie['year'] + 5)]
        incorrect_answers = similar_year_movies['director'].sample(3).tolist()
    
    # Ensure no duplicates in incorrect answers and no overlap with the correct answer
    incorrect_answers = [ans for ans in incorrect_answers if ans != correct_answer] # Remove duplicates if any
    while len(incorrect_answers) < 3:
        additional = df['director'].sample(1).iloc[0]
        if additional != correct_answer and additional not in incorrect_answers:
            incorrect_answers.append(additional)
    
    # Combine correct and incorrect answers and shuffle
    all_answers = incorrect_answers + [correct_answer]
    np.random.shuffle(all_answers)
    
    return {
        'question': question,
        'options': all_answers,
        'correct_answer': correct_answer,
        'difficulty': difficulty
    }