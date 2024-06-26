from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incident import Incident
from entity.Case import Case
from exception.CustomerExceptions import IncidentNumberNotFoundException

def display_menu():
    print("Crime Analysis and Reporting System (CARS)")
    print("1. Create a new Incident")
    print("2. Update Incident Status")
    print("3. Get Incidents within a Date Range")
    print("4. Search Incidents by Type")
    print("5. Generate Incident Report")
    print("6. Create a new Case")
    print("7. Get Case Details")
    print("8. Update Case Details")
    print("9. Get All Cases")
    print("10. Exit")

def main():
    service = CrimeAnalysisServiceImpl()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            incident_type = input("Enter incident type: ")
            incident_date = input("Enter incident date (YYYY-MM-DD): ")
            location_longitude = input("Enter location Longitude: ")
            location_latitude = input("Enter location Latitude: ")
            description = input("Enter description: ")
            status = input("Enter status: ")
            victim_id = int(input("Enter victim ID: "))
            suspect_id = int(input("Enter suspect ID: "))
            incident = Incident(None,incident_type, incident_date, location_longitude, location_latitude, description, status, victim_id, suspect_id)
            if service.createIncident(incident):
                print("Incident created successfully.")

        elif choice == '2':
            incident_id = int(input("Enter incident ID: "))
            status = input("Enter new status: ")
            try:
                if service.updateIncidentStatus(status, incident_id):
                    print("Incident status updated successfully.")
            except IncidentNumberNotFoundException as e:
                print(e.message)

        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            incidents = service.getIncidentsInDateRange(start_date, end_date)
            for incident in incidents:
                print(incident)

        elif choice == '4':
            incident_type = input("Enter incident type to search: ")
            incidents = service.searchIncidents(incident_type)
            for incident in incidents:
                print(incident)

        elif choice == '5':
            incident_id = int(input("Enter incident ID: "))
            incident = Incident(incident_id, None, None, None, None, None, None, None, None)
            report = service.generateIncidentReport(incident)
            print(report)

        elif choice == '6':
            # Collect input for creating a new case
            caseID = int(input("Enter Case ID: "))
            caseDescription = input("Enter Case Description: ")
            incidentIDs = input("Enter Incident IDs (comma separated): ").split(',')
            incidents = [Incident(int(id), None, None, None, None, None, None, None, None) for id in incidentIDs]
            if incidents:
                createdCase = service.createCase(caseDescription, incidents)
                if createdCase is not None:
                    print("Case created successfully!")
                else:
                    print("Failed to create case.")
            else:
                print("No valid incidents found.")
                
        elif choice == '7':
            # Collect input for getting case details
            caseID = int(input("Enter Case ID: "))
            case_details = service.getCaseDetails(caseID)
            if case_details:
                print(case_details)
            else:
                print("Case not found.")

        elif choice == '8':
            case_id = int(input("Enter case ID: "))
            case = service.getCaseDetails(case_id)
            if case:
                case_description = input("Enter new case description: ")
                service.updateCaseDetails(case_id,case_description)
                print("Case details updated successfully.")
            else:
                print("Case not found.")
        elif choice == '9':
            all_cases = service.getAllCases()
            for case in all_cases:
                print(case)

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
