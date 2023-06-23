import streamlit as st


def main():
    st.set_page_config(
        page_title="My Webpage for talking with multiple databases",
        page_icon=":books:",
        layout="wide",
    )

    # ---Header Section ----

    with st.container():
        st.subheader("Hi, I am Paul :wave:")
        st.title("An AI Engineer from Ireland")
        st.write(
            "I am passionate about integrating AI with Society to be more efficient in business "
        )
        st.write("[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs here and click on 'Process'")
        st.button("Process")


if __name__ == "__main__":
    main()
