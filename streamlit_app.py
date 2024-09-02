import streamlit as st
from semantic_search import getMostRelevantCourses
from streamlit_pills import pills
from prompt_llm import ask_gemma2b
from syllabi import syllabi
import time

st.title("Western U - Course Recommender")
# st.write(
#     "This app uses RAG to tune LLM responses to consider western course syllabi"
# )

selected = pills("Eg.", ["Machine Learning Engineer", "Database Adminstrator", "Distributed Systems Engineer", "Game Developer", "Network Engineer", "Data Analyst"], ["🤖", "💾", "💽", "🎮", "🌐","📊"],clearable=True,index=None)

job = st.text_input('My dream job is:', selected)

submitted = st.button("Submit")
st.divider()

string_list = [(key + " - " + value[0]) for key, value in syllabi.items() if value]

if submitted and job:
    st.header('Most Relevant Courses')
    relevantCourses = ''
    # with st.spinner('loading...'):
    #     time.sleep(5)
    try:
        relevantCourses = getMostRelevantCourses(job)
        st.write(relevantCourses)
    except Exception as err:
        print(err)


    col1, col2 = st.columns(2)
    with col1:
        st.header("With RAG")
        rag_output = ''
        try:
            with st.spinner('generating...'):
                
                rag_output = ask_gemma2b(f'''Here are a list of computer science courses at Western University: {string_list}. 
                                Create a 4 year university schedule using only courses from that list. Split each year into 2 semesters.
                                Seperate the schedule by year. You must only have up to 10 courses per year. 
                                Pick courses for becoming a {job}. You must include these relevant courses: {relevantCourses}''')
        except Exception as err:
            st.write(err)   
        st.write(rag_output)

    with col2:
        st.header("Without RAG")
        no_rag_output = ''
        try:
            with st.spinner('generating...'):
                no_rag_output = ask_gemma2b(f'generate a university course schedule to become a {job}')
        except Exception as err:
            st.write(err)  
        st.write(no_rag_output)
