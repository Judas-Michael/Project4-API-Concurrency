import wikipedia

# Returns number of search results
def getNumberOfResults(query):
    results = wikipedia.search(query,suggestion=True)
    return (len(results[0]))

# Returns search suggestions if user incorrectly spelled a word
def getSuggestions(query):
    suggestions = wikipedia.suggest(query)
    return suggestions

# Returns list of image links from search
def getImages(query):
    page = wikipedia.page(query)
    images = page.images
    return images

# Returns full list of possible results
def getSearchResults(query):
    suggestions = wikipedia.search(query)
    return suggestions[:4]

# Returns article of title
def getTitle(query):
    page = wikipedia.page(query)
    return page.title

# Returns article summary
def getSummary(query):
    summary = wikipedia.summary(query, sentences=1)
    return summary

# Returns the page URL
def getURL(query):
    page = wikipedia.page(query)
    url = page.url
    return url

def getPage(query):
    page = wikipedia.page(query)
    return page