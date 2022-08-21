import time
print("Welcome to the directory.\nWhat would you like to do?\n\nAdd student\n\nView all students enrolled\n\nRemove student\n\nSearch student")
userInput=input("\n")

## This would usually be attached to some sort of data base in which students already exist.
## But for this purpose we will be using names that just come from the program
## These are the students in which you will play around with
studentsEnrolled=["John", "Malachi", "Jacob", "Matt", "Carlie", "Kaitlyn", "Lauren", "Tiegan", "Lexus"]

if userInput=="Add Student" or userInput=="add student" or userInput==" Add student":
    newStudent=input("Name of new student\n")
    studentsEnrolled.append(newStudent)
    print("Student has been added to directory")
    i=0
    for x in studentsEnrolled:
        i=i+1
    print("number of students "+str(i))
    print(studentsEnrolled)
    time.sleep(10)
    exit()
elif userInput=="View all students enrolled" or userInput=="view all students enrolled" or userInput=="view all students" or userInput=="View all students" or userInput=="View All Students":
    i=0
    for x in studentsEnrolled:
        i=i+1
    print("number of students "+ str(i))
    print(studentsEnrolled)
    time.sleep(10)
    exit()
elif userInput=="remove student" or userInput=="Remove Student" or userInput=="Remove student":
    print(studentsEnrolled)
    removedStudent=input("Name of student wanting to be removed\n")
    studentsEnrolled.remove(removedStudent)
    print("Removing " +removedStudent+ ".....\n\n\n")
    print("Student has been removed")
    i=0
    for x in studentsEnrolled:
        i=i+1
    print("number of students "+str(i))
    print(studentsEnrolled)
    time.sleep(10)
    exit()
elif userInput=="Search student" or userInput=="Search Student" or userInput=="search student":
    name=input("What student would you like to search for??\n")
    if name in studentsEnrolled:
        print(name+" is currently enrolled")
        time.sleep(10)
        exit()
    else:
        print(name+" is not currently enrolled")
        time.sleep(10)
        exit()
else:
    exit()

