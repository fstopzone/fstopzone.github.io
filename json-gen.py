import os
import json

# Base image path relative to this script
base_folder = os.path.join('images', 'big-images')

# Folders to process
categories = ['action', 'nature', 'street', 'architecture', 'portraits']

# File extensions to include
valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')

for category in categories:
    folder_path = os.path.join(base_folder, category)
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        continue

    image_files = [
        os.path.join(folder_path, f).replace("\\", "/")
        for f in os.listdir(folder_path)
        if f.lower().endswith(valid_extensions)
    ]

    # Output file name: <category>-images.json
    json_filename = f"{category}-images.json"
    with open(json_filename, 'w') as json_file:
        json.dump(image_files, json_file, indent=2)

    print(f"✅ {json_filename} generated with {len(image_files)} image(s).")
