import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

#---------------- STYLE ----------------

st.markdown("""

<style>
  

  
.stApp {
  
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
  
    font-family: Arial, sans-serif;
  
}
  

  
[data-testid="stHeader"] {
  
    background: transparent !important;
  
}
  

  
.block-container {
  
    padding-top: 2.5rem;
  
    padding-bottom: 2.5rem;
  
}
  

  
/* TEXT */
  
html, body, .stApp, p, div, span, label {
  
    color: #111111 !important;
  
    font-weight: 700 !important;
  
}
  

  
/* TITLE */
  
h1 {
  
    text-align: center;
  
    color: white !important;
  
    font-weight: 900 !important;
  
}
  

  
/* CARD */
  
.card {
  
    background: rgba(255, 255, 255, 0.30);
  
    backdrop-filter: blur(10px);
  
    -webkit-backdrop-filter: blur(10px);
  
    padding: 18px;
  
    border-radius: 14px;
  
    box-shadow: 0 6px 18px rgba(0,0,0,0.10);
  
    margin-bottom: 15px;
  
    border: 1px solid rgba(255, 255, 255, 0.25);
  
    text-align: center;
  
}
  

  
/* SIDEBAR */
  
section[data-testid="stSidebar"] {
  
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
  
}
  

  
section[data-testid="stSidebar"] * {
  
    color: white !important;
  
    font-weight: 700 !important;
  
}
  

  
</style>""", unsafe_allow_html=True)

#---------------- TITLE ----------------

st.markdown("<h1>💼 My Projects</h1>", unsafe_allow_html=True)

#---------------- PROJECT GRID ----------------

col1, col2 = st.columns(2)

with col1:

st.markdown("""

<div class="card">

<h3>🌐 Portfolio App</h3>

<p>Streamlit Multipage Portfolio</p>

</div>

""", unsafe_allow_html=True)

with col2:

st.markdown("""

<div class="card">

<h3>👩‍💻 Personal Website</h3>

<p>HTML/CSS Personal Portfolio Design</p>

</div>

""", unsafe_allow_html=True)

#---------------- THIRD PROJECT ----------------

st.markdown("""

<div class="card"><h3>🎨 Bootstrap Project</h3><p>Responsive Web Design Practice using Bootstrap</p></div>""", unsafe_allow_html=True)

Add the thinks we do like calculator in pydroidcol1, col2 = st.columns(2)

# LEFT COLUMN
with col1:
    st.markdown("""
    <div class="card">
    <h3>🌐 Portfolio App</h3>
    <p>Streamlit multipage portfolio showcasing projects.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧮 Calculator App</h3>
    <p>Python calculator built in Pydroid with basic operations.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>📊 Simple Grading System</h3>
    <p>Python
