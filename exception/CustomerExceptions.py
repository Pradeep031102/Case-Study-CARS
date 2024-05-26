class IncidentNumberNotFoundException(Exception):
    def __init__(self, message="Incident number not found"):
        #calling the variable
        self.message = message
        super().__init__(self.message)
