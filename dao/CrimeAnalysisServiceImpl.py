from dao.ICrimeAnalysisService import ICrimeAnalysisService
from util.DBConnUtil import DBConnUtil
from exception.CustomerExceptions import IncidentNumberNotFoundException

class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def createIncident(self, incident):
        cursor = self.connection.cursor()
        query = """INSERT INTO Incident (IncidentType, IncidentDate, Location_Longitude, Location_Latitude, Description, Status, VictimID, SuspectID) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, incident.incident_type, incident.incident_date, incident.location_longitude, incident.location_latitude, incident.description, incident.status, incident.victim_id, incident.suspect_id)
        self.connection.commit()
        return True

    def updateIncidentStatus(self, status, incident_id):
        cursor = self.connection.cursor()
        query = "UPDATE Incident SET Status = ? WHERE IncidentID = ?"
        cursor.execute(query, status, incident_id)
        if cursor.rowcount == 0:
            raise IncidentNumberNotFoundException()
        self.connection.commit()
        return True

    def getIncidentsInDateRange(self, start_date, end_date):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incident WHERE IncidentDate BETWEEN ? AND ?"
        cursor.execute(query, start_date, end_date)
        incidents = cursor.fetchall()
        return incidents

    def searchIncidents(self, incident_type):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incident WHERE IncidentType = ?"
        cursor.execute(query, incident_type)
        incidents = cursor.fetchall()
        return incidents

    def generateIncidentReport(self, incident):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Reports WHERE IncidentID = ?"
        cursor.execute(query, incident.incident_id)
        report = cursor.fetchone()
        if report:
            return report
        else:
            report_query = """INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status)
                              VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(report_query, incident.incident_id, 1, incident.incident_date, incident.description, "Draft")
            self.connection.commit()
            cursor.execute(query, incident.incident_id)
            report = cursor.fetchone()
            return report

    def createCase(self, case_description, location, incidents):
        cursor = self.connection.cursor()
        
        for incident in incidents:
            case_incident_query = "INSERT INTO Evidence (Description, LocationFound, IncidentID) VALUES (?,?,?)"
            cursor.execute(case_incident_query, (case_description), location, (incident.incident_id))
        self.connection.commit()
        return {"description": case_description, "incidents": incidents}



    def getCaseDetails(self, case_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM Evidence WHERE EvidenceID = ?"
        cursor.execute(query, case_id)
        case = cursor.fetchone()
        if not case:
            return None

        incidents_query = "SELECT * FROM Incident WHERE IncidentID IN (SELECT IncidentID FROM Evidence WHERE EvidenceID = ?)"
        cursor.execute(incidents_query, case_id)
        incidents = cursor.fetchall()
        return {"case": case, "incidents": incidents}

    def updateCaseDetails(self, case):
        cursor = self.connection.cursor()
        query = "UPDATE Evidence SET Description = ? WHERE EvidenceID = ?"
        cursor.execute(query, case['description'], case['case_id'])
        self.connection.commit()
        return True

    def getAllCases(self):
         query = "SELECT * FROM Evidence"
         cursor = self.connection.cursor()
         cursor.execute(query)
         cases = cursor.fetchall()
         cursor.close()
         self.connection.close()
         return cases
