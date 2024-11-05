#!/usr/bin/env python
# coding: utf-8

import os

def get_source_path(filename):
    """
    Get the absolute path to a file in the sources directory
    Args:
        filename (str): Name of the source file
    Returns:
        str: Absolute path to the source file
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "..", "sources", filename)

def read_source_url(filename):
    """
    Read URL from a source file
    Args:
        filename (str): Name of the source file
    Returns:
        str: URL content from the file
    """
    try:
        source_path = get_source_path(filename)
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file not found: {filename}")
            
        with open(source_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading source file: {e}")
        return None