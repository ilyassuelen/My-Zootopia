import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML card list item."""
    name = animal_obj.get("name")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")

    output = '<li class="cards__item">\n'

    # Card title for name
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    # Card text for details
    output += '  <p class="card__text">\n'
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'
    if type_:
        output += f'    <strong>Type:</strong> {type_}<br/>\n'
    output += '  </p>\n'

    # End card list item
    output += '</li>\n'

    return output


def main():
    # Load JSON data
    animals_data = load_data("animals_data.json")

    # Generate HTML output
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    # Read template
    with open("animals_template.html", "r", encoding="utf-8") as fileobj:
        template = fileobj.read()

    # Replace placeholder
    html_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write final HTML File
    with open("animals.html", "w", encoding="utf-8") as fileobj:
        fileobj.write(html_output)

    print("Created 'animals.html' with HTML serialization!")


if __name__ == "__main__":
    main()