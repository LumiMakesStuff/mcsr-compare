# mcsr-compare.py
# Main file for LumiMakesStuff/mcsr-compare

# Import
import requests
import prettytable

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Variables
MCSR_ENDPOINT = "https://api.mcsrranked.com/"
MCSR_ENDPOINT_ALT = "https://mcsrranked.com/api/"

chosenEndpoint = ""

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Functions
def check_status():
    global chosenEndpoint

    print("Don't forget all MCSR Ranked endpoints have a limit of 500 requests every 10 minutes unless specified on their documentation.")

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
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Welcome
print("Welcome to MCSR Ranked Compare!")
print()

# Endpoint check
check_status()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Player 1
# For debug using current 1st on leaderboard (edcr)
print()

print("Getting data for edcr...")
data = get_runner_data("edcr")

if data:
    print("Successfully recieved data!")
else:
    print("Failed to get data!")
    print()
    input("Press enter to close.")
    quit()

# Data Variables Runner 1
runner1Statistics = data["statistics"]
runner1StatTotal = runner1Statistics["total"]
runner1StatSeason = runner1Statistics["season"]

runner1Name = data["nickname"]
#---#
runner1CountryCode: str = data["country"].upper()
#---#
runner1EloRate = data["eloRate"]
runner1EloRank = data["eloRank"]
#---#
runner1PlayedMatchesRankedTotal = runner1StatTotal["playedMatches"]["ranked"]
runner1PlayedMatchesCasualTotal = runner1StatTotal["playedMatches"]["casual"]
#---#
runner1PlayedMatchesRankedSeason = runner1StatSeason["playedMatches"]["ranked"]
runner1PlayedMatchesCasualSeason = runner1StatSeason["playedMatches"]["casual"]
#---#
runner1HighestWinStreakRankedTotal = runner1StatTotal["highestWinStreak"]["ranked"]
runner1HighestWinStreakCasualTotal = runner1StatTotal["highestWinStreak"]["casual"]
#---#
runner1HighestWinStreakRankedSeason = runner1StatSeason["highestWinStreak"]["ranked"]
runner1HighestWinStreakCasualSeason = runner1StatSeason["highestWinStreak"]["casual"]
#---#
runner1CurrentWinStreakRankedTotal = runner1StatTotal["currentWinStreak"]["ranked"]
runner1CurrentWinStreakCasualTotal = runner1StatTotal["currentWinStreak"]["casual"]
#---#
runner1CurrentWinStreakRankedSeason = runner1StatSeason["currentWinStreak"]["ranked"]
runner1CurrentWinStreakCasualSeason = runner1StatSeason["currentWinStreak"]["casual"]
#---#
runner1BestTimeRankedTotal = runner1StatTotal["bestTime"]["ranked"]
runner1BestTimeCasualTotal = runner1StatTotal["bestTime"]["casual"]
#---#
runner1BestTimeRankedSeason = runner1StatSeason["bestTime"]["ranked"]
runner1BestTimeCasualSeason = runner1StatSeason["bestTime"]["casual"]
#---#
runner1PlayTimeRankedTotal = runner1StatTotal["playTime"]["ranked"]
runner1PlayTimeCasualTotal = runner1StatTotal["playTime"]["casual"]
#---#
runner1PlayTimeRankedSeason = runner1StatSeason["playTime"]["ranked"]
runner1PlayTimeCasualSeason = runner1StatSeason["playTime"]["casual"]
#---#

# Data Variables Runner 2

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

print()
table = prettytable.PrettyTable(["Stat", runner1Name])

table.add_row(["Country", runner1CountryCode])

table.add_divider()

table.add_row(["Elo Rate", runner1EloRate])
table.add_row(["Elo Rank", runner1EloRank])

table.add_divider()

table.add_row(["All Time Ranked Matches", runner1PlayedMatchesRankedTotal])
table.add_row(["Season Ranked Matches", runner1PlayedMatchesRankedSeason])

table.add_row(["All Time Casual Matches", runner1PlayedMatchesCasualTotal])
table.add_row(["Season Casual Matches", runner1PlayedMatchesCasualSeason])

table.add_divider()

table.add_row(["All Time Highest Ranked Win Streak", runner1HighestWinStreakRankedTotal])
table.add_row(["Season Highest Ranked Win Streak", runner1HighestWinStreakRankedSeason])

table.add_row(["All Time Highest Casual Win Streak", runner1HighestWinStreakCasualTotal])
table.add_row(["Season Highest Casual Win Streak", runner1HighestWinStreakCasualSeason])

table.add_divider()

table.add_row(["All Time Current Ranked Win Streak", runner1CurrentWinStreakRankedTotal])
table.add_row(["Season Current Ranked Win Streak", runner1CurrentWinStreakRankedSeason])

table.add_row(["All Time Current Casual Win Streak", runner1CurrentWinStreakCasualTotal])
table.add_row(["Season Current Casual Win Streak", runner1CurrentWinStreakCasualSeason])

table.add_divider()

table.add_row(["All Time Fastest Ranked Run (In seconds)", runner1BestTimeRankedTotal])
table.add_row(["Season Fastest Ranked Run (In seconds)", runner1BestTimeRankedSeason])

table.add_row(["All Time Fastest Casual Run (In seconds)", runner1BestTimeCasualTotal])
table.add_row(["Season Fastest Casual Run (In seconds)", runner1BestTimeCasualSeason])

table.add_divider()

table.add_row(["All Time Play Time (In seconds)", runner1PlayTimeRankedTotal])
table.add_row(["Season Play Time (In seconds)", runner1PlayTimeRankedSeason])

table.add_row(["All Time Play Time (In seconds)", runner1PlayTimeCasualTotal])
table.add_row(["Season Play Time (In seconds)", runner1PlayTimeCasualSeason])

print(table)





# Finished
print()
print()
input("Press enter to finish.")
