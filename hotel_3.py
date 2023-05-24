###########################################HOTEL3#######################################################
########################################################################################################
def get_image_path(hotel_name):
    if hotel_name == "Hotel Bergamo":
        return "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/bergamo_hotel.jpg"
    elif hotel_name == "Hotel Krauthof":
        return "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/krauthof_hotel.jpg"
    elif hotel_name == "Best Western Hotel Favorit":
        return "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/bestwestern_hotel.jpg"
    elif hotel_name == "ibis budget Ludwigsburg":
        return "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/ibis_hotel.jpg"
    elif hotel_name == "Schlosshotel Monrepos":
        return "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/monrepos_hotel.jpg"
    else:
        return None

if hotel_3:
    result = recommended_hotels("Gastehaus Siebenschlafer")
    result = [hotel for hotel in result if hotel != "Gastehaus Siebenschlafer"]
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