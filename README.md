# Extraction-chain-using-langchain-cohere-api-and-streamlit

# 🔍 Intelligent Information Extractor

A Python project that automatically detects the type of unstructured text (e.g., news articles, resumes, reports) and extracts structured information using [LangChain](https://www.langchain.com/), [Cohere](https://cohere.com/) LLMs, and a dynamic prompt template.

Built with:
- 🧠 LangChain
- 🗣️ Cohere LLM (`command-r-plus`)
- 🌐 Streamlit for UI
- 🔐 Python + .env for API keys

---

## 📌 Features

- ✅ Automatically detects input type (news, resume, email, report, etc.)
- ✅ Dynamically generates relevant fields for extraction
- ✅ Outputs structured JSON
- ✅ Clean and interactive web UI with Streamlit
- ✅ Supports both text input and file upload (.txt)

---

## 📁 Project Structure

extraction_project/
├── .env # Your Cohere API key
├── app.py # Streamlit UI version
├── main.py # Command-line version (optional)
├── requirements.txt # All dependencies
├── prompts/
│ └── dynamic_extraction_prompt.txt # Smart prompt template
└── data/
└── input_text.txt # Sample input text file

yaml
Copy
Edit

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/intelligent-extractor.git
cd intelligent-extractor
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add your Cohere API Key
Create a .env file in the root directory:

ini
Copy
Edit
COHERE_API_KEY=your_cohere_api_key_here
4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
🧠 How It Works
The core of this app is a dynamic prompt template that:

Analyzes the type of unstructured input (resume, news, email, etc.)

Automatically extracts relevant information in a structured JSON format

Uses Cohere's powerful command-r-plus model for fast and accurate output

📊 Sample Outputs
Input (News Text)
nginx
Copy
Edit
Operation Sindoor was launched after the April 22 terrorist attack in Pahalgam...
Output
json
Copy
Edit
{
  "type": "News Article",
  "main_subjects": ["Operation Sindoor", "Indian Armed Forces", "Pakistan"],
  "dates": ["April 22", "May 7", "May 10"],
  "locations": ["Pahalgam", "Jammu and Kashmir"],
  "summary": "India launched Operation Sindoor to retaliate against a terrorist attack..."
}
🛠️ Technologies Used
Python 3.11+

LangChain

Cohere LLM API

Streamlit

python-dotenv

📌 To-Do / Future Work
 PDF input and parsing

 CSV/JSON export

 Vector database storage

 User authentication

🙋‍♂️ Author
Rashmeet Singh
🚀 B.Tech CSE | AI-ML Enthusiast | LangChain Developer
📫 rashmeet@example.com

🛡️ License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml
Copy
Edit

---

Let me know if you'd like:
- A live demo badge (`Open in Streamlit Cloud`)
- A deploy-to-Render or deploy-to-HuggingFace button
- A separate `LICENSE` or `.gitignore` file

I can also create a `README.md` with screenshots or GIFs of the UI if you'd like to impress recruiters or 
