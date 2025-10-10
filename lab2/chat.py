import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import chat_ollama

def run_conversation():
    """Demonstrate multi-turn conversation."""
    
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant that helps with electronics questions.'
        },
        {
            'role': 'user',
            'content': 'How do I spec resistors for leds based on forward voltage and current?'
        }
        # {
        #     'role': 'user',
        #     'content': 'Can you show me an example?'
        # },
        # {
        #     'role': 'user',
        #     'content': 'What if I have a 5V supply with a 2V forward voltage and 20mA current?'
        # },
        # {
        #     'role': 'user',
        #     'content': 'What if I have a 12V supply with a 3.6V forward voltage and 30mA current?'
        # }
    ]
    print("User:", messages[1]['content'])
    
    # First response
    response = chat_ollama(messages, temperature=0.3)
    print("Assistant:", response)
    
    # Add to conversation
    messages.append({
        'role': 'assistant',
        'content': response
    })
    
    messages.append({
        'role': 'user',
        'content': 'Can you summarize your response in two sentences for me?'
    })
    
    print("\nUser:", messages[-1]['content'])
    
    # Second response
    response = chat_ollama(messages, temperature=0.3)
    print("\nAssistant:", response)

if __name__ == "__main__":
    run_conversation()