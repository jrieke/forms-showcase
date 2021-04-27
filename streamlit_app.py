import random
import time
import streamlit as st

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/crystal-ball_1f52e.png",
    width=100,
)

"""
# Try out `st.form`!

We built a super-secret algorithm to recommend a Streamlit app based on your personality. The problem: It takes very long to run. That's why we use a form to bundle all input widgets 👇
"""

""

with st.form(key="recommender"):
    st.write("Click **Submit** to get your recommendation!")
    st.selectbox(
        "Your favorite streamlit call",
        ["st.form", "st.balloons 🎈 ", "st.submit_button", "st.write"],
    )
    st.text_input("Your favorite thing to build streamlit apps for")
    st.slider("How excited you are about forms", 0, 11, 10)
    submitted = st.form_submit_button()

""

if submitted:
    with st.spinner("🤓 Crunching numbers..."):
        time.sleep(2)
    # fortunes = [
    #     "🥠 You will become an even better Streamlit developer",
    #     "🥠 You will use forms in all of your Streamlit apps",
    #     "🥠 You will tell all of your friends and colleagues how cool Streamlit is",
    #     "🥠 You will create a very popular Streamlit app",
    # ]
    # block_methods = [st.error, st.warning, st.info, st.success]
    st.success(
        "☘️ The algorithm recommends this app to you: [Traingenerator](https://traingenerator.jrieke.com/)"
    )

    st.info(
        "💡 With `st.form`, this app (and our complex algorithm!) only reruns when you hit the submit button, not at each widget interaction. [Check out the blog post to learn how it works!]()"
    )

"# Other new features"
"Check out these new features in streamlit v0.81: "
with st.beta_expander("Small text with st.caption"):
    "Lorem ipsum"
with st.beta_expander("Deploy button"):
    "Lorem ipsum"
with st.beta_expander("Theming improvements"):
    "Lorem ipsum"

with st.sidebar:
    "## Release Notes"
    "for streamlit v0.81"
    st.radio("", ["st.form", "st.caption", "Deploy button", "Theming improvements"])