#Saving data in json format

data = {
	"leagues" : {
		"ligaMx" : {
			"teams" : {
				"Tigres" : {
					"nextMatch" : {
						"against" : "Necaxa",
						"stadium" : "Estadio Victoria",
						"date" : "21/04/18",
						"status" : "away"
					},
					"pastMatch" : {
						"against" : "Cruz Azul",
						"stadium" : "Estadio Universitario",
						"date" : "14/04/18"
					} ,
					"leagueInfo" : {
						"place" : "4",
						"goals" : "40", #random number, just for testing
						"points" : "26",
						"streak" : "1"
					},
					"overallInfo" : {
						"leagueChampionships" : "6",
						"internationalChampionships" : "0",
						"rival" : "Monterrey"
					}
				} #end of tigres dict

			} #end of teams dict
		} #end of ligaMx dict
	} #end of leagues dict
}