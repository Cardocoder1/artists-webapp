from PIL import Image
import streamlit as st
import urllib.parse

#___layout______
st.set_page_config(layout="wide")
import streamlit as st
st.sidebar.header("sidebar")

# Inject CSS to reduce top padding
st.markdown("""
    <style>
           .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }
    </style>
    """, unsafe_allow_html=True)


# Inject custom CSS to split backgrounds
st.markdown(
    """
    <style>
    /* Main page background */
    .stApp {
        background: linear-gradient(135deg, #1e2022 0%, #121212 100%);
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color:   #090a0b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#___loaded assets___
image_upload = Image.open("images/1_image.JPG")
st.logo("images/profile.JPG",size="large")





#___introduction of young kay___
with st.container():
    st.write("__")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(image_upload)
    with right_column:
        st.title("AM YOUNG KAY")
        st.write("Meet Young Kay, a talented and ambitious emerging zambian artist determined to take the music scene by storm."
                 " Known for his authentic style, captivating energy, and dedication to his craft, "
                 "Young Kay is building a name for himself one song at a time. As he continues to grow and evolve, "
                 "he is focused on delivering music that inspires, entertains, and connects with audiences around the world.")





st.divider()

#___collecting user data_____
st.title("contact me")
st.caption("for bookings, collabs or sponsorships.")
number = st.text_input("enter a phone number or email which we will use to contact you.")
message = st.text_area("enter a short description of what we can do for you.")

#___user data____
message = f"""
   my number/email: {number}
   my request: {message}
   """

#___generating whatsapp link___
encoded_message = urllib.parse.quote(message)
url = f"https://wa.me/260971234567?text={encoded_message}"

#___verifying inputs___

#___send data to whatsapp___
st.link_button("submit",url)

st.divider()


st.caption("click a link below to visit my page ")

st.markdown("""
<style>
.link-bar {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin: 1rem 0;
}

.link-bar a {
    display: inline-block;
    padding: 5px 10px;
    background-color:  #1e293b;
    color: #ffffff !important;
    text-decoration: none !important;
    font-weight: 600;
    border-radius: 8px;
    transition: background-color 0.2s ease, transform 0.2s ease;
}

.link-bar a:hover {
    background-color:  #334155;
    transform: translateY(-2px);
}

.link-bar a:active {
    transform: translateY(0);
}
</style>

<div class="link-bar">
     <a href="https://www.tiktok.com/@abelmvula141gmail.com?_r=1&_t=ZS-9AovjENLMSj" rel="noopener noreferrer"> tiktok</a>
    <a href="https://www.facebook.com/share/1GwQSirL8a/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer">facebook</a>
    <a href="https://youtube.com/@youngkayzambia?si=_-TD9_OtE9j9oQhX" rel="noopener noreferrer"> youtube</a>
</div>
""", unsafe_allow_html=True)
