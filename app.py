import streamlit as st
import os
from dotenv import load_dotenv

from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

# Set up the model
llm = ChatCohere(cohere_api_key=cohere_api_key, model="command-r-plus", temperature=0)

# Load extraction prompt
with open("prompts/extraction_prompt.txt", "r") as f:
    extraction_prompt = f.read()

# Streamlit UI
st.set_page_config(page_title="Information Extractor", layout="centered")
st.title("🔍 Extract Structured Info from Text")
st.markdown("Paste or upload unstructured text and get structured JSON output.")

# Input options
option = st.radio("Choose input method:", ("Text input", "Upload .txt file"))

input_text = ""

if option == "Text input":
    input_text = st.text_area("Paste your text here:", height=200)

elif option == "Upload .txt file":
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file:
        input_text = uploaded_file.read().decode("utf-8")

# Run extraction
if st.button("Extract Information"):
    if input_text.strip() == "":
        st.warning("Please provide input text.")
    else:
        # Format prompt
        prompt = PromptTemplate.from_template("{extraction_prompt}\n\nInput:\n{input_text}")
        final_prompt = prompt.invoke({
            "extraction_prompt": extraction_prompt,
            "input_text": input_text
        })

        # Get response from model
        with st.spinner("Extracting..."):
            response = llm.invoke(final_prompt)

        st.success("Extraction complete!")
        st.subheader("📋 Extracted Structured Info")
        st.code(response.content, language="json")
