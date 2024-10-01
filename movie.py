import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id): 
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()  # Fixed: Added assignment operator
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']  # Fixed: Added closing parenthesis

# Function to recommend movies based on the given movie
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters  # Fixed: Return posters too

# Load the movie list and similarity matrix from the pickle files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Extract the list of movie titles for the selectbox
movie_list = movies['title'].values

# Set the background color to black
st.markdown(
    """
    <style>
    .reportview-container {
        background: black;
    }
    .title {
        color: red;
    }
    .movie-name {
        color: red; /* Style for movie names */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the Streamlit app
st.markdown('<h1 class="title">Movie Recommender System</h1>', unsafe_allow_html=True)

# Selectbox for movie selection
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',  
    movie_list
)

# Button to generate recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)  # Fixed: Assign the returned values

    # Creating columns for displaying posters
    col1, col2, col3, col4, col5 = st.columns(5)  # Updated: Used st.columns instead of st.beta_columns
     
    with col1:
        st.markdown(f'<p class="movie-name">{names[0]}</p>', unsafe_allow_html=True)  # Changed to HTML
        st.image(posters[0])  # Fixed: Corrected the syntax for displaying images

    with col2:
        st.markdown(f'<p class="movie-name">{names[1]}</p>', unsafe_allow_html=True)  # Changed to HTML
        st.image(posters[1])  # Fixed: Corrected the syntax for displaying images

    with col3:
        st.markdown(f'<p class="movie-name">{names[2]}</p>', unsafe_allow_html=True)  # Changed to HTML
        st.image(posters[2])  # Fixed: Corrected the syntax for displaying images

    with col4:
        st.markdown(f'<p class="movie-name">{names[3]}</p>', unsafe_allow_html=True)  # Changed to HTML
        st.image(posters[3])  # Fixed: Corrected the syntax for displaying images

    with col5:
        st.markdown(f'<p class="movie-name">{names[4]}</p>', unsafe_allow_html=True)  # Changed to HTML
        st.image(posters[4])  # Fixed: Corrected the syntax for displaying images 
