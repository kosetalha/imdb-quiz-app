# Description: This script contains functions for visualizing quiz results.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def initialize_quiz_history():
    return pd.DataFrame(columns=['question', 'user_answer', 'correct_answer', 
                               'difficulty', 'score'])

def add_quiz_result(df, result): # Add a new quiz result to the history
    return pd.concat([df, pd.DataFrame([result])], ignore_index=True) # ignore_index=True ensures the index is reset

def plot_score_progression(df):
    fig, ax = plt.subplots(figsize=(8, 6)) # Create a figure and axis, figsize 8x6 looks good
    
    sns.set_style("whitegrid")
    sns.lineplot(data=df, x=df.index + 1, y='score', ax=ax) # ax parameter ensures the plot is drawn on the same figure
    
    ax.set_title('Score Progression')
    ax.set_xlabel('Question Number')
    ax.set_ylabel('Points')
    
    plt.tight_layout()
    return fig