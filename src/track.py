import datetime
import sys

# Function for generating signature lines for the sign-in sheets
def generateline(length):
    line = "          "
    for i in range(0, length-10):
        line = str(line) + "_"
    return line

# Function for generating the lists of members based upon the flag in the entry form
def generatelist(flag, attendance, members):
    li = ""
    for member in attendance:
        if member[1] == flag:
            index = -1
            for i in range(0, len(members)):
                if members[i][0] == member[0]:
                    index = i
                    break
            li = li+str(members[index][1]+"\n")
    return li

# Determine if there are any command line arguments
if len(sys.argv[1]) <= 0:
    print(sys.argv[1])
    print("No args specified")
    exit()
# If the generate argument is sent, generate a sign-in sheet and entry form
if sys.argv[1] == "generate":
    roster_raw = [line.rstrip('\n') for line in open(sys.argv[2], 'r')] # Read in the roster file
    roster_raw[0] = roster_raw[0][1:] # Quick fix for Microsoft excel adding weird characters to the beginning of files
    roster = []
    # Seperate the lines into name and email
    for i in range(0, len(roster_raw)):
        tmp = [roster_raw[i][0:roster_raw[i].find(',')], roster_raw[i][roster_raw[i].find(',')+1:]]
        roster.append(tmp)
    print("Roster Loaded")

    # Generate sign-in sheet
    x = datetime.datetime.now()
    output_signin = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_SignIn_Sheet.txt", 'w')
    output_signin.write("                        " + str(x.month) + '-' + str(x.day) + '-' + str(x.year) + " Sign In Sheet\n\n")
    for member in roster:
        tmp = str(member[0]) + str(generateline(70-len(member[0])) + "\n\n")
        output_signin.write(tmp)
    output_signin.close()

    # Generate entry form
    output_entry = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Entry_Form.csv", 'w')
    output_entry.write("Valid Options are H: Here A: Absent E: Excused\n")
    for member in roster:
        tmp = str(member[0]+",N/A\n")
        output_entry.write(tmp)
    output_entry.close()
    print("Files generated")

# if the convert argument is sent, read in the entry form and generate the lists
if sys.argv[1] == "convert":
    roster_raw = [line.rstrip('\n') for line in open(sys.argv[2], 'r')] # Read in the roster file
    roster_raw[0] = roster_raw[0][1:] # Quick fix for Microsoft excel adding weird characters to the beginning of files
    roster = []
    # Seperate the lines into name and email
    for i in range(0, len(roster_raw)):
        tmp = [roster_raw[i][0:roster_raw[i].find(',')], roster_raw[i][roster_raw[i].find(',') + 1:]]
        roster.append(tmp)
    print("Roster Loaded")
    entryform_raw = [line.rstrip('\n') for line in open(sys.argv[3], 'r')] # Read in the entry form
    entryform_raw.remove(entryform_raw[0]) # Remove the instruction line
    entryform = []
    # Seperate the lines into name and flag
    for i in range(0, len(entryform_raw)):
        tmp = [entryform_raw[i][0:entryform_raw[i].find(',')], entryform_raw[i][entryform_raw[i].find(',') + 1:]]
        entryform.append(tmp)
    print("Entry Form Loaded")

    # Genarte the list of those who attended and write it to a file
    x = datetime.datetime.now()
    output_attended = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Attended.txt", 'w')
    output_attended.write(generatelist('H', entryform, roster))
    output_attended.close()
    print("Attendance File Written")

    # Generate the list of those who were excused and write it to a file
    output_excused = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Excused.txt", 'w')
    output_excused.write(generatelist('E', entryform, roster))
    output_excused.close()
    print("Excused File Written")

    # Generate the list of those who were absent and write it to a file
    output_absent = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Absent.txt", 'w')
    output_absent.write(generatelist('A', entryform, roster))
    output_absent.close()
    print("Absent File Written")

# Error state in the event that an invalid argument is sent in
if sys.argv[1] != "generate" and sys.argv[1] != "convert":
    print("The valid arguments are:\ngenerate roster.csv\nconvert roster.csv entryform.csv")
    exit()
