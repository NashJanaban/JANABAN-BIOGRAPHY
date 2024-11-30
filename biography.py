import streamlit as st

st.set_page_config(page_title="Nash Biography", page_icon=":collision:", layout="wide")

col1, col2 = st.columns([1, 1]) 
with col1:
    st.image("https://scontent.xx.fbcdn.net/v/t1.15752-9/463211923_1258770261997420_2210241824044250435_n.jpg?stp=dst-jpg_s480x480&_nc_cat=105&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeHv_5G8LOJekPY7nvjRP3piQHxyDlyEhE1AfHIOXISETct-27_j21INcRDclZ2dRdp8kXrDhhN59f4DO0mPni92&_nc_ohc=uECPib8fDyQQ7kNvgH62kn2&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QGd7ceg5YSHps0lwdFdMB2LAqb3HXSiPm7NAoQk5HNrhg&oe=6772A0F5", width=400,)
with col2:
    st.write("###")
    st.write("###")
    st.title("**NASH EOWYN Y. JANABAN**")
    st.write(
        "A Computer Engineering student, activity in Programming Logic and Design Called - Biography Streamlit "
    )
  
st.write("\n")
st.subheader("Personal Details")
st.write(
    """- Name is Nash Eowyn Y. Janaban
- Birthday May 11, 2006
- Age 18 years old
- Course is Bachelor of Science in Computer Engineering.
- First year college student"""
, height=150
)
st.write("\n")
st.subheader("Family Background",)
st.text_area("",
    """Father's Name is Ian P. Janaban
Birthday: October 4, 1978

Mother's Name is Meryl Y. Janaban
Birthday: April 6, 1981

Sister's Name is Schinina Isabella Y. Janaban
Birthday: February 19, 2009""", height=230
)

st.write("\n")
st.subheader("Educational Attainment")
st.text_area("",
    """Elementary, Surigao City Pilot School
High School, Nemco
Senior High, Surigao Norte National High School
""", height=100
)

st.title("Achievements")
st.subheader("What I achieve")
st.text_area("","""I'm an consistent with honor since Grade 11 and 12, where I consistently excelled in my studies and participated in various extracurricular activities. During this time, I developed a strong foundation in technology and computer skills. One of my significant accomplishments was that I successfully passed the NC2 in CSS, which certified my proficiency in web development and gave me the confidence to pursue further learning in the field of programming and design.
""", height=180,
) 

st.title("My skills")
st.subheader("The skills that I learn")
st.text_area("","""As a computer enthusiast, I have gained experience in various aspects of computer technology, including working with the programming language Python to develop applications and automate tasks. Additionally, I have explored disassembly and assembly computer techniques, which allow me to understand and repair hardware components effectively. I am also skilled in installing servers for different purposes, such as hosting websites or managing databases. Whether it’s setting up a new system or optimizing an old one, I am proficient in formatting computers to ensure they run smoothly. Furthermore, I have hands-on experience with Wi-Fi configuration, troubleshooting network issues, and optimizing connectivity to ensure reliable internet access for users.""", height=270
)
   
