#!/usr/bin/env python
# coding: utf-8

import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyPDFLoader

# Load environment variables
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def load_pdf(pdf_path):
    """
    Load and process a PDF document
    Args:
        pdf_path (str): Path to the PDF file
    Returns:
        list: List of Document objects containing page content and metadata
    """
    try:
        # Check if file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at path: {pdf_path}")
            
        # Get absolute path
        abs_path = os.path.abspath(pdf_path)
        
        loader = PyPDFLoader(abs_path)
        pages = loader.load()
        return pages
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return None
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

if __name__ == "__main__":
    # Use a relative path from the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "..", "sources", "sfbu-2024-2025-university-catalog-8-20-2024.pdf")
    
    pages = load_pdf(pdf_path)
    if pages:
        print(f"Successfully loaded {len(pages)} pages")
        # Print page 8 sample with larger content slice
        print("\nPage 8 content sample:")
        print("=" * 50)
        print(pages[7].page_content[:1000])  # Using index 7 for page 8 (0-based indexing)
        print("=" * 50)