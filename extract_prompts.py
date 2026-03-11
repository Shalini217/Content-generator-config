import json
import re

# Read the Prompts.json file
prompts_file = r"C:\Users\DELL\Downloads\Prompts.json"

try:
    with open(prompts_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean MongoDB-style JSON
    # Remove ObjectId() wrapper
    content = re.sub(r'ObjectId\("([^"]+)"\)', r'"\1"', content)

    prompts_data = json.loads(content)

    print("Reading Prompts.json file...")
    print("="*60)

    # Display structure
    print("\nFile structure:")
    print(f"Type: {type(prompts_data)}")

    if isinstance(prompts_data, dict):
        print(f"Keys: {list(prompts_data.keys())}")
    elif isinstance(prompts_data, list):
        print(f"Array length: {len(prompts_data)}")
        if len(prompts_data) > 0:
            print(f"First item keys: {list(prompts_data[0].keys()) if isinstance(prompts_data[0], dict) else 'Not a dict'}")

    print("\n" + "="*60)
    print("PROMPTS DATA:")
    print("="*60)
    print(json.dumps(prompts_data, indent=2))

    # Save as JavaScript constant for embedding
    output_file = r"C:\Users\DELL\prompts_data.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("const PROMPTS_DATA = ")
        f.write(json.dumps(prompts_data, indent=4))
        f.write(";\n")

    print("\n" + "="*60)
    print(f"Saved JavaScript format to: {output_file}")
    print("="*60)

except FileNotFoundError:
    print(f"Error: File not found at {prompts_file}")
    print("Please make sure 'Prompts.json' exists in your Downloads folder")
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON format - {e}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
