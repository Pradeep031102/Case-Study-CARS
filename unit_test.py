import unittest
from unittest.mock import MagicMock
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incident import  Incident
from util.DBConnUtil import DBConnUtil

from datetime import datetime


class TestCrimeAnalysisService(unittest.TestCase):
    def test_create_incident_success(self):
        # Mock user input
        user_input = {
            "incident_id":15 ,
            "incident_type": "Theft",
            "incident_date": '2024-04-15',
            "location_longitude": 45.9078,
            "location_latitude": -24.7893,
            "description": "Robbery",
            "status": "Open",
            "victim_id": 101,
            "suspect_id": 1002
        }

        # Create an Incident object
        incident = Incident(**user_input)

        # Create an instance of CrimeAnalysisServiceImpl
        service = CrimeAnalysisServiceImpl()

        # Call the createIncident method with the incident object
        success = service.createIncident(incident)

        # Assert that the method returns True (indicating successful creation)
        self.assertTrue(success)
    
    def test_update_incident_status_success(self):
        # Mock user input
        incident_id = 2
        new_status = "Closed"
        service = CrimeAnalysisServiceImpl()

        # Call the method
        success = service.updateIncidentStatus(new_status, incident_id)

        # Assertions
        self.assertTrue(success)
        

if __name__ == '__main__':
    unittest.main()