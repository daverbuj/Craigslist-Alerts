# Craigslist Alerts

### Goal: 
Create a python script that can run continuously (every minute) on Raspberry Pi that will check if there are any new postings on Craigslist that match the desired keyword(s). Email new unique postings.

### Inputs: 
* craigslist url: 'http.url.com'
* list of keyword(s): ['crashpad', 'crash pad', 'bouldering pad']
* list of email(s) to send alerts to: ['dan@email.com', 'alon@email.com']

### Notes:
The url we use to check listings will change depending on what we are interested in. For example, for crashpads I've selected 'sporting goods', 'general for sale', and 'free stuff', as well as postings close to the zip code. (w/in 25 mile)

So, Below is the url we will be using for crash pads:

https://sandiego.craigslist.org/search/sss?excats=7-13-22-2-24-1-4-19-2-1-1-1-1-9-10-1-1-1-2-2-8-1-1-1-1-1-4-1-3-1-3-1-1-1-1-7-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1-1-1-1-1-2-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-2-1&postedToday=1&search_distance=25&postal=92130

### CRON
Using Raspberry Pi's Cron job scheduler, create a new job that will run the program every minute

Edit the Cron scheduler

`crontab -e`

Add the job at the bottom of the file

`1-59 * * * * /abspath/python /abspath/check_cl.py`
