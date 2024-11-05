#!/usr/bin/env python
# coding: utf-8

import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import WebBaseLoader
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from loaders.source_loader import read_source_url

# Load environment variables
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def clean_content(text):
    """
    Clean and format the content by removing excessive whitespace and empty lines
    """
    lines = text.split('\n')
    # Remove empty lines and strip whitespace
    lines = [line.strip() for line in lines if line.strip()]
    return '\n'.join(lines)

def load_url(url=None, source_file=None):
    """
    Load and process content from a URL
    Args:
        url (str, optional): Direct URL to load
        source_file (str, optional): Name of source file containing URL
    Returns:
        list: List of Document objects containing web page content
    """
    try:
        if source_file:
            url = read_source_url(source_file)
            if not url:
                return None
                
        if not url:
            raise ValueError("No URL provided")
            
        loader = WebBaseLoader(url)
        docs = loader.load()
        return docs
    except Exception as e:
        print(f"Error loading URL: {e}")
        return None

if __name__ == "__main__":
    # Example using source file
    docs = load_url(source_file="sfbu-health-insurance-url.txt")
    if docs:
        print("Successfully loaded URL content")
        content = docs[0].page_content
        print("\nContent sample:")
        print("=" * 50)
        print(clean_content(content[:1000]))
        print("=" * 50)