from data_fetcher import fetch_data

def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML card list item."""
    name = animal_obj.get("name", "Unknown")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    lifespan = characteristics.get("lifespan", "Unknown")
    slogan = characteristics.get("slogan", "")
    habitat = characteristics.get("habitat", "Unknown")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Type:</strong> {animal_type}<br/>\n'
    output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        output += f'    <strong>Location:</strong> {", ".join(locations)}<br/>\n'
    output += f'    <strong>Lifespan:</strong> {lifespan}<br/>\n'
    if slogan:
        output += f'    <em>"{slogan}"</em><br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


def main():
    animal = input("Enter the name of an animal: ").strip()
    animals_data = fetch_data(animal)

    # Check if animals_data is empty or None
    if not animals_data:
        html_output = f"""
        <html>
        <head><title>No Results</title></head>
        <body>
            <h2>The animal "{animal}" doesn't exist or was not found.</h2>
        </body>
        </html>
        """
    else:
        # Generate HTML output
        animals_html = ""
        for animal_obj in animals_data:
            animals_html += serialize_animal(animal_obj)

        # Read template
        with open("animals_template.html", "r", encoding="utf-8") as fileobj:
            template = fileobj.read()

        # Replace placeholder
        html_output = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write final HTML File
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_output)

    print("Website was successfully generated as 'animals.html'.")


if __name__ == "__main__":
    main()