# career_advisor_bot.py

import streamlit as st

st.title("🎓 Career Advisor Bot")
st.subheader("Get career suggestions based on your interests!")

# Step 1: Get user input
interest = st.text_input("What is your primary interest? (e.g., Data Science, Design, Law)")

# Step 2: Recommend career based on input
if st.button("Suggest Career"):
    if "data" in interest.lower():
        st.success("💡 Suggested Career: Data Scientist, Analyst, ML Engineer")
    elif "design" in interest.lower():
        st.success("💡 Suggested Career: UI/UX Designer, Graphic Designer, Product Designer")
    elif "law" in interest.lower():
        st.success("💡 Suggested Career: Legal Advisor, Human Rights Lawyer, Corporate Lawyer")
    else:
        st.warning("Hmm... Try giving a more specific interest!")

st.markdown("---")
st.caption("Built with ❤️ by Priyal Khunia")
