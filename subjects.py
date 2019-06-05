#This file is used to add questions for specified subjects by the Teacher.
import os
print("------------------Welcome To Automatic Question Paper Generation System----------------------")
print("---------------------------------------------------------------------------------------------")
print("            ----------Instructions For Entering Questions In Database-------                 ")
print("Type the question and end it with either '?' and '.' followed by double_colon '::' as seperator to choose the category of question .")
print("Category is defined as --> 'E'-Easy  , 'M'-Medium  and 'H'-Hard questions.")
print("Example : --> 'What do you mean by IP ?::E' ")
print("---------------------------------------------------------------------------------------------")
print("Enter the Subject Name. eg: 'Operating System'")
subject_name=input().upper()+".txt"
file_name=os.getcwd()+"\\Subjects\\"+subject_name
print(file_name)
file=open(file_name,"a+")
with open(file_name,"r") as file1:
    data = file1.read().split("\n")
print("Do you want to enter more questions? Yes/No")
choice=input().upper()
while(choice=="YES"):
	print("Enter Question?")
	quest=input()
	if quest in data:
		print("Question Already Present ! Enter a different Question.")
		continue;
	else:
		quest=quest+"\n"
		file.write(quest)
	print("Do you want to enter more questions? Yes/No")
	choice=input().upper()
print("Questions Submitted Successfully.")