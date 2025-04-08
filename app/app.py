import streamlit as st
from utils.seo_tools import generate_keywords, run_audit
from utils.blog_tools import generate_blog
from utils.video_tools import generate_video_script

st.set_page_config(page_title="RankMind AI", layout="wide")

st.title("🚀 RankMind — Your AI-Powered SEO Agent")

tab1, tab2, tab3, tab4 = st.tabs(["SEO Audit", "Keyword Generator", "Blog Generator", "Video Script"])

with tab1:
    st.header("SEO Site Audit")
    url = st.text_input("Enter a website URL")
    if st.button("Run Audit"):
        result = run_audit(url)
        st.markdown(result)

with tab2:
    st.header("Generate Keywords")
    topic = st.text_input("Enter topic for keyword ideas")
    if st.button("Generate Keywords"):
        keywords = generate_keywords(topic)
        st.markdown("\n".join(keywords))

with tab3:
    st.header("AI Blog Generator")
    topic = st.text_input("Enter blog topic")
    if st.button("Generate Blog"):
        blog = generate_blog(topic)
        st.markdown(blog)

with tab4:
    st.header("Video Script Assistant")
    video_topic = st.text_input("Enter video topic")
    if st.button("Generate Script"):
        script = generate_video_script(video_topic)
        st.text_area("Script:", script, height=300)
