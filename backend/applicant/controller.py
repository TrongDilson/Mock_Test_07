from flask_socketio import emit
from flask import Blueprint, jsonify, request
from applicant.service import ApplicantService

applicant_bp = Blueprint("applicant", __name__)

@applicant_bp.route("/classes", methods=["GET"])
def get_cultural_classes():
    """Endpoint to fetch available cultural classes."""
    try:
        cultural_classes = ApplicantService.get_cultural_classes()
        return jsonify([{"name": cls} for cls in cultural_classes]), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

@applicant_bp.route("/add", methods=["POST"])
def add_applicant():
    """Endpoint to add a new applicant."""
    data = request.json
    name = data.get("name")
    age = data.get("age")
    classes = data.get("classes")
    if not (name and age and classes):
        return jsonify({"error": "Invalid data"}), 400
    try:
        ApplicantService.add_applicant(name, age, classes)
        return jsonify({"message": "Applicant added"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@applicant_bp.route("/list", methods=["GET"])
def list_applicants():
    """Endpoint to list all applicants."""
    applicants = ApplicantService.get_applicants()
    return jsonify(applicants), 200

@applicant_bp.route("/delete/<string:name>", methods=["DELETE"])
def delete_applicant(name):
    """Endpoint to delete an applicant by name."""
    try:
        ApplicantService.delete_applicant(name)
        return jsonify({"message": f"Applicant {name} deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
