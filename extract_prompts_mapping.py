import json
import sys

# Read the Prompts.json file
with open(r'C:\Users\DELL\Downloads\Prompts.json', 'r', encoding='utf-8') as f:
    content = f.read()
    # Remove ObjectId wrapper
    content = content.replace('ObjectId("', '"').replace('")', '"')
    data = json.loads(content)

# Extract prompts mapping
prompts_mapping = {}

for config in data.get('generationConfigs', []):
    # Get productFieldName from responseFields
    response_fields = config.get('responseFields', [])
    if response_fields:
        product_field_name = response_fields[0].get('productFieldName', '')

        # Get systemPromptSimple
        system_prompt = config.get('systemPromptSimple', {})

        prompts_mapping[product_field_name] = {
            'prompt': system_prompt.get('prompt', ''),
            'attributesToUsePrefix': system_prompt.get('attributesToUsePrefix', ''),
            'suffix': system_prompt.get('suffix', '')
        }

# Output as JavaScript object
print('const PROMPTS_DATA = {')
for field_name, prompts in prompts_mapping.items():
    print(f'    "{field_name}": {{')
    print(f'        "prompt": {json.dumps(prompts["prompt"])},')
    print(f'        "attributesToUsePrefix": {json.dumps(prompts["attributesToUsePrefix"])},')
    print(f'        "suffix": {json.dumps(prompts["suffix"])}')
    print('    },')
print('};')
