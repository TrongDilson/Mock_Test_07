from flask import Flask
from flask_cors import CORS
from applicant.controller import applicant_bp

app = Flask(__name__)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Register Applicant Blueprint
app.register_blueprint(applicant_bp, url_prefix="/applicant")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
