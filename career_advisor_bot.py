import streamlit as st

st.set_page_config(page_title="Career Advisor", layout="wide")

# Custom CSS for style
st.markdown("""
    <style>
    body {
        background-color: #f4f6f9;
    }
    .main {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .title {
        font-size: 38px;
        font-weight: bold;
        color: #4A90E2;
    }
    .sub {
        font-size: 22px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 class='title'>🔐 Welcome to Career Advisor</h1>", unsafe_allow_html=True)

st.markdown("### 👋 Please sign in to continue")
email = st.text_input("Email", placeholder="Enter your email")
password = st.text_input("Password", placeholder="Enter your password", type="password")

if st.button("Login"):
    if email and password:
        st.success("✅ Login successful!")
        st.balloons()

        # ---------------- DETAILS PAGE ----------------
        st.markdown("---")
        st.markdown("## 🧾 Enter Your Details")

        name = st.text_input("👤 Name")
        age = st.number_input("🎂 Age", min_value=10, max_value=100)
        stream = st.selectbox("📚 Your Stream", ["AI & DS", "Computer Science", "Commerce", "Arts", "Others"])
        interest = st.text_input("💡 Your Primary Interest (e.g., Data Science, Law, Design, Psychology...)")
        img = st.file_uploader("📸 Upload Your Profile Photo (Optional)", type=["jpg", "png", "jpeg"])

        if st.button("Suggest Career"):
            st.markdown("---")
            st.markdown(f"### 👋 Hello **{name.title()}**!")
            if img:
                st.image(img, width=150)

            st.markdown(f"##### 🎓 Based on your interest in **{interest.title()}**, we recommend:")

            # Career Suggestions
            career = "🔍 Try being curious! Explore multiple fields."
            if "data" in interest.lower():
                career = "💻 Data Scientist, Analyst, ML Engineer"
            elif "design" in interest.lower():
                career = "🎨 UI/UX Designer, Product Designer"
            elif "law" in interest.lower():
                career = "⚖️ Legal Advisor, Corporate Lawyer"
            elif "psychology" in interest.lower():
                career = "🧠 Psychologist, Counselor, HR Specialist"
            elif "business" in interest.lower():
                career = "📈 Business Analyst, Entrepreneur, Product Manager"

            st.success(career)

            st.markdown("""
                > _✨ "Choose a job you love, and you will never have to work a day in your life."_  
                — Confucius
            """)
    else:
        st.error("❗Please fill in both email and password to continue.")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🚀 Built with ❤️ by Priyal Khunia")
