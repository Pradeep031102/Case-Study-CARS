class Incident:
    def __init__(self, incident_id, incident_type, incident_date, location, description, status, victim_id, suspect_id):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.incident_date = incident_date
        self.location = location
        self.description = description
        self.status = status
        self.victim_id = victim_id
        self.suspect_id = suspect_id
