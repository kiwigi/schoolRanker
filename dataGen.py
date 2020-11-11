import random

#This program will generate random data about students at a university 
#It will create a text file with 100 data enteries 
#Data format: studentID, High school, GPA

nameList = ["Cats", "Pizza", "Gaming","C4lg4ry","Default Dance", "Dogs", "Mars","P-72","Pp","Coding","Epic","360 No-scope"]
universityName = "University of " + random.choice(nameList)

i = 0
f = open(universityName+ " " +'data.txt','w') #File will be named after a (randomly generated) university

while i < 100:
    studentID = random.randint(1111,9999)
    highschoolName = random.choice(nameList) + " High School"
    gpa =  round(random.uniform(0.0, 4.0),1)
    dataEntry = str(studentID)+str(i) +" "+ highschoolName +" "+ str(gpa) #appending i to the ID will make sure it's unique
    print(dataEntry)
    f.write(dataEntry+'\n')
    i+=1



