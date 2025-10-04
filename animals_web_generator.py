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
    # append information to each string
    name = animal.get("name")
    locations = animal.get("locations", [])
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")

    # Begin <li>
    output += '<li class="cards__item">\n'

    if name:
        output += f"Name: {name}<br/>\n"
    if diet:
        output += f"Diet: {diet}<br/>\n"
    if locations:
        output += f"Location: {locations[0]}<br/>\n"
    if type_:
        output += f"Type: {type_}<br/>\n"

    # End </li>
    output += '</li>\n'


# Read Template
with open("animals_template.html", "r", encoding="utf-8") as fileobj:
    template = fileobj.read()

# Replace Placeholder
html_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new File
with open("animals.html", "w", encoding="utf-8") as fileobj:
    fileobj.write(html_output)

print("Created 'animals.html' with HTML serialization!")