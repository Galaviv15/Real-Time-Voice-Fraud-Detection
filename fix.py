import json

# Replace with your actual filename
filename = 'Chinese_fraud_detection.ipynb' 

try:
    with open(filename, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Remove hidden Unicode markers that can break JSON parsing
    bad_chars = ["\ufeff", "\u200e", "\u200f"]
    for ch in bad_chars:
        raw = raw.replace(ch, "")

    data = json.loads(raw)

    # Ensure metadata and widgets keys exist
    if 'metadata' not in data:
        data['metadata'] = {}
    
    if 'widgets' not in data['metadata']:
        data['metadata']['widgets'] = {}

    # Inject the 'state' key required by GitHub/nbviewer
    data['metadata']['widgets']['state'] = {}
    
    # Save the fixed notebook with proper indentation
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)

    print(f"Success: '{filename}' has been repaired and saved.")

except json.JSONDecodeError as e:
    print(f"Error: The file is not a valid JSON. You might need to rollback. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")