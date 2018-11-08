import datetime
import sys


def generateline(length):
    line = "          "
    for i in range(0, length-10):
        line = str(line) + "_"
    return line


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


if len(sys.argv[1]) <= 0:
    print(sys.argv[1])
    print("No args specified")
    exit()

if sys.argv[1] == "generate":
    if len(sys.argv) < 3:
        print("Roster file not provided")
        exit()
    roster_raw = [line.rstrip('\n') for line in open(sys.argv[2], 'r')]
    roster = []
    for i in range(0, len(roster_raw)):
        tmp = [roster_raw[i][0:roster_raw[i].find(',')], roster_raw[i][roster_raw[i].find(',')+1:]]
        roster.append(tmp)
    print("Roster Loaded")
    x = datetime.datetime.now()
    output_signin = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_SignIn_Sheet.txt", 'w')
    output_signin.write("                        " + str(x.month) + '-' + str(x.day) + '-' + str(x.year) + " Sign In Sheet\n\n")
    for member in roster:
        tmp = str(member[0]) + str(generateline(70-len(member[0])) + "\n\n")
        output_signin.write(tmp)
    output_signin.close()
    output_entry = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Entry_Form.csv", 'w')
    output_entry.write("Valid Options are H: Here A: Absent E: Excused\n")
    for member in roster:
        tmp = str(member[0]+",N/A\n")
        output_entry.write(tmp)
    output_entry.close()
    print("Files generated")

if sys.argv[1] == "convert":
    if len(sys.argv) < 4:
        print("Not all parameters not provided")
        exit()
    roster_raw = [line.rstrip('\n') for line in open(sys.argv[2], 'r')]
    roster = []
    for i in range(0, len(roster_raw)):
        tmp = [roster_raw[i][0:roster_raw[i].find(',')], roster_raw[i][roster_raw[i].find(',') + 1:]]
        roster.append(tmp)
    print("Roster Loaded")
    entryform_raw = [line.rstrip('\n') for line in open(sys.argv[3], 'r')]
    entryform_raw.remove(entryform_raw[0])
    entryform = []
    for i in range(0, len(entryform_raw)):
        tmp = [entryform_raw[i][0:entryform_raw[i].find(',')], entryform_raw[i][entryform_raw[i].find(',') + 1:]]
        entryform.append(tmp)
    print("Entry Form Loaded")
    x = datetime.datetime.now()
    output_attended = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Attended.txt", 'w')
    output_attended.write(generatelist('H', entryform, roster))
    output_attended.close()
    print("Attendance File Written")
    output_excused = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Excused.txt", 'w')
    output_excused.write(generatelist('E', entryform, roster))
    output_excused.close()
    print("Excused File Written")
    output_absent = open(str(x.month) + '_' + str(x.day) + '_' + str(x.year) + "_Absent.txt", 'w')
    output_absent.write(generatelist('A', entryform, roster))
    output_absent.close()
    print("Absent File Written")

if sys.argv[1] != "generate" and sys.argv[1] != "convert":
    print("The valid arguments are:\ngenerate roster.csv\nconvert roster.csv entryform.csv")
    exit()
