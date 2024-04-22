import openai, os, requests

openai.api_type = # apo type
openai.api_version = #api_version
# Azure OpenAI setup
openai.api_base = # Add your endpoint here
openai.api_key = # Add your OpenAI API key here
deployment_id = # Add your deployment ID here

import PyPDF2
## Upload pdf
# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2. PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Function to ask a question using Azure OpenAI's API
def ask_question_about_text(text, question):
    # Define the prompt
    prompt = [{"role": "user", "content": f"Question: {question}\nContext: {text}\nAnswer:"}]

    # Set parameters for the completion
    params = {
        "temperature": 0.5,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": ["\n"]
    }

    completion = openai.ChatCompletion.create(
    messages=prompt,
    deployment_id="gpt-4",
    )

    # Extract and return the answer
    answer = completion.choices[0].message["content"]
    return answer

# Path to your PDF file
pdf_path = "../data/Cumulative-sample-report-with-notes-2017_2.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)
#print(pdf_text)
# Ask a question about the text
question = "Highlight abnormal lab result in bullet points"

answer = ask_question_about_text(pdf_text, question)

print("Answer:", answer)