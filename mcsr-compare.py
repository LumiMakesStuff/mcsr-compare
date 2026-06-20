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

# Runner 1
runner1 = str(input("Pick your first runner (UUID, Name) | "))

print(f"Getting data for {runner1}...")
runner1Data = get_runner_data(runner1)

if runner1Data:
    print("Successfully received data!")
else:
    print("Failed to get data!")
    print()
    input("Press enter to close.")
    quit()

# Data Variables Runner 1
runner1Statistics = runner1Data["statistics"]
runner1StatTotal = runner1Statistics["total"]
runner1StatSeason = runner1Statistics["season"]

runner1Name = runner1Data["nickname"]
#---#
runner1CountryCode: str = runner1Data["country"]
if isinstance(runner1CountryCode, str):
    runner1CountryCode = runner1CountryCode.upper()
else:
    runner1CountryCode = "??"
#---#
runner1EloRate = runner1Data["eloRate"]
runner1EloRank = runner1Data["eloRank"]
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
runner1PlayTimeRankedTotal = runner1StatTotal["playtime"]["ranked"]
runner1PlayTimeCasualTotal = runner1StatTotal["playtime"]["casual"]
#---#
runner1PlayTimeRankedSeason = runner1StatSeason["playtime"]["ranked"]
runner1PlayTimeCasualSeason = runner1StatSeason["playtime"]["casual"]
#---#

# Runner 2
runner2 = str(input("Pick your second runner (UUID, Name) | "))

print(f"Getting data for {runner2}...")
runner2Data = None

if runner1 == runner2:
    runner2Data = runner1Data
else:
    get_runner_data(runner2)

if runner2Data:
    print("Successfully received data!")
else:
    print("Failed to get data!")
    print()
    input("Press enter to close.")
    quit()

# Data Variables Runner 2
runner2Statistics = runner2Data["statistics"]
runner2StatTotal = runner2Statistics["total"]
runner2StatSeason = runner2Statistics["season"]

runner2Name = runner2Data["nickname"]
#---#
runner2CountryCode: str = runner2Data["country"]
if isinstance(runner2CountryCode, str):
    runner2CountryCode = runner2CountryCode.upper()
else:
    runner2CountryCode = "??"
#---#
runner2EloRate = runner2Data["eloRate"]
runner2EloRank = runner2Data["eloRank"]
#---#
runner2PlayedMatchesRankedTotal = runner2StatTotal["playedMatches"]["ranked"]
runner2PlayedMatchesCasualTotal = runner2StatTotal["playedMatches"]["casual"]
#---#
runner2PlayedMatchesRankedSeason = runner2StatSeason["playedMatches"]["ranked"]
runner2PlayedMatchesCasualSeason = runner2StatSeason["playedMatches"]["casual"]
#---#
runner2HighestWinStreakRankedTotal = runner2StatTotal["highestWinStreak"]["ranked"]
runner2HighestWinStreakCasualTotal = runner2StatTotal["highestWinStreak"]["casual"]
#---#
runner2HighestWinStreakRankedSeason = runner2StatSeason["highestWinStreak"]["ranked"]
runner2HighestWinStreakCasualSeason = runner2StatSeason["highestWinStreak"]["casual"]
#---#
runner2CurrentWinStreakRankedTotal = runner2StatTotal["currentWinStreak"]["ranked"]
runner2CurrentWinStreakCasualTotal = runner2StatTotal["currentWinStreak"]["casual"]
#---#
runner2CurrentWinStreakRankedSeason = runner2StatSeason["currentWinStreak"]["ranked"]
runner2CurrentWinStreakCasualSeason = runner2StatSeason["currentWinStreak"]["casual"]
#---#
runner2BestTimeRankedTotal = runner2StatTotal["bestTime"]["ranked"]
runner2BestTimeCasualTotal = runner2StatTotal["bestTime"]["casual"]
#---#
runner2BestTimeRankedSeason = runner2StatSeason["bestTime"]["ranked"]
runner2BestTimeCasualSeason = runner2StatSeason["bestTime"]["casual"]
#---#
runner2PlayTimeRankedTotal = runner2StatTotal["playtime"]["ranked"]
runner2PlayTimeCasualTotal = runner2StatTotal["playtime"]["casual"]
#---#
runner2PlayTimeRankedSeason = runner2StatSeason["playtime"]["ranked"]
runner2PlayTimeCasualSeason = runner2StatSeason["playtime"]["casual"]
#---#

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

