"""
Property Management System App

This file defines a Flask web application for managing properties. It uses a PropertyManager class to handle
the management of properties, and it provides various routes for filtering, sorting, and saving property data.
"""

import json
import configparser
from classes.property_manager import PropertyManager

from flask import Flask, render_template, request


# Create a configparser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Access values of input and output file
input_file = config["FILES"]["Input"]
output_file = config["FILES"]["Output"]

app = Flask(__name__)
property_manager = PropertyManager()
property_manager.read_properties_from_json(input_file)


@app.route('/')
def homepage():
    """
    Route for the homepage that renders the index.html template with the list of all properties.

    Returns:
        render_template: The rendered template with property data.
    """
    return render_template(
        "index.html",
        properties=property_manager.get_properties(),
        info="all")


@app.route("/filter_by_location", methods=["POST"])
def filter_by_location():
    """
    Route for filtering properties by location.

    Returns:
        render_template: The rendered template with filtered property data.
    """
    location = request.form["location"]
    filtered_properties = property_manager.filter_by_location(
        location=location)
    return render_template(
        'index.html',
        properties=filtered_properties,
        info=f"filtered by location: {location}")


@app.route("/filter_by_price", methods=["POST"])
def filter_by_price():
    """
    Route for filtering properties by price range.

    Returns:
        render_template: The rendered template with filtered property data.
    """
    min_price = int(request.form["min_price"])
    if not request.form["max_price"]:
        max_price = None
    else:
        max_price = int(request.form["max_price"])

    filtered_properties = property_manager.filter_by_price(min_price=min_price,
                                                           max_price=max_price)
    return render_template(
        "index.html",
        properties=filtered_properties,
        info=f"filtered by price: min={min_price}, max={max_price}")


@app.route("/filter_by_square_footage", methods=["POST"])
def filter_by_square_footage():
    """
    Route for filtering properties by square footage range.

    Returns:
        render_template: The rendered template with filtered property data.
    """
    min_square_footage = int(request.form["min_square_footage"])
    if not request.form["max_square_footage"]:
        max_square_footage = None
    else:
        max_square_footage = int(request.form["max_square_footage"])

    filtered_properties = property_manager.filter_by_square_footage(
        min_square_footage=min_square_footage, max_square_footage=max_square_footage)
    return render_template(
        "index.html",
        properties=filtered_properties,
        info=f"filtered by square footage: min={min_square_footage}, max={max_square_footage}")


@app.route("/filter_by_property_type", methods=["POST"])
def filter_by_property_type():
    """
    Route for filtering properties by property type.

    Returns:
        render_template: The rendered template with filtered property data.
    """
    property_type = request.form["property_type"]
    filtered_properties = property_manager.filter_by_property_type(
        property_type=property_type)
    return render_template(
        "index.html",
        properties=filtered_properties,
        info=f"filtered by property type {property_type}")


@app.route("/sort", methods=["POST"])
def sort():
    """
    Route for sorting properties based on the given attribute and sorting type.

    Returns:
        render_template: The rendered template with sorted property data.
    """
    sorting_attribute = request.form["sorting_attribute"]
    sorting_type = request.form["sorting_type"]
    sorted_properties = property_manager.sort_properties(
        sorting_attribute=sorting_attribute, sorting_type=sorting_type)
    return render_template(
        "index.html",
        properties=sorted_properties,
        info=f"sorted by {sorting_attribute} in {sorting_type} order")


@app.route("/save_current_selection", methods=["POST"])
def save_current_selection():
    """
    Route for saving the current selection of properties to a JSON file.

    Returns:
        render_template: The rendered template indicating the success and the path to the saved file.
    """
    selected_properties = request.form.getlist("selected_properties")
    selected_properties_data = []

    for prop in selected_properties:
        for p in property_manager.get_properties():
            if p.get_id() == prop:
                selected_properties_data.append(p.to_dict())
                break

    with open(output_file, "w", encoding="utf-8") as jf:
        json.dump(selected_properties_data, jf, ensure_ascii=False, indent=4)

    return render_template("success.html", path_to_file=output_file)


if __name__ == '__main__':
    app.run(debug=True)
