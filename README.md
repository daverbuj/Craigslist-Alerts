# Craigslist Alerts

### Goal: 
Create a python script that we can run continuously (every ~30 minutes) on Raspberry Pi that will check if there are any new postings that match our keyword(s). Email new postings to us.

### Inputs: 
* craigslist url: 'http.url.com'
* list of keyword(s): ['crashpad', 'crash pad', 'bouldering pad']
* list of email(s) to send alerts to: ['dan@email.com', 'alon@email.com']

### Notes:
The url we use to check listings will change depending on what we are interested in. For example, for crashpads I've selected 'sporting goods', 'general for sale', and 'free stuff', as well as postings close to our zip code. (w/in 25 mile)
Below is the url we will be using for crash pads.
https://sandiego.craigslist.org/search/sss?excats=7-13-22-2-24-1-4-19-2-1-1-1-1-9-10-1-1-1-2-2-8-1-1-1-1-1-4-1-3-1-3-1-1-1-1-7-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-1-1-1-1-2-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1&postedToday=1&search_distance=25&postal=92130

We only want to send alerts from a posting once. If our script detects a keyword from the same listing which has already been emailed to us, don't send another email about it.

### Steps:
The main function will be called check_cl

#### 1.
I'll create the first function which takes the source code and outputs a list of raw entries. The raw entries will also be source code but it only contain the information on one posting.

#### 2.
You will then create a function that takes the raw entries and cleans them up, resulting in a data structure that has the title of the posting and the link to the posting.

