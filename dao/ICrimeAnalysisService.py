from abc import ABC, abstractmethod

class ICrimeAnalysisService(ABC):
    @abstractmethod
    def createIncident(self, incident):
        pass

    @abstractmethod
    def updateIncidentStatus(self, status, incident_id):
        pass

    @abstractmethod
    def getIncidentsInDateRange(self, start_date, end_date):
        pass

    @abstractmethod
    def searchIncidents(self, incident_type):
        pass

    @abstractmethod
    def generateIncidentReport(self, incident):
        pass

    @abstractmethod
    def createCase(self, case_description, incidents):
        pass

    @abstractmethod
    def getCaseDetails(self, case_id):
        pass

    @abstractmethod
    def updateCaseDetails(self, case_id, case_description):
        pass

    @abstractmethod
    def getAllCases(self):
        pass
