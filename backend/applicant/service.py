import redis
import json
from applicant.model import Applicant

APPLICANTS_KEY = "applicants_data"
redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

class ApplicantService:
    CULTURAL_CLASSES_KEY = "cultural_classes"

    @staticmethod
    def add_applicant(name, age, classes):
        """Add a new applicant to Redis."""
        data = redis_client.get(APPLICANTS_KEY)
        applicants = json.loads(data) if data else []

        # Check for duplicate applicant name
        if any(applicant["name"] == name for applicant in applicants):
            raise ValueError(f"Applicant with name {name} already exists.")

        applicant = Applicant(name, age, classes).to_dict()
        applicants.append(applicant)
        redis_client.set(APPLICANTS_KEY, json.dumps(applicants))
        return applicant

    @staticmethod
    def get_applicants():
        """Retrieve all applicants from Redis."""
        data = redis_client.get(APPLICANTS_KEY)
        if data:
            return json.loads(data)
        return []

    @staticmethod
    def delete_applicant(name):
        """Delete an applicant by name."""
        data = redis_client.get(APPLICANTS_KEY)
        if not data:
            raise ValueError(f"No applicants found to delete.")

        applicants = json.loads(data)
        updated_applicants = [applicant for applicant in applicants if applicant["name"] != name]

        if len(applicants) == len(updated_applicants):
            raise ValueError(f"Applicant with name {name} not found.")

        redis_client.set(APPLICANTS_KEY, json.dumps(updated_applicants))
        return True

    @staticmethod
    def get_cultural_classes():
        """Retrieve cultural classes from Redis."""
        data = redis_client.get(ApplicantService.CULTURAL_CLASSES_KEY)
        if data:
            return json.loads(data)
        return ["Piano", "Martial Arts"]  # Default classes if none are set

    @staticmethod
    def set_cultural_classes(classes):
        """Set cultural classes in Redis."""
        redis_client.set(ApplicantService.CULTURAL_CLASSES_KEY, json.dumps(classes))
