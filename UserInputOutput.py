import WikipediaAPI
import youtubeAPI
import weatherapi

def user_input():
	input = True
	while (input == True):
		search_string = input("Please enter a location (city, country)")
		if " " not in search_string: #simple validation. Checks for space
		input = True
		else:
		input = False
		
def results_print():
	