import pickle
import pandas as pd
import streamlit as st
import requests


st.title('Movie Recommendor')

def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a2ec521b7f6c6f01fd79d44b1ed3fb7a&language=en-US'.format(movie_id))
   data = response.json()

   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):# reccomends 5 movies
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    reccomended_movies = []
    recommended_movie_poster = []

    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id  # list ke 1st index pr movie ki id hai , jo hm recommended_movie_poster ke list me append kr rahey hai aur fetch bhi

        reccomended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movie_poster.append( fetch_poster(movie_id))

    return reccomended_movies , recommended_movie_poster


movies_dict = pickle.load(open('movie_dict.pkl ','rb'))
movies = pd.DataFrame(movies_dict)

similarity =  pickle.load(open('similarity.pkl ','rb'))

selected_movie_name = st.selectbox(
'Enter the movie of your preference',
movies['title'].values )

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

#to run comman= streamlit run app.py