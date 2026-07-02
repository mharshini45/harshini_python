#host-IP address
#user-is the name that must be already exists in mysql or default as "root"
#password - that we enter while we open
#auth_plugin- the method mysql uses to verify you password
#cursor sends the sql commands from python to mysql and brings back the result
import mysql.connector as resume
mydb=resume.connect(host="localhost",user="root",password="Harshu@27",database="Resume1")

mycursor=mydb.cursor() 

Name=(input("enter the name:"))
Age=(input("enter your age:"))
Mobile_no=(input("enter your phone_no:"))
Designation=(input("enter your designation:"))

mycursor.execute("insert into register(Name,Age,Mobile_no,Designation)values(%s,%s,%s,%s)"
                 ,(Name,Age,Mobile_no,Designation))

mydb.commit()
print("value inserted successfully")
