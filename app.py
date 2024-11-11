from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

MANGO_IMPORT_CONDITIONS = {
    "Thailand": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Vapor Heat Treatment (VHT)", "Hot Water Treatment (HWT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Pre-clearance inspection", "BICON registration"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=123456"
    },
    "India": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Irradiation Treatment", "Hot Water Treatment (HWT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration", "Irradiation Certificate"],
        "additional_requirements": ["Pre-shipment inspection", "BICON registration"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=654321"
    },
    "Pakistan": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Hot Water Treatment (HWT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Pre-shipment inspection"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=789012"
    },
    "Philippines": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Vapor Heat Treatment (VHT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["BICON registration", "Pre-clearance program"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=210987"
    },
    "Vietnam": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Vapor Heat Treatment (VHT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Pre-clearance inspection"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=345678"
    },
    "Taiwan": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Vapor Heat Treatment (VHT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Systems approach verification"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=876543"
    },
    "Mexico": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Hot Water Treatment (HWT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Pre-clearance program"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=567890"
    },
    "Fiji": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["High Temperature Forced Air (HTFA)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Pre-shipment inspection"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=234567"
    },
    "Haiti": {
        "permits_required": ["Import Permit", "Phytosanitary Certificate"],
        "treatments": ["Hot Water Treatment (HWT)"],
        "documentation": ["Treatment Certificate", "Packing Declaration"],
        "additional_requirements": ["Pre-shipment verification"],
        "bicon_link": "https://bicon.agriculture.gov.au/BiconWeb4.0/ViewElement/Element/Index?elementPk=987654"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/countries')
def get_countries():
    return jsonify(list(MANGO_IMPORT_CONDITIONS.keys()))

@app.route('/api/conditions/<country>')
def get_conditions(country):
    return jsonify(MANGO_IMPORT_CONDITIONS.get(country, {}))

if __name__ == '__main__':
    app.run(debug=True)
