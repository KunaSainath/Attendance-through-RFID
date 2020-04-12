# Attendance-through-RFID
Automated attendance system for universities using Radio Frequency Identification (RFID) tags.

The main motto of this project is to automate attendance system which would completely eliminate the human intervention in maintaining attendance system.

"active.json" and "archive.json" are sample json files which contain information about student rollnumbers and the RFID tags linked to them. The "active.json" file should contain the list of RFID tags of only currently active students in the university and it should undergo the changes in according to the students presence in the university. The "archive.json" file should contain the dictionary with key , value pairs of all the registered student rollnumbers and RFID tags. 

"mapping.py" is the main program that will run for every 60 seconds to check for inactive students in the university. The program takes "active.json" and "archive.json" files as input for every 60 seconds. By processing both the files, the program will generate a "today.log" file having information of absentees including their last active time. The program will automatically update the data in "today.log" file by appending the rollnumbers of new absentees for each 60 seconds. This would complete the purpose of attendance automation.

