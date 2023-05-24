import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import os

df = pd.read_excel("https://github.com/elcintimurcakmak/myadvice_app/blob/main/hotel_info.xlsx")
hotel = pd.read_excel("https://github.com/elcintimurcakmak/myadvice_app/blob/main/hotel_info.xlsx", sheet_name="hotel")
ratings = pd.read_excel("https://github.com/elcintimurcakmak/myadvice_app/blob/main/hotel_info.xlsx", sheet_name="ratings")

df_ = pd.merge(hotel, ratings, how="inner", on=["hotel_id"])
df = df_.copy()
df.head()

#GENEL SAYFA AYARI
st.set_page_config(
    page_title=" MYADVICE - BOOKING HOTELS IN LUDWIGSBURG",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="auto")

#SIDEBAR MYADVICE LOGOSU EKLEME
from PIL import Image
image_path = "https://github.com/elcintimurcakmak/myadvice_app/blob/main/hotels/nese7.png"
image = Image.open(image_path)
st.sidebar.image(image, use_column_width=True)


st.sidebar.write("<h3></h3>", unsafe_allow_html=True)
st.sidebar.write("<h3>HOTEL LIST</h3>", unsafe_allow_html=True)

def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['reviews'] = dataframe['reviews'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['reviews'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

def content_based_recommender(hotel_name, cosine_sim, dataframe):
    indices = pd.Series(dataframe.index, index=dataframe['hotel_name_x'])
    indices = indices[~indices.index.duplicated(keep='last')]
    hotel_index = indices[hotel_name]
    similarity_scores = pd.DataFrame(cosine_sim[hotel_index], columns=["scores"])
    similarity_scores = similarity_scores.reset_index()
    similarity_scores = similarity_scores.rename(columns={"index": "hotel_index"})
    similarity_scores = similarity_scores.sort_values("scores", ascending=False)
    recommended_indices = similarity_scores[similarity_scores["hotel_index"] != hotel_index]["hotel_index"]
    recommended_hotels = dataframe.loc[recommended_indices, :]
    return recommended_hotels['hotel_name_x'].unique()[:5]

def recommended_hotels(hotel_name):
    cosine_sim = calculate_cosine_sim(df)
    recommended_hotels = content_based_recommender(hotel_name, cosine_sim, df)
    return recommended_hotels

hotel_1 = st.sidebar.checkbox("Best Western Hotel Favorit", key="hotel_1")
hotel_2 = st.sidebar.checkbox("Boutique-Hotel Kronenstuben", key="hotel_2")
hotel_3 = st.sidebar.checkbox("City Hotel Ludwigsburg", key="hotel_3")
hotel_4 = st.sidebar.checkbox("Harbr. hotel Ludwigsburg", key="hotel_4")
hotel_5 = st.sidebar.checkbox("ibis budget Ludwigsburg", key="hotel_5")
hotel_6 = st.sidebar.checkbox("Komfort Hotel Ludwigsburg", key="hotel_6")
hotel_7 = st.sidebar.checkbox("Schlosshotel Monrepos", key="hotel_7")
hotel_8 = st.sidebar.checkbox("Westend Hotel", key="hotel_8")
hotel_9 = st.sidebar.checkbox("hotelmarchen Garni", key="hotel_9")
hotel_10 = st.sidebar.checkbox("Hotel Bergamo", key="hotel_10")
hotel_11 = st.sidebar.checkbox("Hotel City Oase Lb", key="hotel_11")
hotel_12 = st.sidebar.checkbox("Hotel Cocco Bello in der Villa Foret", key="hotel_12")

######################################################################################################
#################################SAĞ ÜST BANNER#######################################################
######################################################################################################
image_path = "https://github.com/elcintimurcakmak/myadvice_app/blob/main/hotels/banner_2.jpg"
image = Image.open(image_path)
#st.image(image, caption='Ludwigsburg', use_column_width=True)
st.image(image, use_column_width=True)

######################################################################################################
#################################SAĞ ORTA BANNER######################################################
######################################################################################################
image_path = "https://github.com/elcintimurcakmak/myadvice_app/blob/main/hotels/sub_banner.jpg"
image = Image.open(image_path)
#st.image(image, caption='Ludwigsburg', use_column_width=True)
st.image(image, use_column_width=True)


import streamlit as st
from PIL import Image


########################################################################################################
##########################################HOTEL RECOMMENDATIONS#########################################
########################################################################################################

########################################################################################################
###########################################HOTEL1#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "hotelmarchen Garni":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/garni_hotel.jpg"
    elif hotel_name == "Hotel Moerike":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/morike_hotel.jpg"
    elif hotel_name == "Schlosshotel Monrepos":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/monrepos_hotel.jpg"
    else:
        return None

if hotel_1:
    result = recommended_hotels("Best Western Hotel Favorit")
    result = [hotel for hotel in result if hotel != "Best Western Hotel Favorit"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")

########################################################################################################
###########################################HOTEL2#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel City Oase Lb":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/oase_hotel.jpg"
    elif hotel_name == "Hotel Riviera":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/riviera_hotel.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Gasthaus Hirschberg Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/hirschberg_gasthaus.jpg"
    else:
        return None

if hotel_2:
    result = recommended_hotels("Boutique-Hotel Kronenstuben")
    result = [hotel for hotel in result if hotel != "Boutique-Hotel Kronenstuben"]
    st.markdown("### Recommended Hotels")


    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")


#########################################################################################################
###########################################HOTEL3#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "City Hotel Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/city_hotel.jpg"
    elif hotel_name == "Westend Hotel":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/westend_hotel.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Hotel Goldener Pflug":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/goldener_hotel.jpg"
    elif hotel_name == "Komfort Hotel Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/komfort_hotel.jpg"
    else:
        return None

if hotel_3:
    result = recommended_hotels("City Hotel Ludwigsburg")
    result = [hotel for hotel in result if hotel != "City Hotel"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")


#########################################################################################################
###########################################HOTEL4#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "City Hotel Ludwigsburg":
            return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/city_hotel.jpg"
    elif hotel_name == "Hotel Goldener Pflug":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/goldener_hotel.jpg"
    elif hotel_name == "Gastehaus Siebenschlafer":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/siebenschlafer_gastehaus.jpg"
    else:
        return None

if hotel_4:
    result = recommended_hotels("Harbr. hotel Ludwigsburg")
    result = [hotel for hotel in result if hotel != "Harbr. hotel Ludwigsburg"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")

#########################################################################################################
###########################################HOTEL5#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel-Restaurant Poseidon":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/poseidon_hotel.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Schlosshotel Monrepos":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/monrepos_hotel.jpg"
    elif hotel_name == "hotelmarchen Garni":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/garni_hotel.jpg"
    else:
        return None

if hotel_5:
    result = recommended_hotels("ibis budget Ludwigsburg")
    result = [hotel for hotel in result if hotel != "ibis budget Ludwigsburg"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")

#########################################################################################################
###########################################HOTEL6#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Riviera":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/riviera_hotel.jpg"
    elif hotel_name == "Best Western Hotel Favorit":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bestwestern_hotel.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Hotel Goldener Pflug":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/goldener_hotel.jpg"
    else:
        return None

if hotel_6:
    result = recommended_hotels("Komfort Hotel Ludwigsburg")
    result = [hotel for hotel in result if hotel != "Komfort Hotel Ludwigsburg"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")



#########################################################################################################
###########################################HOTEL7#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Gasthaus Hirschberg Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/hirschberg_gasthaus.jpg"
    elif hotel_name == "Gastehaus Im Osterholz":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/osterholz_gastehaus.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Hotel-Restaurant Poseidon":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/poseidon_hotel.jpg"
    else:
        return None

if hotel_7:
    result = recommended_hotels("Schlosshotel Monrepos")
    result = [hotel for hotel in result if hotel != "Schlosshotel Monrepos"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")


#########################################################################################################
###########################################HOTEL8#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Krauthof":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/krauthof_hotel.jpg"
    elif hotel_name == "Hotel Goldener Pflug":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/goldener_hotel.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Gasthaus Hirschberg Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/hirschberg_gasthaus.jpg"
    else:
        return None

if hotel_8:
    result = recommended_hotels("Westend Hotel")
    result = [hotel for hotel in result if hotel != "Westend Hotel"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")


#########################################################################################################
###########################################HOTEL9#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Moerike":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/morike_hotel.jpg"
    elif hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "Hotel Krauthof":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/krauthof_hotel.jpg"
    elif hotel_name == "Hotel Cocco Bello in der Villa Foret":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/cocco_hotel.jpg"
    else:
        return None

if hotel_9:
    result = recommended_hotels("hotelmarchen Garni")
    result = [hotel for hotel in result if hotel != "hotelmarchen Garni"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")

#########################################################################################################
###########################################HOTEL10#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Cocco Bello in der Villa Foret":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/cocco_hotel.jpg"
    elif hotel_name == "Hotel Riviera":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/riviera_hotel.jpg"
    elif hotel_name == "Westend Hotel":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/westend_hotel.jpg"
    elif hotel_name == "Schlosshotel Monrepos":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/monrepos_hotel.jpg"
    else:
        return None

if hotel_10:
    result = recommended_hotels("Hotel Bergamo")
    result = [hotel for hotel in result if hotel != "Hotel Bergamo"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")

#########################################################################################################
###########################################HOTEL11#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Gasthaus Hirschberg Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/hirschberg_gasthaus.jpg"
    elif hotel_name == "Hotel Goldener Pflug":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/goldener_hotel.jpg"
    elif hotel_name == "Schlosshotel Monrepos":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/monrepos_hotel.jpg"
    elif hotel_name == "City Hotel Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/city_hotel.jpg"
    else:
        return None

if hotel_11:
    result = recommended_hotels("Hotel City Oase Lb")
    result = [hotel for hotel in result if hotel != "Hotel City Oase Lb"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")

#########################################################################################################
###########################################HOTEL12#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Bergamo":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/bergamo_hotel.jpg"
    elif hotel_name == "City Hotel Ludwigsburg":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/city_hotel.jpg"
    elif hotel_name == "Westend Hotel":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/westend_hotel.jpg"
    elif hotel_name == "Hotel Riviera":
        return "https://github.com/elcintimurcakmak/myadvice_app/tree/main/hotels/riviera_hotel.jpg"
    else:
        return None

if hotel_12:
    result = recommended_hotels("Hotel Cocco Bello in der Villa Foret")
    result = [hotel for hotel in result if hotel != "Hotel Cocco Bello in der Villa Foret"]
    st.markdown("### Recommended Hotels")

    for i, hotel in enumerate(result, start=1):
        col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
        col1.markdown(f"<b>Name:</b> {hotel}", unsafe_allow_html=True)
        image_path = get_image_path(hotel)  # Otelin fotoğraf yolunu alın

        if image_path is not None:
            image = Image.open(image_path)
            st.image(image, caption=hotel, use_column_width=True)
        else:
            st.write("No image available")
        st.markdown("---")



