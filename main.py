from difflib import SequenceMatcher
import re

def preprocess_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

def calculate_similarity(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = preprocess_text(f1.read())
        data2 = preprocess_text(f2.read())

    if not data1 or not data2:
        return "One or both files are empty. Cannot calculate similarity."

    similarity = SequenceMatcher(None, data1, data2).ratio()
    return f"The plagiarized content is {similarity * 100:.2f}%"


file1 = input("Enter the path of the first file: ")
file2 = input("Enter the path of the second file: ")
print(calculate_similarity(file1, file2))
