# career_advisor_bot.py

import streamlit as st

# Title
st.title("🎓 Career Advisor Bot")
st.subheader("Get career suggestions based on your interests!")

# Sidebar
st.sidebar.title("👤 User Info")
name = st.sidebar.text_input("Enter your name:")
if name:
    st.write(f"Hi {name}! Let's explore your career path ✨")

# Selectbox for interests
interest = st.selectbox(
    "Choose your primary interest:",
    ["", "Data Science", "Design", "Law", "Marketing", "Cybersecurity", "Psychology"]
)

# File upload (just for future use/fun)
uploaded_file = st.file_uploader("📄 Upload your resume", type=["pdf", "docx"])
if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

# Career Suggestions
if st.button("Suggest Career"):
    if interest == "Data Science":
        st.success("👩‍💻 Suggested Careers: Data Scientist, Data Analyst, ML Engineer")
        st.info("📘 Learn Python, Pandas, SQL, Machine Learning")
    elif interest == "Design":
        st.success("🎨 Suggested Careers: UI/UX Designer, Product Designer")
        st.info("📘 Learn Figma, Adobe XD, User Research")
    elif interest == "Law":
        st.success("⚖️ Suggested Careers: Legal Advisor, Corporate Lawyer")
        st.info("📘 Learn Constitutional Law, Legal Drafting")
    elif interest == "Marketing":
        st.success("📢 Suggested Careers: Digital Marketer, SEO Analyst")
        st.info("📘 Learn SEO, Social Media Strategy, Google Ads")
    elif interest == "Cybersecurity":
        st.success("🛡️ Suggested Careers: Security Analyst, Ethical Hacker")
        st.info("📘 Learn Networking, Kali Linux, Penetration Testing")
    elif interest == "Psychology":
        st.success("🧠 Suggested Careers: Therapist, Research Psychologist")
        st.info("📘 Learn Counselling Techniques, Cognitive Science")
    else:
        st.warning("Please select an interest!")

# Fun image
st.image("https://cdn.pixabay.com/photo/2017/01/10/19/05/laptop-1967479_960_720.jpg", caption="You got this!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ by Priyal Khunia")
