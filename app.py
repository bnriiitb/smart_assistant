import streamlit as st
import PyPDF2
from docx import Document
from gpt import *
# Function to count words in a text
def count_words(text):
    words = text.split()
    return len(words)

# Function to read a PDF file and return its text content
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()
    return text

# Function to read a DOCX file and return its text content
def read_docx(file):
    doc = Document(file)
    paragraphs = [p.text for p in doc.paragraphs]
    return "\n".join(paragraphs)

# Streamlit app
def main():
    st.title("TVS Smart Assistant")

    # File upload section
    # st.subheader("Upload a File")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "docx", "pdf"])

    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]

        # Show file upload progress
        with st.spinner("Uploading file..."):
            if file_type == "txt":
                file_contents = uploaded_file.read().decode("utf-8")
            elif file_type == "docx":
                file_contents = read_docx(uploaded_file)
            elif file_type == "pdf":
                file_contents = read_pdf(uploaded_file)

        st.success("The file has been successfully uploaded")
        word_count = count_words(file_contents)
        st.write(f"Number of words in the file: {word_count}")

    # User question section
    st.subheader("User Question")
    user_question = st.text_area("Ask me a question",height=100)

    if st.button("Submit"):
        # Show progress bar
        progress_bar = st.progress(0)
        progress_text = st.empty()

        # Perform some processing (e.g., API call, computation, etc.)
        for i in range(100):
            # Simulating a delay
            question_answer('', uploaded_file.name, user_question)

            # Update progress bar and text
            progress_bar.progress(i + 1)
            progress_text.text(f"Progress: {i + 1}%")

        # Display the result or answer to the user
        st.success("Here is the answer to your question.")

if __name__ == "__main__":
    main()