print()

if runner1Name == runner2Name:
    runner1Name = f"{runner1Name} (1)"
    runner2Name = f"{runner2Name} (2)"

table = prettytable.PrettyTable(["Stat", runner1Name, runner2Name])

table.add_row(["Country", runner1CountryCode, runner2CountryCode])

table.add_divider()

table.add_row(["Elo Rate", runner1EloRate, runner2EloRate])
table.add_row(["Elo Rank", runner1EloRank, runner2EloRate])

table.add_divider()

table.add_row(["All Time Ranked Matches", runner1PlayedMatchesRankedTotal, runner2PlayedMatchesRankedTotal])
table.add_row(["Season Ranked Matches", runner1PlayedMatchesRankedSeason, runner2PlayedMatchesRankedSeason])

table.add_row(["All Time Casual Matches", runner1PlayedMatchesCasualTotal, runner2PlayedMatchesCasualTotal])
table.add_row(["Season Casual Matches", runner1PlayedMatchesCasualSeason, runner2PlayedMatchesCasualSeason])

table.add_divider()

table.add_row(["All Time Highest Ranked Win Streak", runner1HighestWinStreakRankedTotal, runner2HighestWinStreakRankedTotal])
table.add_row(["Season Highest Ranked Win Streak", runner1HighestWinStreakRankedSeason, runner2HighestWinStreakRankedSeason])

table.add_row(["All Time Highest Casual Win Streak", runner1HighestWinStreakCasualTotal, runner2HighestWinStreakCasualTotal])
table.add_row(["Season Highest Casual Win Streak", runner1HighestWinStreakCasualSeason, runner2HighestWinStreakCasualSeason])

table.add_divider()

table.add_row(["All Time Current Ranked Win Streak", runner1CurrentWinStreakRankedTotal, runner2CurrentWinStreakRankedTotal])
table.add_row(["Season Current Ranked Win Streak", runner1CurrentWinStreakRankedSeason, runner2CurrentWinStreakRankedSeason])

table.add_row(["All Time Current Casual Win Streak", runner1CurrentWinStreakCasualTotal, runner2CurrentWinStreakCasualTotal])
table.add_row(["Season Current Casual Win Streak", runner1CurrentWinStreakCasualSeason, runner2CurrentWinStreakCasualSeason])

table.add_divider()

table.add_row(["All Time Fastest Ranked Run (In seconds)", runner1BestTimeRankedTotal, runner2BestTimeRankedTotal])
table.add_row(["Season Fastest Ranked Run (In seconds)", runner1BestTimeRankedSeason, runner2BestTimeRankedSeason])

table.add_row(["All Time Fastest Casual Run (In seconds)", runner1BestTimeCasualTotal, runner2BestTimeCasualTotal])
table.add_row(["Season Fastest Casual Run (In seconds)", runner1BestTimeCasualSeason, runner2BestTimeCasualSeason])

table.add_divider()

table.add_row(["All Time Play Time Ranked (In seconds)", runner1PlayTimeRankedTotal, runner2PlayTimeRankedTotal])
table.add_row(["Season Play Time Ranked (In seconds)", runner1PlayTimeRankedSeason, runner2PlayTimeRankedSeason])

table.add_row(["All Time Play Time Ranked (In seconds)", runner1PlayTimeCasualTotal, runner2PlayTimeCasualTotal])
table.add_row(["Season Play Time Ranked (In seconds)", runner1PlayTimeCasualSeason, runner2PlayTimeCasualSeason])

print(table)

# Finished
print()
print()
input("Press enter to finish.")
