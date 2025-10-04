import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


# Load JSON-Data
animals_data = load_data('animals_data.json')


# Generate output string
output = ""

for animal in animals_data:
    name = animal.get("name")
    locations = animal.get("locations", [])
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Diet: {diet}\n"
    if locations:
        output += f"Location: {locations[0]}\n"
    if type_:
        output += f"Type: {type_}\n"

    output += "\n"

# Read Template
with open("animals_template.html", "r", encoding="utf-8") as fileobj:
    template = fileobj.read()

# Replace Placeholder
html_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new File
with open("animals.html", "w", encoding="utf-8") as fileobj:
    fileobj.write(html_output)

print("Created 'animals.html'!")