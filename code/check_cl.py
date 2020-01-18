#import urllib.request python 3
import urllib.request
import smtplib
from os import listdir, getcwd
from os.path import isfile, join

#################################################
# FUNCTIONS   FUNCTIONS   FUNCTIONS   FUNCTIONS #
#################################################
def get_next_entry(src):
    entry_start = src.find('<li class=')
    entry_end = src.find('</li>') +5
    entry = src[ entry_start : entry_end ]
    rest_of_src = src[ entry_end + 1 : ]
    return entry, rest_of_src

def get_raw_entries(url):
    # read in the url's source code
    #file = urllib.request.urlopen(url)
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
    clean_entries = []
    for entry in raw_entries:
        # location
        if 'result-hood' not in entry:
            location = 'Unknown'
        else:
            loc_start = entry.find('result-hood')+15
            loc_end = entry.find(')</span>')
            location = entry[ loc_start : loc_end]
        #title
        title_start = entry.find('hdrlnk') + 8
        pre_title = entry[title_start:loc_start-15]
        title_end = entry[title_start:loc_start-15].find('</a>')
        title = pre_title[ : title_end ]
        # link
        link_start = entry.find('https')
        link_end = entry.find('.html') + 5
        link = entry[ link_start : link_end ]
        # price
        price_start = entry.rfind('result-price')+14
        pre_price = entry[price_start:loc_start]
        price_end = pre_price.find('</span>')
        price = pre_price[ : price_end ]
        if price == '': price = 'Not Listed'
        # appending
        listing = (title.upper(), link, price, location.upper())
        clean_entries.append(listing)
    return clean_entries

def find_novel(clean_entries, keywords, emailed_list):
    email = []
    for listing in clean_entries:
        for keyword in keywords:
           # print(already_sent)
            if keyword.upper() in listing[0] and listing[1] not in emailed_list:
                email.append(listing)
    return email

#########################################################
# MAIN   MAIN   MAIN   MAIN   MAIN   MAIN   MAIN   MAIN #
#########################################################

# This is the final function that the rasperry pi will run
def check_cl(url, keywords, emails):
    # making a file if none exist
    files = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
    if 'already_sent.txt' not in files:
        file = open('already_sent.txt', 'w')
        emailed_list = []
    # appending to the file if it does exist
    else:
        reading = open('already_sent.txt')
        emailed = reading.read()
        emailed_list = emailed[:-1].split(',')
        reading.close()
        file = open('already_sent.txt', 'a')
    # turning the listing we have already seen into a list
    raw_entries = get_raw_entries(url)
    clean_entries = get_clean_entries(raw_entries)
    to_email = find_novel(clean_entries, keywords, emailed_list)
    for i in to_email:
        file.write('{},'.format(i[1]))
    file.close()
    # use the to_email list and email new postings to list of emails provided
    if to_email:
        if len(to_email) == 1: title = keywords[0]
        else: title = keywords[0] + 's'
        content = """Subject: New {0} just posted on Craigslist!

Here is the information:

""".format(title)
        for posting in to_email:
            content += "Title: {}\nPrice: {}\nLocation: {}\nLink: {} \n\n".format(posting[0], posting[2], posting[3], posting[1])

        for email in emails:
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('daverbuj1@gmail.com','password-here')
            mail.sendmail('daverbuj1@gmail.com', email, content)
            mail.close()

####################
# SCRIPT RUNS HERE #
####################
url = 'https://sandiego.craigslist.org/search/sss?excats=7-13-22-2-24-1-4-19-2-1-1-1-1-9-10-1-1-1-2-2-8-1-1-1-1-1-4-1-3-1-3-1-1-1-1-7-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-1-1-1-1-2-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1&postedToday=1&search_distance=50&postal=92130'
check_cl(url, ['crash pad', 'crashpad', 'crash-pad', 'boulder pad', 'bouldering pad', 'climbing pad'], ['dan@mail.com', 'alon@mail.com'])
