import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import call_ollama

def extract_info(text):
    """Extract structured information using zero-shot prompting."""
    prompt = f"""Extract the person's name, age, and occupation from this text.
Return as JSON.

Text: {text}

JSON:"""
    
    response = call_ollama(
        prompt, 
        temperature=0.1, 
        num_predict=150
    )
    return response

# Test
text = """My name is Alice Johnson, I'm 28 years old, and I work as a software engineer.
    My name is Bob Smith, I'm 35 years old, and I work as a teacher.
    My name is Dr. Carol Williams, I'm 42 years old, and I work as a physician.
    My name is Dave, I'm 29 years old, and I work in marketing.
"""
result = extract_info(text)
print("\n\nInformation Extraction\n" + "="*50)
print(f"Input: {text}")
print(f"Output: {result}")