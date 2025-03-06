import time
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

# State to control the timer
if "stop_timer" not in st.session_state:
    st.session_state.stop_timer = False

# Custom CSS for Background, Title, and Buttons
st.markdown(
    """
    <style>
        /* Background Color */
        .stApp {
            background-color:  #C9FFE5; 
        }
        /* Title Styling */
        .title {
        
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
            
        }
        /* Animated Name on Left */
        @keyframes colorChange {
            0% { color: #e74c3c; }
            25% { color: #3498db; }
            50% { color: #2ecc71; }
            75% { color: #f1c40f; }
            100% { color: #e74c3c; }
        }
        .animated-name {
            text-align: left;
            font-size: 30px;
            font-weight: bold;
            animation: colorChange 2s infinite;
            color: white;
            margin-bottom: 0px;
        }
        .subtitle {
            text-align: left;
            color: Red;
            font-size: 14px;
            font-style: italic;
            margin-top: 0px;
            margin-bottom: 20px;
        }

        
          /* Timer Text */
        .timer-text {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #f1c40f;
        }
        /* Input Box */
        .stNumberInput > div {
            width: 100px !important;
            margin: auto;
            text-align: center;
            border: 3px solid #FFC9E3;
            
        }
        /* Button Styling */
        .stButton>button {
            font-size: 16px;
            padding: 8px 16px;
            border-radius: 6px;
            border: none;
            cursor: pointer;
            transition: background 0.3s;
            
        }
        .stButton>button:first-child {
            background-color: #3498db;
            color: white;
        }
        .stButton>button:first-child:hover {
            background-color: #2980b9;
        }
        .stButton>button:nth-child(2) {
            background-color: #e74c3c;
            color: white;
        }
        .stButton>button:nth-child(2):hover {
            background-color: #c0392b;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Left-aligned name and created by text
st.markdown("<p class='subtitle'>- Created by</p>", unsafe_allow_html=True)
st.markdown("<p class='animated-name'>Farhana Ahsan</p>", unsafe_allow_html=True)


# Title (Centered)
st.markdown("<h1 class='title'>Countdown Timer</h1>", unsafe_allow_html=True)

# Input field for countdown time (Centered & Styled)
seconds = st.number_input("⏳ Time (sec):", min_value=1, value=10, step=1, key="time", format="%d")

# Buttons in Same Row
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    start = st.button("Start Timer", key="start", help="Click to Start Timer", use_container_width=True)

with col3:
    stop = st.button("Stop Timer", key="stop", help="Click to Stop Timer", use_container_width=True)

# Timer Display
placeholder = st.empty()

# Timer Logic
if start:
    st.session_state.stop_timer = False  # Reset stop state
    for i in range(seconds, -1, -1):
        if st.session_state.stop_timer:
            placeholder.markdown("<h1 class='timer-text'>Stopped</h1>", unsafe_allow_html=True)
            break
        
        minutes = i // 60
        sec = i % 60
        placeholder.markdown(
            f"<h1 class='timer-text'>{minutes:02d}:{sec:02d}</h1>",
            unsafe_allow_html=True,
        )
        time.sleep(1)

    if not st.session_state.stop_timer:
        st.success("⏰ Time's Up!")

# Stop Timer Logic
if stop:
    st.session_state.stop_timer = True
