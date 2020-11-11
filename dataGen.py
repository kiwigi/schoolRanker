import random

#This program will generate random data about students at a university
#Will generate 100 data enteries 

nameList = ["Cats", "Pizza", "Gaming","C4lg4ry","Monkey", "Dogs", "Mars","P-72","Pp"]
universityName = "University of " + random.choice(nameList)


#Data format: studentID, High school, GPA
i = 0

while i < 100:
    studentID = random.randint(1111,9999)
    highschoolName = random.choice(nameList) + " High School"
    gpa =  round(random.uniform(0.0, 4.0),1)
    dataEntry = str(studentID)+str(i) +" "+ highschoolName +" "+ str(gpa) #appending i to the ID will make sure it's unique
    print(dataEntry)
    i+=1

