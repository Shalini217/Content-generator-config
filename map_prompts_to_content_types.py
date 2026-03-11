import json
import re

# Read both files
prompts_file = r"C:\Users\DELL\Downloads\Prompts.json"
content_types_file = r"C:\Users\DELL\Downloads\Content Types.xlsx"

# Read and clean Prompts.json
with open(prompts_file, 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'ObjectId\("([^"]+)"\)', r'"\1"', content)
prompts_data = json.loads(content)

# Extract prompt mappings by productFieldName
prompt_mappings = {}

for config in prompts_data.get('generationConfigs', []):
    response_fields = config.get('responseFields', [])
    for field in response_fields:
        product_field_name = field.get('productFieldName')
        if product_field_name:
            system_prompt = config.get('systemPromptSimple', {})
            prompt_mappings[product_field_name] = {
                "prompt": system_prompt.get('prompt', ''),
                "attributesToUsePrefix": system_prompt.get('attributesToUsePrefix', ''),
                "suffix": system_prompt.get('suffix', '')
            }

print("PROMPT MAPPINGS BY PRODUCT FIELD NAME:")
print("="*60)
for field_name, prompts in prompt_mappings.items():
    print(f"\n{field_name}:")
    print(f"  Has prompt: {len(prompts['prompt'])} chars")
    print(f"  Has prefix: {len(prompts['attributesToUsePrefix'])} chars")
    print(f"  Has suffix: {len(prompts['suffix'])} chars")

print("\n" + "="*60)
print("JAVASCRIPT FORMAT FOR HTML:")
print("="*60)

output = "const PROMPTS_BY_PRODUCT_FIELD = " + json.dumps(prompt_mappings, indent=4, ensure_ascii=False) + ";"

# Save to file
output_file = r"C:\Users\DELL\prompts_by_product_field.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\nSaved to: {output_file}")
print("\nYou can now embed this in your HTML file!")

# Also create a summary
print("\n" + "="*60)
print("SUMMARY:")
print("="*60)
print(f"Total product fields with prompts: {len(prompt_mappings)}")
print("\nProduct fields found:")
for field_name in prompt_mappings.keys():
    print(f"  - {field_name}")
