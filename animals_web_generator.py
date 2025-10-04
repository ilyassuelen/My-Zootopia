import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


# Load JSON-Data
animals_data = load_data('animals_data.json')


# Iterate over all animals
for animal in animals_data:
    name = animal.get("name")
    locations = animal.get("locations", [])
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if locations:
        print(f"Location: {locations[0]}")
    if type_:
        print(f"Type: {type_}")

    print()