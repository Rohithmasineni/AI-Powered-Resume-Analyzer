# AI-Powered-Resume-Analyzer

## 🤖 AI-Powered Resume Analyzer & CSV Generator (LangChain + Streamlit)

This project implements an intelligent resume-processing system that automatically extracts structured candidate information from multiple resumes and converts it into a downloadable CSV file — making candidate screening faster, consistent, and more efficient.

Instead of manually reviewing resumes one-by-one, this system automates the workflow using:

- LangChain structured output parsing

- Pydantic schema validation

- LLM-powered information extraction

- Streamlit-based interactive UI

The goal of this project was learning-oriented: to understand how real-world resume-analysis pipelines and LLM-based data extraction systems are designed — including schema enforcement, batch processing, and structured output generation.

This project helped me understand the complete workflow — from ZIP-based resume ingestion to LLM extraction, validation, CSV aggregation, and user-friendly report download.

## Project Overview

Recruiters and HR teams often receive resumes in bulk — usually PDFs and DOCX files grouped inside ZIP folders.

Manually going through each resume to extract details such as:

- Name

- Email

- Skills

- Experience

- Education

is slow, repetitive, and prone to human error.

*This project automates that workflow:*

✔ Accepts a ZIP file containing multiple resumes

✔ Reads PDF & DOCX resumes automatically

✔ Extracts structured candidate information using LLMs

✔ Validates the output using Pydantic schema

✔ Converts the final dataset into a CSV file

✔ Allows the user to download the CSV directly

The focus was not just on automation — but on building a reliable structured extraction pipeline using LangChain.

### 🔄 End-to-End Workflow

**🗂 Resume Input**

User uploads a ZIP folder containing:

- multiple resumes

- mixed formats (PDF + DOCX)

- different layouts and templates

The system automatically scans and processes each resume.

### 📄 Resume Text Extraction

For each file:

- PDFs are parsed using pypdf

- DOCX files are parsed using python-docx

Once extracted, the raw text is passed to the LLM pipeline.

### 🧠 LLM-Based Information Extraction

LangChain is used to:

- send resume text to the LLM

- extract relevant attributes only

- return clean structured output

The extraction is guided through:

✔ Prompt templates

✔ Role-based instruction formatting

✔ Field-specific guidance

The output is validated using a Pydantic schema, ensuring:

- correct data types

- mandatory fields are handled safely

- lists stay as lists

- invalid responses are rejected

This helped me understand how structured LLM output improves consistency over free-text responses.

### 🧾 CSV Aggregation & Export

All parsed resumes are:

- combined into a single dataset

- converted into a Pandas DataFrame

- exported into a downloadable CSV report

The CSV file can be used for:

- candidate filtering

- recruitment analytics

- ATS processing

- talent dataset building

### 🧠 System Logic & Architecture

The project follows:

Resume ZIP Upload → Resume Parsing → LLM Extraction → Schema Validation → CSV Export → Download

Key components include:

- Pydantic-validated Resume Schema

- LangChain LLM + Output Parser Pipeline

- Batch resume processing

- Streamlit-based UI workflow

This project helped me better understand:

✔ structured information extraction using LLMs

✔ schema-driven output enforcement

✔ batch document automation workflows

✔ user-friendly data processing design

### 🧰 Tech Stack

- Python

- Streamlit

- LangChain

- Google Gemini Model

- Pydantic

- Pandas

- PyPDF

- python-docx

- dotenv for API key management

### ✅ Outcomes & Learnings

*Through this project, I was able to:*

✔ Build an end-to-end LLM-powered document processing system

✔ Work with structured output parsing using Pydantic

✔ Automate bulk resume extraction workflows

✔ Understand schema-validated LLM pipelines

✔ Design a practical, recruiter-friendly tool

This project lays a strong foundation for future enhancements such as:

- candidate ranking

- ATS score generation

- skills matching engine

- role-based resume filtering

### 📬 Contact

If you’d like to explore the project, suggest improvements, or collaborate — feel free to connect 😊

📧 Email — rohithmasineni223@email.com

🔗 LinkedIn — [Your LinkedIn Text](https://www.linkedin.com/in/your-profile/)

⭐ If you find this project useful, consider starring the repository!
