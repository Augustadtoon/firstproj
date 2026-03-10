import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="RTU Student Productivity Tracker", layout="wide")

# ---------------- HEADER ----------------
st.title("🎓 RTU Student Productivity Tracker")
st.caption("Rizal Technological University - Productivity Monitoring App")

# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/4/4a/Rizal_Technological_University_logo.png", width=120)
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Home", "Study Tracker", "Study Dashboard", "Goals", "Feedback", "About"])

# Sample data storage
if "study_data" not in st.session_state:
    st.session_state.study_data = []

# ---------------- HOME ----------------
if page == "Home":

    st.header("Welcome Students 👋")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("About the App")
        st.write("""
        This application helps *RTU students* track their study time,
        productivity, and learning habits.
        """)

        st.info("📌 Tip: Consistent study habits improve long-term learning.")

    with col2:
        st.subheader("Motivation")
        st.success("“Small progress each day adds up to big results.”")

        st.metric("Weekly Study Target", "20 Hours")

        st.progress(70)

    st.divider()

    st.subheader("Quick Reminders")

    st.warning("Avoid procrastination.")
    st.error("Do not overload yourself with tasks.")
    st.success("Stay consistent with your study routine!")

# ---------------- STUDY TRACKER ----------------
elif page == "Study Tracker":

    st.header("📝 Log Study Session")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name")

        subject = st.selectbox(
            "Subject",
            ["Programming", "Mathematics", "Database", "Networking", "English"]
        )

        study_date = st.date_input("Study Date", datetime.date.today())

        study_time = st.slider("Study Hours", 0, 10)

    with col2:
        difficulty = st.radio(
            "Difficulty Level",
            ["Easy", "Medium", "Hard"]
        )

        topics = st.multiselect(
            "Topics Covered",
            ["Lecture", "Assignment", "Reading", "Practice Coding"]
        )

        mood = st.select_slider(
            "Mood While Studying",
            options=["😞", "😐", "🙂", "😄"]
        )

        focus = st.checkbox("I studied with full focus")

    notes = st.text_area("Study Notes")

    if st.button("Save Study Log"):

        new_data = {
            "Name": name,
            "Subject": subject,
            "Date": study_date,
            "Hours": study_time,
            "Difficulty": difficulty
        }

        st.session_state.study_data.append(new_data)

        st.success("Study session saved!")

# ---------------- STUDY DASHBOARD ----------------
elif page == "Study Dashboard":

    st.header("📊 Study Dashboard")

    if len(st.session_state.study_data) == 0:

        st.info("No study data yet. Add a study log first.")

    else:

        df = pd.DataFrame(st.session_state.study_data)

        st.subheader("Study Records")
        st.dataframe(df)

        st.subheader("Study Hours Chart")
        st.bar_chart(df["Hours"])

        st.subheader("Subjects Distribution")
        st.write(df["Subject"].value_counts())

# ---------------- GOALS ----------------
elif page == "Goals":

    st.header("🎯 Study Goals")

    goal = st.text_input("Weekly Study Goal")

    hours_goal = st.number_input(
        "Target Study Hours",
        min_value=1,
        max_value=100
    )

    deadline = st.date_input("Goal Deadline")

    progress_goal = st.slider("Goal Progress (%)", 0, 100)

    st.progress(progress_goal)

    if st.button("Save Goal"):
        st.success("Goal saved successfully!")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.header("💬 Feedback Form")

    rating = st.slider("Rate this App", 1, 10)

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

    st.header("ℹ️ About This Project")

    st.subheader("Project Information")

    st.write("""
    *Application Name:* RTU Student Productivity Tracker  
    *Course:* Streamlit UI Development  
    *Purpose:* The RTU Student Productivity Tracker is designed to help students bridge the gap between "being busy" and 
    "being productive. By logging focused study sessions, students can identify patterns in their learning habits and 
    stay committed to their academic goals.
    """)
    
    st.subheader("Target Users")

    st.write("""
    RTU students who want to improve their study habits and productivity.
    """)
    st.subheader("Main Features")

    st.write("""
    - Study session tracking  
    - Goal monitoring  
    - Productivity dashboard  
    - Feedback collection  
    """)

    st.subheader("Developed By")

    st.write("""
    August Adtoon
    """)

    
