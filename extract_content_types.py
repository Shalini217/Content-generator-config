import pandas as pd
import json

# Read the Excel file
excel_file = r"C:\Users\DELL\Downloads\Content Types.xlsx"

try:
    # Read the Excel file
    df = pd.read_excel(excel_file)

    print("Excel file columns:", df.columns.tolist())
    print("\nFirst few rows:")
    print(df.head())

    # Extract content types and product field names
    content_types_data = {}

    for index, row in df.iterrows():
        # Try different possible column names for Content Type
        content_type = None
        if 'Content Type' in df.columns:
            content_type = row['Content Type']
        elif 'contentType' in df.columns:
            content_type = row['contentType']
        elif 'content_type' in df.columns:
            content_type = row['content_type']

        # Try different possible column names for Product Field Name
        product_field = None
        if 'Product Field Name' in df.columns:
            product_field = row['Product Field Name']
        elif 'productFieldName' in df.columns:
            product_field = row['productFieldName']
        elif 'product_field_name' in df.columns:
            product_field = row['product_field_name']

        # Add to dictionary if both values exist
        if pd.notna(content_type) and pd.notna(product_field):
            content_types_data[str(content_type)] = {
                "productFieldName": str(product_field)
            }

    print("\n" + "="*60)
    print("EXTRACTED DATA:")
    print("="*60)
    print(json.dumps(content_types_data, indent=4))

    print("\n" + "="*60)
    print("JAVASCRIPT FORMAT (Copy this into HTML):")
    print("="*60)
    print("const CONTENT_TYPES_DATA = {")
    for idx, (ct_name, ct_data) in enumerate(content_types_data.items()):
        comma = "," if idx < len(content_types_data) - 1 else ""
        print(f'    "{ct_name}": {{')
        print(f'        "productFieldName": "{ct_data["productFieldName"]}"')
        print(f'    }}{comma}')
    print("};")

    print("\n" + "="*60)
    print(f"Total content types found: {len(content_types_data)}")
    print("="*60)

except FileNotFoundError:
    print(f"Error: File not found at {excel_file}")
    print("Please make sure 'Content Types.xlsx' exists in your Downloads folder")
except Exception as e:
    print(f"Error reading Excel file: {e}")
    print("\nMake sure you have pandas and openpyxl installed:")
    print("  pip install pandas openpyxl")
