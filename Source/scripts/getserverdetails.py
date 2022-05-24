import requests

host = "176.57.173.3"
port = 28615

url = "https://vrisingserverapi.herokuapp.com/all/" + host + "/" + str(port)
response = requests.request("GET", url)
jsonResponse = response.json()

if jsonResponse == {}:
    print("No Data")
else:
    serverName = jsonResponse["name"]
    serverMap = jsonResponse["map"]
    serverPassword = jsonResponse["password"]
    serverPlayersOnline = jsonResponse["raw"]["numplayers"]
    serverPlayers = jsonResponse["players"]
    serverMaxPlayers = jsonResponse["maxplayers"]
    serverPlayIP = jsonResponse["connect"]
    serverPing = jsonResponse["ping"]

    print("Server Name: " + serverName)
    print("Server Map: " + serverMap)
    print("Server Password: " + str(serverPassword))
    print("Server Players Online: " + str(serverPlayersOnline))
    print("Server Players: " + str(serverPlayers))
    print("Server Max Players: " + str(serverMaxPlayers))
    print("Server Play IP: " + serverPlayIP)
    print("Server Ping: " + str(serverPing))