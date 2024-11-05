# Document Loader Project

This project provides modular document loaders for different types of content (PDF, YouTube, and URLs) using LangChain. It supports both direct input and source file-based loading.

## Features

- PDF document loading and parsing with metadata extraction
- YouTube video content extraction with OpenAI Whisper transcription and automatic cleanup
- Web page content loading with search functionality and content cleaning
- Source file-based URL loading for all loaders
- Clean content formatting and display

## Prerequisites

- Python 3.8+
- ffmpeg (required for YouTube audio processing)
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt-get install ffmpeg`
  - Windows: Download from https://ffmpeg.org/download.html
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd document-loader-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the project root and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### PDF Loading
```python
from loaders import load_pdf

# Direct path loading
pdf_path = "path/to/your/document.pdf"
pages = load_pdf(pdf_path)
if pages:
    print(f"Loaded {len(pages)} pages")
    print(pages[0].page_content)  # Access content of first page
```

### YouTube Video Processing
```python
from loaders import load_youtube

# Direct URL loading
url = "https://www.youtube.com/watch?v=your_video_id"
docs = load_youtube(url)

# Or load from source file
docs = load_youtube(source_file="youtube-mba-spotlight.txt")

if docs:
    print(docs[0].page_content)  # Access transcribed content
```

### Web Page Content Loading
```python
from loaders import load_url

# Direct URL loading
url = "https://example.com"
docs = load_url(url)

# Or load from source file
docs = load_url(source_file="sfbu-health-insurance-url.txt")

if docs:
    content = docs[0].page_content
    # Search within content
    search_term = "specific topic"
    for line in content.split('\n'):
        if search_term in line.lower():
            print(line.strip())
```

## Project Structure
```
project/
├── loaders/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── youtube_loader.py
│   ├── url_loader.py
│   └── source_loader.py
├── sources/
│   ├── youtube-mba-spotlight.txt
│   └── sfbu-health-insurance-url.txt
├── docs/
│   └── youtube/     # Temporary files directory
├── requirements.txt
└── .env
```

## Dependencies

Core packages:
- langchain==0.1.12: Core functionality for document loading
- langchain-community==0.0.27: Additional loaders and utilities
- openai==1.14.0: For YouTube video transcription
- python-dotenv==1.0.1: Environment variable management

Media processing:
- pypdf==4.1.0: PDF processing
- yt-dlp==2024.3.10: YouTube video downloading
- pydub==0.25.1: Audio processing

## Important Notes

1. **Setup Requirements**
   - Install ffmpeg before using YouTube functionality
   - Configure OpenAI API key in .env file

2. **File Management**
   - Place source files in the sources/ directory
   - YouTube temporary files are automatically cleaned up
   - Each loader supports both direct input and source files

3. **Usage Tips**
   - Start with PDF loader for simpler testing
   - Test YouTube loader with short videos first
   - Check source files exist before loading