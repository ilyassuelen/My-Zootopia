import requests


def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML card list item."""
    name = animal_obj.get("name")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    type_ = characteristics.get("type")
    lifespan = characteristics.get("lifespan")
    slogan = characteristics.get("slogan")

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
    if lifespan:
        output += f'    <strong>Lifespan:</strong> {lifespan}<br/>\n'
    if slogan:
        output += f'    <strong>Slogan:</strong> {slogan}<br/>\n'
    output += '  </p>\n'

    # End card list item
    output += '</li>\n'

    return output


def main():
    # Prompt for animal name
    animal_name = input("Enter a name of an animal: ")

    # Load JSON data from API
    API_URL = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    API_KEY = "roKB7lb0UTVxsu4nUzxZeg==1igNpbrf1k2qAIQJ"

    response = requests.get(API_URL, headers={"X-Api-Key": API_KEY})

    if response.status_code == 200:
        animals_data = response.json()
    else:
        print("Error fetching data:", response.status_code, response.text)
        return

    # Check if animals_data is empty
    if not animals_data:
        html_output = f'<h2>The animal "{animal_name}" does not exist.</h2>'
    else:
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

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()