
# IMDb Quiz App 🎥

The **IMDb Quiz App** is an interactive web application where users can test their movie directors knowledge! The app dynamically generates movie-related multiple-choice questions using an IMDb dataset. Built with Python and Streamlit, it offers a fun and challenging experience with difficulty-based scoring and visual feedback on performance.

This project is developed for the [Coding for Data Science and Data Management](https://www.unimi.it/en/education/degree-programme-courses/2025/coding-data-science-and-data-management) course.

Play it on: https://imdb-quiz-app.streamlit.app/

---

## Features 🚀

- **Dynamic Question Generation**: Randomly generated questions: "Who directed [Movie Title]?".
- **Difficulty Levels**:
  - Easy: Random directors from the dataset.
  - Medium: Directors from movies in the same genre.
  - Hard: Directors from movies released within ±5 years of the selected movie.
- **Scoring System**: Earn points based on difficulty (10 for easy, 20 for medium, 30 for hard).
- **Visual Feedback**:
  - Line chart showing cumulative score progression.
  - Dataframe showing showing results at the end of the game.
- **Streamlit Integration**: Fully interactive and user-friendly interface.

---

## Demo 🖥️

Run the app locally or deploy it online with Streamlit.

---

## Installation and Setup ⚙️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kosetalha/imdb-quiz-app.git
   cd imdb-quiz-app
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

4. **Enjoy the Quiz**:
   Open your browser and navigate to `http://localhost:8501` to start playing!

---

## Project Structure 📂

```
imdb-quiz-app/
├── data/                     # Dataset folder
│   └── imdb_top_1000.csv     # IMDb dataset
├── app.py                    # Main Streamlit app
├── data_preparation.py       # Data loading and cleaning module
├── quiz_generation.py        # Quiz question generator
├── scoring.py                # Scoring system module
├── visualization.py          # Visualizations module
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## Dataset 📊

- The app uses the **IMDb Top 1000 Movies Dataset**, retrieved from https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows.
- The dataset includes key information about movies such as titles, genres, directors, and more.
- Location: `data/imdb_top_1000.csv`.

---

## How It Works 🛠️

1. **Data Preparation**:
   - Load and clean the dataset.
   - Select relevant columns.
2. **Question Generation**:
   - Randomly pick a movie and generate a question about its director.
   - Provide incorrect answers based on difficulty.
3. **Scoring**:
   - Assign points for correct answers based on difficulty.
   - Update the cumulative score.
4. **Visualization**:
   - Display the score progression and difficulty breakdown.

---

## Contributing 🤝

All contributions are welcome. Here's how you can help:
- Report bugs or suggest features via [Issues](https://github.com/kosetalha/imdb-quiz-app/issues).
- Fork the repository, make your changes, and submit a pull request.

---

## License 📄

This project is licensed under the MIT License.

---
