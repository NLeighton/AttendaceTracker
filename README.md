# Attendance Tracker
### About
Attendance Tracker is a Python script for generating sign-in sheets and converting the data to an output accepted by Involvement Network.
### Usage
Start the process by generating a sign-in sheet using the roster:
```bash
python track.py generate roster.csv
```
That will generate a two files, a sign in sheet and a data entry form. The sign in sheet have the date of generation at the top as to make it obvious as to which day the sheet is for.

Once the attendance data has been entered into the data entry form run:
```bash
python track.py convert roster.csv entry_form.csv
```
to convert the data into 3 separate lists of who is present and who isn't. The format accepted by Involvement Network is a file with the email addresses of everyone with there being one email per line. Three files are generated and labeled accordingly to make the process of uploading them to Involvement Network easier.
### Notes
This project is not actively maintained since it does what needs to be done and was created purely as a temporary fix until the official software gets fixed.
