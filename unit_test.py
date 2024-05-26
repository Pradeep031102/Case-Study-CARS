import unittest
from unittest.mock import MagicMock
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incident import  Incident



class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        self.service=CrimeAnalysisServiceImpl()

    def test_add_incident(self):
        incidentType= "Homicide"
        incidentDate= '2024-04-29'
        Location_Longitude= 36.9028
        Location_Latitude= -26.6458
        description= "Homicide attack occurred at the bank."
        status= "Under Investigation"
        victimID= 103
        suspectID= 1005
        self.test_incident = Incident(None, incidentType, incidentDate,Location_Longitude,Location_Latitude,description,status,victimID,suspectID)
        self.test_incident_id = self.service.createIncident(self.test_incident)
        self.assertIsNotNone(self.test_incident_id)

    def test_create_incident_success(self):
       
        user_input = {
            "incident_id": 16,
            "incident_type": "Theft",
            "incident_date": '2024-04-21',
            "location_longitude": 25.0920,
            "location_latitude": -45.2763,
            "description": "Theft of Gold",
            "status": "Open",
            "victim_id": 101,
            "suspect_id": 1002
        }

        incident = Incident(**user_input)

        service = CrimeAnalysisServiceImpl()

        success = service.createIncident(incident)

        self.assertTrue(success)
    
    def test_update_incident_status_success(self):
        
        incident_id = 1
        new_status = "Closed"
        service = CrimeAnalysisServiceImpl()

 
        success = service.updateIncidentStatus(new_status, incident_id)

        self.assertTrue(success)
        

if __name__ == '__main__':
    unittest.main()