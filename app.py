import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Student Productivity Tracker", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Study Tracker", "Goals", "Feedback", "About"])

# ---------------- HOME ----------------
if page == "Home":

    st.title("📚 Student Productivity Tracker")

    st.header("Welcome")
    st.write("This app helps students track their study habits and productivity.")

    st.subheader("Daily Motivation")
    st.info("Small progress every day leads to big success.")

    st.success("Tip: Study consistently!")

    st.warning("Avoid procrastination.")

    st.error("Do not overload yourself with tasks.")

    st.markdown("---")

    st.metric("Study Streak", "5 Days")

    progress = st.progress(60)

    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644", caption="Stay Focused!")

# ---------------- STUDY TRACKER ----------------
elif page == "Study Tracker":

    st.title("📝 Study Tracker")

    name = st.text_input("Enter your name")

    subject = st.selectbox(
        "Select Subject",
        ["Math", "Science", "Programming", "History", "English"]
    )

    study_date = st.date_input("Study Date", datetime.date.today())

    study_time = st.slider("Study Hours", 0, 10)

    difficulty = st.radio(
        "Difficulty Level",
        ["Easy", "Medium", "Hard"]
    )

    topics = st.multiselect(
        "Topics Covered",
        ["Lecture", "Homework", "Reading", "Practice Problems"]
    )

    notes = st.text_area("Study Notes")

    focus = st.checkbox("I studied with full focus")

    mood = st.select_slider(
        "Mood While Studying",
        options=["😞", "😐", "🙂", "😄"]
    )

    if st.button("Submit Study Log"):
        st.success("Study log saved!")

# ---------------- GOALS ----------------
elif page == "Goals":

    st.title("🎯 Study Goals")

    goal = st.text_input("Enter your weekly study goal")

    hours_goal = st.number_input("Target Study Hours", min_value=1, max_value=100)

    deadline = st.date_input("Goal Deadline")

    st.write("Goal Progress")

    progress_goal = st.slider("Progress (%)", 0, 100)

    st.progress(progress_goal)

    if st.button("Save Goal"):
        st.success("Goal saved successfully!")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.title("💬 Feedback Form")

    rating = st.slider("Rate this app", 1, 10)

    recommend = st.radio(
        "Would you recommend this app?",
        ["Yes", "Maybe", "No"]
    )

    comments = st.text_area("Additional Comments")

    uploaded_file = st.file_uploader("Upload Screenshot (Optional)")

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# ---------------- ABOUT ----------------
elif page == "About":

    st.title("ℹ️ About This App")

    st.subheader("What the App Does")
    st.write("""
    The Student Productivity Tracker helps students record their study sessions,
    track study goals, and monitor productivity.
    """)

    st.subheader("Target Users")
    st.write("""
    - College students  
    - High school students  
    - Anyone who wants to improve study habits
    """)

    st.subheader("Inputs Collected")
    st.write("""
    - Student name
    - Study subject
    - Study hours
    - Topics covered
    - Study notes
    - Mood and focus level
    """)

    st.subheader("Outputs")
    st.write("""
    - Study logs
    - Progress tracking
    - Productivity insights
    """)    