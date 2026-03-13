import os, json # os skal hjelpe med filpath, ettersom det var litt trøbbel med det når man går fra å kjøre main-py til å runne den som modul

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
file_path = os.path.join(BASE_DIR, "health_records.json")

#file_path = "../health_records.json"

# Litt uklart om json skal pushes eller ikke, men jeg tar den med uansett så du har en populert fil
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