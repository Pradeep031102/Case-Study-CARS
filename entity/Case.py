from entity.Incident import Incident
class Case:
    def __init__(self, caseID: int, caseDescription: str,incidents):
        self.caseID = caseID
        self.caseDescription = caseDescription
        self.incidents = incidents