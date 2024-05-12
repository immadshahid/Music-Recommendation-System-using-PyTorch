import streamlit as st

# Create a Streamlit app
st.title("SpotiVibe")

# Create a container for the header section
header_container = st.container()

# Add the header content to the container
with header_container:
    st.subheader("Who We Are")
    st.write("At SpotiVibe, we live and breathe music. Our team of music enthusiasts is dedicated to revolutionizing your listening experience.")
    st.write("With cutting-edge technology and a passion for melodies, we're here to elevate your music journey like never before.")
    st.write("Join us on this musical adventure and let the rhythm take you to new heights!")

# Create a container for the team section
team_container = st.container()

# Add the team content to the container
with team_container:
    st.subheader("Meet Our Maestros")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("assets/images/IMG_1128.JPG", caption="Immad Shahid")
        st.write("Hail to the Chief Musician")
    with col2:
        st.image("assets/images/photo-1545386673-7723f55e5490.jpeg", caption="Harmony Grace")
        st.write("Sound Sorceress")
    with col3:
        st.image("assets/images/photo-1596421250711-9ec0ef9cbba3.jpeg", caption="Rhythm Reed")
        st.write("Beat Wizard")
    with col4:
        st.image("assets/images/photo-1589571739149-47ed80eae6ba.jpeg", caption="Lyric Luna")
        st.write("Melody Maven")

# Create a container for the featured mixes section
mixes_container = st.container()

# Add the featured mixes content to the container
with mixes_container:
    st.subheader("Featured Mixes")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("assets/images/photo-1494232410401-ad00d5433cfa.jpeg", caption="Chill")
        st.write("Soothing Serenades Vol. 1")
        st.button("Listen", key="chill-button")
    with col2:
        st.image("assets/images/photo-1605731414532-6b26976cc153.jpeg", caption="Party")
        st.write("Energetic Beats Vol. 1")
        st.button("Listen", key="party-button")
    with col3:
        st.image("assets/images/photo-1496293455970-f8581aae0e3b.jpeg", caption="Focus")
        st.write("Productivity Boost Vol. 1")
        st.button("Listen", key="focus-button")
    with col4:
        st.image("assets/images/photo-1511379938547-c1f69419868d.jpeg", caption="Workout")
        st.write("Sweat Session Vol. 1")
        st.button("Listen", key="workout-button")

# Create a container for the FAQ section
faq_container = st.container()

# Add the FAQ content to the container
with faq_container:
    st.subheader("Got Questions? We've Got Answers!")
    st.write("Q: What is SpotiVibe?")
    st.write("A: SpotiVibe is a music recommendation platform that uses AI to suggest personalized playlists and tracks.")
    st.write("Q: How does it work?")
    st.write("A: Simply create an account, input your music preferences, and our AI algorithm will generate a personalized playlist for you.")
    st.write("Q: Is it free?")
    st.write("A: Yes, SpotiVibe is completely free to use. No ads, no subscriptions, no hidden fees.")