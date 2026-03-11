import json

file_path = "src/health_records.json"


def saveObject(health_object):
    try:
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(health_object)

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)

        print(f"Data successfully saved to {file_path}")

    except IOError as e:
        print(f"Error saving file: {e}")

def jsonObject():
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
            data = []
            print("Error fetching data from JSON file")
    return data