import streamlit as st
from semantic_search import getMostRelevantCourses


st.title("Western Course Recommender")
st.write(
    "This app uses RAG to tune LLM responses to consider western course syllabi"
)
job = st.text_input('My dream job is:')
submitted = st.button("Submit")
st.divider()

if submitted and job:
    st.header('Most Relevant Courses')
    st.write(getMostRelevantCourses(job))


    col1, col2 = st.columns(2)
    with col1:
        st.header("With RAG")
        st.write('world')

    with col2:
        st.header("Without RAG")
        st.write('hello')
