

# 🏦 Investment Banking GPT using Llama2-RAG 🦙

This repository contains the **Investment Banking GPT** project, developed by **Sonia Patel** as part of an AI programming course. The project leverages **Llama Index LLM** with **RAG (Retrieval Augmented Generation)** to allow users to upload multiple annual reports of companies in PDF format and ask questions, enabling comparative analysis and insights.

## 📜 Project Overview

The **Investment Banking GPT** project is designed to:
- Accept multiple PDF files 📁 (e.g., annual reports of various companies).
- Allow users to chat and ask questions to gain insights from these documents.
- Perform comparative analysis with competitors using advanced AI techniques.

## 🛠️ Key Features

- **Information Retrieval**: Utilizes keyword matching, semantic similarity, and machine learning to find relevant documents from large corpuses of text.
- **Text Generation**: Creates new content, answers questions, and generates factual, informative, and consistent text based on the uploaded data.
- **RAG (Retrieval Augmented Generation)**: Combines retrieval and text generation to overcome limitations of fine-tuning, making the model cost-efficient and always up to date.

## ⚙️ Tech Stack

- **Llama Index** for efficient information retrieval and text generation.
- **Streamlit** for the user interface and file uploads.
- **Hugging Face Transformers** for model fine-tuning.
- **Torch** for handling datatype attributes.
- **Langchain Community** for advanced embeddings and querying.

## 📂 Dataset

For the project, annual reports for 2022 of **JP Morgan Chase & Co.** and **Goldman Sachs** were used. However, the system can accept the annual report of any company, allowing flexible analysis across various reports.

## 🚀 How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/investment-banking-gpt.git
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Upload PDF files** 📄: The app will accept multiple PDF files of annual reports for processing and analysis.

5. **Ask Questions** 💬: Input your prompt in the text box and get insights from the reports using the Llama2-RAG model.

## 🔍 Why Use RAG?

- **No training required**, making it cost-effective.
- **Always up to date** with real-time data fetching.
- **Trustworthy** by showing retrieved documents as part of the response.

## 📈 Results

The model provides insights and comparative analysis between companies' annual reports using Llama2-RAG. It outputs:
- Responses to user queries based on the uploaded documents.
- Source text references for transparency and trustworthiness.
![Picture1](https://github.com/user-attachments/assets/4d543c0a-088d-4cad-bfec-9461a5d213cf)

![image](https://github.com/user-attachments/assets/3f86c4f4-9291-4069-b931-d47563195034)




## 🎓 Contribution

This project shows creativity and technical depth by combining various libraries and AI techniques to automate financial report analysis. It can be extended to various applications within **Investment Banking** and **Corporate Finance** sectors.

## 🤝 Contribution

Feel free to fork the repository and submit pull requests if you’d like to collaborate on improving the model or expanding its capabilities!

