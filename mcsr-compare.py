# mcsr-compare.py
# Main file for LumiMakesStuff/mcsr-compare

# Import
import requests
import json # Will use soon

# Variables
MCSR_ENDPOINT = "https://api.mcsrranked.com/"
MCSR_ENDPOINT_ALT = "https://mcsrranked.com/api/"

chosenEndpoint = ""


# Functions
def check_status():
    global chosenEndpoint

    print("Don't forget all MCSR Ranked endpoints have a limit of 500 requests per minute unless specified on their documentation.")

    print()

    # Main endpoint
    print(f"Checking endpoint {MCSR_ENDPOINT}...")
    mainEndpointResponse = requests.get(MCSR_ENDPOINT)

    # Result
    if mainEndpointResponse.status_code == 200:
        # Main Success
        print("Recieved code 200. Using main endpoint.")
        chosenEndpoint = MCSR_ENDPOINT
    else:
        # Main fail
        Warning(f"Main endpoint failed with code {mainEndpointResponse.status_code}.")
        
        print()

        # Try alt instead
        print(f"Checking endpoint {MCSR_ENDPOINT_ALT}...")
        altEndpointResponse = requests.get(MCSR_ENDPOINT_ALT)

        # Result
        if altEndpointResponse.status_code == 200:
            # Alt Success
            print("Recieved code 200. Using alternate endpoint")
            chosenEndpoint = altEndpointResponse
        else:
            # Alt failed
            Warning(f"Alternate endpoint failed with code {altEndpointResponse.status_code}.")
            
            print()

            # Cannot continue
            print("Failed to connect to all servers :(")
            input("Press enter to close.")
            quit()

def get_runner_data(runnerIdentifier: str):
    request = requests.get(f"{chosenEndpoint}users/{runnerIdentifier}")

    if request.status_code == 200:
        # Success
        print(f"Got data for {runnerIdentifier}")
        
        json = request.json()
        data = json.get("data")

        return data

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Welcome
print("Welcome to MCSR Ranked Compare!")
print()

# Endpoint check
check_status()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Player 1
# For debug using current 1st on leaderboard (edcr)
print()

print("Getting data for edcr...")
data = get_runner_data("edcr")
print(data)

print()
print()
input("Press enter to finish.")
