import streamlit as st

st.set_page_config(
    page_title="My Profile",
    page_icon="🌷",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #222222;
}

.sub-title {
    font-size: 20px;
    color: #666666;
    margin-bottom: 24px;
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 12px;
    color: #222222;
}

.info-box {
    background-color: #f8f8f8;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 14px;
    border: 1px solid #eeeeee;
}

.small-text {
    color: #666666;
    font-size: 16px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Menu",
    ["Home", "About", "Education", "Interests", "Contact"]
)

if menu == "Home":
    st.markdown('<div class="main-title">Hello, I\'m SiaLee</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-title">Master\'s student in Mathematics Education</div>',
        unsafe_allow_html=True
    )

    st.write("""
    I am a graduate student in Mathematics Education with a strong interest in meaningful learning,
    student growth, and effective mathematics teaching.
    """)

    st.write("""
    I value sincerity, steady growth, and creating positive learning experiences.
    """)

    st.markdown("""
    **One-line Introduction**  
    Passionate about Mathematics Education
    """)

elif menu == "About":
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>Name:</b> [Sia Lee]<br>
    <b>Program:</b> Master's in Mathematics Education<br>
    <b>Focus:</b> Meaningful learning, student-centered teaching, and mathematical understanding
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-text">
    I am interested in helping students understand mathematics in a deeper and more meaningful way.
    I hope to become an educator who connects mathematical thinking with positive classroom experiences.
    </div>
    """, unsafe_allow_html=True)

elif menu == "Education":
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>Master's student in Mathematics Education</b><br>
    Studying mathematics teaching and learning with an interest in effective instructional methods.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>Academic Interest</b><br>
    Mathematics teaching, student understanding, and meaningful classroom learning.
    </div>
    """, unsafe_allow_html=True)

elif menu == "Interests":
    st.markdown('<div class="section-title">Interests</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    - Mathematics Education<br>
    - Student-centered learning<br>
    - Meaningful teaching practices<br>
    - Educational growth and communication
    </div>
    """, unsafe_allow_html=True)

elif menu == "Contact":
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <b>Email:</b> sialee@korea.ac.kr<br>
    <b>Tel: </b> 010-9259-9068
    </div>
    """, unsafe_allow_html=True)
