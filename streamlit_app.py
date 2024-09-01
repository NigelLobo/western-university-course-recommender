import streamlit as st
from semantic_search import getMostRelevantCourses
from streamlit_pills import pills


st.title("Western Course Recommender")
# st.write(
#     "This app uses RAG to tune LLM responses to consider western course syllabi"
# )

selected = pills("Eg.", ["Machine Learning Engineer", "Database Adminstrator", "Distributed Systems Engineer", "Game Developer", "Network Engineer", "Data Analyst"], ["🤖", "💾", "💽", "🎮", "🌐","📊"],clearable=True,index=None)

job = st.text_input('My dream job is:', selected)

submitted = st.button("Submit")
st.divider()


if submitted and job:
    st.header('Most Relevant Courses')
    try:
        st.write(getMostRelevantCourses(job))
    except Exception as err:
        print(err)


    col1, col2 = st.columns(2)
    with col1:
        st.header("With RAG")
        st.write('world')

    with col2:
        st.header("Without RAG")
        st.write('hello')
