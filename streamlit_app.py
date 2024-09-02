import streamlit as st
from semantic_search import getMostRelevantCourses
from streamlit_pills import pills
from prompt_llm import ask_gemma2b
from syllabi import syllabi
import time
import pandas as pd
import numpy as np

st.title("Western U - Course Recommender")
# st.write(
#     "This app uses RAG to tune LLM responses to consider western course syllabi"
# )

selected = pills("Eg.", ["Machine Learning Engineer", "Database Adminstrator", "Distributed Systems Engineer", "Game Developer", "Network Engineer", "Data Analyst"], ["🤖", "💾", "💽", "🎮", "🌐","📊"],clearable=True,index=None)

job = st.text_input('My dream job is:', selected)

submitted = st.button("Submit")

st.write('\n')

expander = st.expander("See all courses")

df = pd.DataFrame.from_dict(syllabi, orient='index').reset_index()
df.columns = ['Course Code', 'Course Name', 'Syllabus', 'Pre-requistes', 'Anti-requisites']
def process_string(s):
    if isinstance(s, str):
        # Cut out content before the first ':' and take a 50-character preview
        return s.split(':', 1)[-1][:50] + '...'
    return s

# Apply the function to the second column
df['Syllabus'] = df['Syllabus'].apply(process_string)

expander.dataframe(df)

st.divider()

string_list = [(key + " - " + value[0]) for key, value in syllabi.items() if value]

if submitted and job:
    st.subheader('Most Relevant Courses For You')
    st.write('Scanned course syllabi using Semantic Search:')
    relevantCourses = ''
    # with st.spinner('loading...'):
    #     time.sleep(5)
    try:
        relevantCoursesStr, courseCodes = getMostRelevantCourses(job)
        st.write(relevantCoursesStr)
    except Exception as err:
        print(err)
    
        

    st.divider()
    st.header("Degree Planning")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("With RAG")
        rag_output = ''
        try:
            with st.spinner('asking Google Gemma-2-2b-it...'):
                prompt = f'''Here is a list of 40 computer science courses at Western University: {string_list}. 
                                Create a 4 year university schedule using only courses from that list. Split each year into 2 semesters.
                                Seperate the schedule by year. You must only have up to 10 courses per year. 
                                Pick courses for becoming a {job}. You must include these relevant course codes in the schedule: {", ".join(courseCodes)}'''
                rag_output = ask_gemma2b(prompt)
                
                for course in courseCodes:
                    rag_output = rag_output.replace(course, f':green[{course}]')
        except Exception as err:
            st.write(err)   
        st.write(rag_output)

    with col2:
        st.subheader("Without RAG")
        no_rag_output = ''
        try:
            with st.spinner('asking Google Gemma-2-2b-it...'):
                prompt = f'Forget any previous conversation. Start with a new context. Do not use course codes: {string_list}. Generate a university course schedule to become a {job}'
                no_rag_output = ask_gemma2b(prompt)
        except Exception as err:
            st.write(err)  
        st.write(no_rag_output)
