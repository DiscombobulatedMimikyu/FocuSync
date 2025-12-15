import json
import os

# Retrieve JSON data
def get_data(file_name='tasks'):
    # ile path 
    file_path = fr'C:\Users\gary\OneDrive\Desktop\FocuSync\data\{file_name}.json'

    # Check if the file exists
    if os.path.exists(file_path):
        try:
            # Open the file in read mode
            with open(file_path, 'r') as f:
                # Load the JSON data from the file
                file_data = json.load(f)
                # Return the loaded data
                return file_data
        except:
            # Return None if the file is empty or invalid JSON
            return None
    else:
        # Return error message if file doesn't exist
        return "file not found"


# Get a list of values for a specific key
def key_data(key='title'):
    # Retrieve the JSON data
    json_data = get_data()

    # Empty list to store key values
    key_list = []

    # If data exists
    if json_data:
        # Collect the value of the specified key
        for items in json_data:
            key_list.append(items.get(key))

        # Return values
        return key_list
    else:
        # Return None if JSON data is empty
        return None