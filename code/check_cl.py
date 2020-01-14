import urllib.request

url = 'https://sandiego.craigslist.org/search/sss?excats=7-13-22-2-24-1-4-19-2-1-1-1-1-9-10-1-1-1-2-2-8-1-1-1-1-1-4-1-3-1-3-1-1-1-1-7-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-1-1-1-1-2-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1&postedToday=1&search_distance=25&postal=92130'

def get_next_entry(src):
    entry_start = src.find('<li class=')
    entry_end = src.find('</li>') +5
    entry = src[ entry_start : entry_end ]
    rest_of_src = src[ entry_end + 1 : ]
    return entry, rest_of_src

def get_raw_entries(url):
    # read in the url's source code
    file = urllib.request.urlopen(url)
    # convert it to a string instead of bytes
    all_src = str(file.read())
    # extract just the part of the source code that contains the listings
    listings_src = all_src[ all_src.find('<ul class="rows">')+48 : all_src.rfind('class="search-legend bottom')-110 ]
    # initialize the list which will contain the raw source code for each inidividual entry
    raw_entries = []
    # use the get_next_entry function to loop through the source code, extracting the first entry and changing the
    # listings_src to exclude the extracted entry
    while listings_src.find('<li class=') != -1: # -1 is the output of .find() if not in string
        entry, listings_src = get_next_entry(listings_src)
        raw_entries.append(entry)
    return raw_entries

# FOR ALON TO DO
def get_clean_entries(raw_entries):
    clean_entries = # data structure of your choosing which will work well for our needs
    # code here...
    return clean_entries
    




#########################################################
# MAIN   MAIN   MAIN   MAIN   MAIN   MAIN   MAIN   MAIN #
#########################################################

# This is the final function that the rasperry pi will run
def check_cl(url, keywords, emails):
    raw_entries = get_raw_entries(url)
    # clean_entries = get_clean_entries(raw_entries)       < this is where your code will fit in once you finish it
