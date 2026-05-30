# Import
import requests
import json

# Variables
MCSR_ENDPOINT = "https://api.mcsrranked.com/"
MCSR_ENDPOINT_ALT = "https://mcsrranked.com/api/"

chosenEndpoint = ""

# Function
def check_status():
    print("Don't forget all MCSR Ranked endpoints have a limit of 500 requests per minute unless specified on their documentation.")

    print()

    print(f"Checking endpoint {MCSR_ENDPOINT}...")
    mainEndpointResponse = requests.get(MCSR_ENDPOINT)

    if mainEndpointResponse.status_code == 200:
        print("Recieved code 200. Using main endpoint.")
        chosenEndpoint = MCSR_ENDPOINT
    else:
        Warning(f"Main endpoint failed with code {mainEndpointResponse.status_code}.")
        
        print()

        print(f"Checking endpoint {MCSR_ENDPOINT_ALT}...")
        altEndpointResponse = requests.get(MCSR_ENDPOINT_ALT)

        if altEndpointResponse.status_code == 200:
            print("Recieved code 200. Using alternate endpoint")
            chosenEndpoint = altEndpointResponse
        else:
            Warning(f"Alternate endpoint failed with code {altEndpointResponse.status_code}.")
            print()
            print("Failed to connect to all servers :(")
            input("Press enter to close.")
            quit()

def get_runner_data():
    pass

# Welcome
print("Welcome to mcsr-compare!")
print()

# Endpoint check
check_status()



input("Press enter to finish.")
