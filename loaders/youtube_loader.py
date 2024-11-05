#!/usr/bin/env python
# coding: utf-8

import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from loaders.source_loader import read_source_url

# Load environment variables
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def load_youtube(url=None, source_file=None, save_dir="docs/youtube/"):
    """
    Load and process content from a YouTube video using OpenAI Whisper
    Args:
        url (str, optional): Direct YouTube URL to load
        source_file (str, optional): Name of source file containing YouTube URL
        save_dir (str): Directory to save temporary audio files
    Returns:
        list: List of Document objects containing transcribed content
    """
    try:
        if source_file:
            url = read_source_url(source_file)
            if not url:
                return None
                
        if not url:
            raise ValueError("No YouTube URL provided")
            
        # Create save directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)
        
        # Initialize the generic loader with YouTube audio loader and Whisper parser
        loader = GenericLoader(
            YoutubeAudioLoader([url], save_dir),
            OpenAIWhisperParser()
        )
        
        # Load and transcribe the content
        docs = loader.load()
        return docs
        
    except Exception as e:
        print(f"Error loading YouTube content: {e}")
        return None
    finally:
        # Cleanup temporary files
        try:
            if os.path.exists(save_dir):
                for file in os.listdir(save_dir):
                    file_path = os.path.join(save_dir, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
        except Exception as e:
            print(f"Warning: Could not clean up temporary files: {e}")

if __name__ == "__main__":
    # Example using source file
    docs = load_youtube(source_file="youtube-mba-spotlight.txt")
    if docs:
        print("Successfully loaded YouTube content")
        print("\nContent sample:")
        print("=" * 50)
        print(docs[0].page_content[:1000])
        print("=" * 50)