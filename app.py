# Description: This script contains the Streamlit app code for the IMDb Directors Quiz.

import streamlit as st
import datetime
import matplotlib.pyplot as plt
from data_preparation import load_and_clean_data
from quiz_generation import generate_question
from scoring import calculate_score
from visualization import initialize_quiz_history, add_quiz_result, plot_score_progression

# Page configuration
st.set_page_config(
    page_title="IMDB Directors Quiz",
    layout="wide",
    initial_sidebar_state="auto"
)

# Session state initialization
# This will store the current stage of the quiz, questions, current question index, quiz history and score.

if 'stage' not in st.session_state:
    st.session_state.stage = 'welcome'
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'quiz_history' not in st.session_state:
    st.session_state.quiz_history = initialize_quiz_history()
if 'score' not in st.session_state:
    st.session_state.score = 0

# Load data
df = load_and_clean_data()

# This is the initial screen that provides an overview of the quiz rules and instructions.
if st.session_state.stage == 'welcome':
    st.title("🎬 IMDB Directors Quiz")
    st.write("""
    ### Rules:
    - Total questions: 15 (5 easy, 5 medium, 5 hard)
    - Scoring: Easy = 10pts, Medium = 20pts, Hard = 30pts
    - Answer each question and click Next to proceed
    - Track your progress in real-time on the right
    """)
    
    # Start quiz button to begin and generate questions based on difficulty
    if st.button("Start Quiz", use_container_width=True):
        difficulties = ['easy'] * 5 + ['medium'] * 5 + ['hard'] * 5 # !!! find a better solution
        st.session_state.questions = [generate_question(df, diff) for diff in difficulties]
        st.session_state.stage = 'quiz'
        st.rerun()

# Quiz screen
elif st.session_state.stage == 'quiz':
    # Display quiz in 2 columns
    col1, col2 = st.columns([2, 1])
    
    # Display question and options on the left
    with col1:
        current = st.session_state.questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}/15")
        st.info(f"Difficulty: {current['difficulty'].title()}")
        
        st.write("### " + current['question'])
        answer = st.radio(
            "Select your answer:",
            current['options'],
            key=f"q_{st.session_state.current_question}",
            index=None
        )
        
        # Submit button to check answer and proceed to next question
        if st.button("Submit & Next", use_container_width=True, disabled=answer is None):
            is_correct = answer == current['correct_answer']
            points = calculate_score(is_correct, current['difficulty'])
            st.session_state.score += points
            
            # Display feedback correct/incorrect
            if is_correct:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Correct answer: {current['correct_answer']}")
            
            # Save quiz result to history
            result = {
                'question': current['question'],
                'user_answer': answer,
                'correct_answer': current['correct_answer'],
                'difficulty': current['difficulty'],
                'score': st.session_state.score
            }
            st.session_state.quiz_history = add_quiz_result(st.session_state.quiz_history, result)
            
            # Proceed to next question or results screen

            if st.session_state.current_question < 14:
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.session_state.stage = 'results'
                st.rerun()
    
    # Display score progression on the right
    with col2:
        st.subheader("Score Progression")
        if not st.session_state.quiz_history.empty:
            fig = plot_score_progression(st.session_state.quiz_history)
            st.pyplot(fig)
            plt.close()
        
        # Display current score
        st.metric("Current Score", st.session_state.score)

# Results screen

elif st.session_state.stage == 'results':
    st.title("Quiz Results")
    st.subheader(f"🏆 Final Score: {st.session_state.score}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create the results dataframe
        results_df = st.session_state.quiz_history[['question', 'user_answer', 'correct_answer', 'difficulty', 'score']]
        
        # Add styling
        def highlight_correct(row):
            is_correct = row['user_answer'] == row['correct_answer']
            return ['background-color: #90EE90' if is_correct else 'background-color: #FFB6C1'] * len(row)
        
        # Display styled dataframe
        st.write("### Quiz Summary")
        styled_df = results_df.style.apply(highlight_correct, axis=1)
        st.dataframe(styled_df, use_container_width=True)
    
    with col2:
        # Create a line plot of score progression
        fig = plot_score_progression(st.session_state.quiz_history)
        st.pyplot(fig)
        plt.close()
    
    if st.button("Play Again", use_container_width=True):
        for key in ['stage', 'questions', 'current_question', 'quiz_history', 'score']:
            if key in st.session_state: # Clear session state
                del st.session_state[key]
        st.rerun()

