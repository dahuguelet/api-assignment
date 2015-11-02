import urllib2, json, re, os, sys, subprocess

def clean_json(json):
    # '''
    # Turn dirty State Department JSON into clean JSON.
    # '''
    return re.sub(r'new Date\(.*?\)', '""', json)

# 1. Filter to just Hillary Clinton's e-mails (case number F-2014-20439)
# 2. Request all e-mails containing the word Benghazi
# Also: limit is raised to far more than the number of all documents in the database
# Retrieving json
dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446145914167&searchText=Benghazi&beginDate=false&endDate=false&collectionMatch=false&postedBeginDate=false&postedEndDate=false&caseNumber=F-2014-20439&page=1&start=0&limit=100000000#').read()

# Cleaning and loading json
valid_json = clean_json(dirty_json)
data = json.loads(valid_json)

# 3. Return all e-mails and print the information necessary to download their raw files from the State Department.
# Grabbing PDF links from nested key "pdfLink" and added them to first part of State Department search HTML'


# Setting variable to differentiate each pdf downloaded
n = 1

# Starting user input loop
while True:
	answer = raw_input("Do you want to download PDFs of all Hillary emails related to Benghazi? (enter y/n)")		
	
	# If user says yes or y, files are downloaded.
	if answer in ("y","yes"):
		for i in data['Results']:
			response = 'https://foia.state.gov/searchapp/' + i['pdfLink']
			get = urllib2.urlopen(response)
			download = open("document" + str(n), "w")
			download.write(get.read())
			download.close()
			n = n+1;
		break			
	
	# If user says no, loop and program end.
	if answer in ("n","no"):
		print "Okay, maybe next time."
		break
	
	# If user enters something that doesn't make sense, loop restarts.
	else:
		print "Sorry, I didn't understand that."
		continue

	