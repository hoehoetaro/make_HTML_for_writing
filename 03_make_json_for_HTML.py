import os
import json
from datetime import datetime

# Change the working directory to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Get the current folder name
current_folder_name = os.path.basename(os.getcwd())

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Specify the creator
creator = "hoehoe"

# Specify the source
source = "GPT4"

# Create log data
log_data = f"Creation Date: {current_date}\nCreator: {creator}\nSource: {source}\n"

# Write log data to a text file
with open(f'{current_folder_name}_log.txt', 'w', encoding='utf-8') as f:
    f.write(log_data)

# Create the data to output
data = {
    "title": {
        "type": "title",
        "name": current_folder_name,
        "thumbnail_source": f"{current_folder_name}_thumbnail.png"
    },
    "update_data": {
        "type": "text",
        "name": "更新記録",
        "file_path": f"{current_folder_name}_log.txt"
    },
    "contents": []
}

# Serialize to JSON format and write to a file
with open(f'{current_folder_name}_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
