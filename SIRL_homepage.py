from dis import disco
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageOps


  
def show_circular_image(path, size=(200, 200)):
    """Show a circular image"""
    img=Image.open(path)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output



st.title("Social Insight Research Lab")


with st.sidebar:
    st.title("Navigation")
    st.write("Use the sidebar to navigate to the different pages of the lab.")

    st.write("## Pages")
    pages = ["Home", "People", "Projects", "Publications", "Contact"]
    page = st.radio("Go to", pages)
    
if page == "Home":
    st.write("You are already on the homepage.")
elif page == "People":
    st.write("This is the people page.")

    images, discriptions = st.columns([2,5],)
    with images:
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.write("     ")
        st.image(show_circular_image('profile_images\Ashique.jpg'), caption= "Ashique KhudaBukhsh",
        width=200)

    with discriptions:
        st.subheader("Assistant Professor")
        st.write("Ashique KhudaBukhsh is currently an Assistant Professor at RIT. Prior to this role, he was a Project Scientist at CMU mentored by Prof. Tom Mitchell. He was a postdoc mentored by Prof. Jaime Carbonell. His current research focus is in Computational Social Science. In this field, he is interested in analyzing globally important events in South East Asia and developing methods for noisy social media texts generated in this linguistically diverse region. His other broad focus is US politics; he has offered a graduate course (team-taught with Prof. Mark S. Kamlet and Prof. Tom M. Mitchell) at the intersection of machine learning and political science focusing on the 2020 US election. A detailed resume can be found here. He is also a head of the RIT Social Insight Research Lab (SIRL).")


    st.write("---")
    images, discriptions = st.columns([2,5])
    with images:
        st.image(show_circular_image('profile_images\Sujan.jpg'), caption= "Sujan Dutta",
        width=185)

    with discriptions:
        st.subheader("PhD Candidate")

    st.write("---")
    images, discriptions = st.columns([1,3])
    with images:
        st.image(show_circular_image('profile_images\Adel.jpg'), caption= "Adel Khorramrouz",
        width=175)

    with discriptions:
        st.subheader("M.Sc Candidate")

    st.write("---")
    images, discriptions = st.columns([1,3],)
    with images:
        st.image(show_circular_image('profile_images\Seyd.jpg'), caption= "Syed Mohammad Sualeh A.",
        width=175)

    
    with discriptions:
        st.subheader("M.Sc Candidate")

    




elif page == "Projects":
    st.write("This is the projects page.")
elif page == "Publications":
    st.write("This is the publications page.")
elif page == "Contact":
    st.write("This is the contact page.")
