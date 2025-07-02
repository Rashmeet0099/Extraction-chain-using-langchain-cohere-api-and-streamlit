import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
import streamlit as st  # Optional: for UI

# Load API key
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

# Set up the model
llm = ChatCohere(cohere_api_key=cohere_api_key, model="command-r-plus", temperature=0)

# Load the dynamic extraction prompt
with open("prompts/dynamic_extraction_prompt.txt", "r") as f:
    dynamic_prompt_template = f.read()

# OPTIONAL: Streamlit UI
st.title("🔍 Intelligent Text Extractor")
input_text = st.text_area("Paste any unstructured text below:", height=300)

if st.button("Extract"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        # Apply prompt template dynamically
        prompt = PromptTemplate.from_template(dynamic_prompt_template)
        final_prompt = prompt.invoke({"input_text": input_text})

        with st.spinner("Detecting text type and extracting information..."):
            response = llm.invoke(final_prompt)

        st.success("✅ Extraction complete!")
        st.subheader("📋 Extracted Information")
        st.code(response.content, language="json")
