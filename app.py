

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id: object) -> object:
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8c91640508de77d5858bb4c96f10e6ee".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters



movies_dict =pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')


selected_movie_name = st.selectbox('Type or select a movie from the dropdown', movies['title'].values)


if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



st.markdown("Made by **Aryan🤍**")

col1, col2 = st.columns([4, 1])

with col1:
    # Your content here
    pass  # Add this line if you don't have any content

with col2:
    if st.button("**Contact me:**"):
        st.markdown("""
        * **GitHub:** [Aryan Mishra]((https://github.com/Aryan-18bit/aryanmishra))
        * **LinkedIn:** [Aryan Mishra]((https://www.linkedin.com/in/aryan-mishra-484482265))
        """)













