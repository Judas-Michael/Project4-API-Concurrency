#Wiki API
#Don't forget to pip install wikipedia!

import wikipedia #imports wiki function
print wikipedia.summary("Wikipedia") #prints wiki's tagline/headline info


def wiki_main():
	wikipedia.set_lang("en") #sets language to english
	wikipedia.search(search_string) #TODO Get user input search string