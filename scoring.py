# Description: This file contains the scoring logic for the quiz game.

def calculate_score(is_correct, difficulty):
    
    if not is_correct: # If the answer is incorrect, return 0 points
        return 0
    
    points = {
        'easy': 10,
        'medium': 20,
        'hard': 30
    }
    
    return points.get(difficulty, 0) # Return 0 if difficulty is not valid
