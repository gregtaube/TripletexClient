from TripletexClient import TripletexClient

request_headers = {

}

client = TripletexClient(host="http://localhost:8080", request_headers=request_headers)

employee_payload = {
    "firstName": "ansatt med lonnsdetaljer",
    "userType": "NO_ACCESS",
    "department": {"id": 101472},
    "lastName": "best",
    "dateOfBirth": "2001-01-01",
}
employee_response = client.make_employee(employee_payload)
employee_id = employee_response['value']['id']

divisions = client.get_divisions()
divisionId = divisions['values'][0]['id']


employment_payload = {
    "startDate": "2019-09-01",
    "division": {
        "id": divisionId
    },
    "employee": {
        "id": employee_id
    },

}
employment_response = client.make_employment(employment_payload)
print(employment_response)

employment_details_payload = {
    "annualSalary": 500000,
    "percentageOfFullTimeEquivalent": 100,
    "employment": {
        "id": employment_response['value']['id']
    }
}
employmentDetails = client.make_employment_details(employment_details_payload)
print(employmentDetails)

