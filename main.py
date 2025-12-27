import os 
import zipfile 
from io import BytesIO 
from typing import List, Optional 
from typing import Annotated

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from pypdf import PdfReader
from docx import Document 

from pydantic import BaseModel, Field, EmailStr 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

# API Key Loading
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# if not GOOGLE_API_KEY:
#     st.error

# Resume output schema:
class ResumeSchema(BaseModel):
    name: Optional[str] = Field(default = '', description = 'Full name of candidate')
    email: Optional[EmailStr] = Field(default = None)
    phone: Optional[str] = Field(default = '')
    summary: Optional[str] = Field(default = '')
    
    experience: float = Field(description="Total years of work experience as a number")
    skills: List[str] = Field(description="A list of top technical and soft skills", default_factory = list)
    education: str = Field(description="Highest degree and university name")
    links: Annotated[list[str], 'if any links found in the text return me the links as list of string']
    
    source_file: Optional[str] = None
    
parser = PydanticOutputParser(pydantic_object = ResumeSchema) # it tells LLM, Whatever you generate must match this Pydantic Model
format_instructions = parser.get_format_instructions()

    
# LLM Model
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

# Prompt
prompt = PromptTemplate(
    template = """
    You are an expert ATS resume analyzer.

    Extract structured candidate information from the resume text.

    The output MUST strictly follow this format:
    {format_instructions}
    
    Resume:
    --------
    {resume_text}
    --------
    """,
        input_variables = ['resume_text'],
        partial_variables = {'format_instructions':format_instructions}
)


def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ''
    for page in reader.pages:
        text = text + page.extract_text() + '\n'
    return text 

def extract_text_from_docx(path):
    doc = Document(path)
    return '\n'.join(p.text for p in doc.paragraphs)

def analyze_resume(text: str):
    chain = prompt | model | parser
    return chain.invoke({'resume_text':text})


# Streamlit UI
st.title('AI-Powered Resume Analyzer')
st.write('Upload a ZIP file containing resumes (PDF / DOCX).')

uploaded_zip = st.file_uploader('Upload ZIP', type = ['zip'])

if uploaded_zip:
    
    results = []
    zip_bytes = BytesIO(uploaded_zip.read())
    
    with zipfile.ZipFile(zip_bytes, 'r') as zip_ref:
        
        for file_name in zip_ref.namelist():
            
            if not (file_name.endswith('.pdf') or file_name.endswith('.docx')):
                continue
            
            st.write(f'Processing: {file_name}')
            
            extracted_path = zip_ref.extract(file_name, "temp_resumes")
            
            if file_name.endswith('.pdf'):
                text = extract_text_from_pdf(extracted_path)
                
            elif file_name.endswith('.docx'):
                text = extract_text_from_docx(extracted_path)
                
            else:
                continue
            
            try:
                parsed = analyze_resume(text)
                parsed.source_file = file_name
                results.append(parsed.model_dump())
                
            except Exception as e:
                st.error(f'❌ Parsing failed for {file_name}: {e}')
                
    if results:
        
        df = pd.DataFrame(results)
        
        st.success('Extraction completed successfully ✅')
        st.dataframe(df)

        csv_path = 'resume_analysis.csv'
        df.to_csv(csv_path, index = False)
        
        with open(csv_path, 'rb') as f:
            st.download_button(
                'Download CSV', 
                f,
                file_name = 'resume_analysis.csv',
                mime = 'text/csv'
            )    
            
    else:
         st.warning("No valid resumes parsed.")
         
