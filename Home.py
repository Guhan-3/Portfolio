import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("GUHAN S M")
    content = """
    Driven and detail-oriented fresher with a solid foundation in software development and Python. 
    Passionate about problem-solving and continuously improving skills in Data Structures and Algorithms. 
    Eager to apply my skills to real-world projects and grow within a dynamic team.
    """
    st.info(content)

col3, empty, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[source_code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row["image"]}")
        st.write(f"[source_code]({row['url']})")
