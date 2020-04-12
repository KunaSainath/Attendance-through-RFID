import json , logging
from threading import Timer
def attendance():
	active_file = open("/home/sainath/RFID/active.json","r")	 #----------------------------------------> Opening the file active.json
	archive_file = open("/home/sainath/RFID/archive.json","r")  #---------------------------------------->	Opeining the file archive.json
	active_data = active_file.read()		 #----------------------------------------> Reading the file which has all the RFID tags of existing students of the college.
	archive_data = archive_file.read()		 #----------------------------------------> Reading the file which has the roll numbers of currently active students of the college.
	active_file.close()						 #----------------------------------------> Closing the file active.json.
	archive_file.close()					 #----------------------------------------> Closing the file archive.json.
	rfid_tags = json.loads(active_data)["rfid_tags"]     #----------------------------> Loading data from "active_data" in the form of a list(has all existing rfid tags)
	mapped_rollnumbers = json.loads(archive_data)["roll_numbers"]   #-----------------> Loading data from "archive_data" in the form of a dictionary(has pairs of rollnumbers which are active and rfid tags)
	absentees = []													
	for roll_number , rfid_tag in mapped_rollnumbers.items():		#-----------------> Looping through each item of currently active rollnumbers.
		if rfid_tag not in rfid_tags:		 #----------------------------------------> Checking for the roll numbers which are inactive.
			absentees.append(roll_number)	 #----------------------------------------> Storing the absentees in a list.
	if len(absentees) == 0:					 #----------------------------------------> If there are no absentees.
		logging.basicConfig(level = logging.INFO, 
							format = '%(message)s : --> %(asctime)s',
							datefmt = '%m/%d/%Y %I:%M',
							filename = 'today.log',
							filemode = 'a')	 #---------------------------------------->	Creating the log file with the specified format.
		LOG = logging.getLogger()			 #----------------------------------------> Calling the getLogger() function to load data into log file.
		LOG.info("NO ABSENTEES")			 #----------------------------------------> Loading the message, "NO ABSENTEES" into the log file.
	else:									 #----------------------------------------> If there are any inactive roll numbers.
		for absentee in absentees:			 #----------------------------------------> Looping through all the absentees.
			logging.basicConfig(level = logging.INFO, 
								format = '%(message)s : ACTIVE --> %(asctime)s',
								datefmt = '%m/%d/%Y %I:%M',
								filename = 'today.log',
								filemode = 'a') #-------------------------------------> Creating the log file with the specified format.
			LOG = logging.getLogger()		 #----------------------------------------> Calling the getLogger() function to load data into log file.
			LOG.info(absentee)			     #----------------------------------------> Loading each absentee's roll number into the log file.
	Timer(60,attendance).start()			 #----------------------------------------> Setting the timer for 60 sec. It makes the function to run for every 60 seconds and to check for absentees.
if __name__ == "__main__":
	attendance()							 #----------------------------------------> Calling the attendance() function.

		