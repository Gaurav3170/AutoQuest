#This file is used to generate question paper of specified subjects. 
import fpdf
import random
import os
pdf=fpdf.FPDF(format='letter')
def pdfgen(list1,list2,list3,subject,SessionYear,subject_code,semester):
    pdf.add_page()
    pdf.set_font("Arial",'b', size=14)
    pdf.cell(200,10,"United College Of Engineering And Research,Allahabad", ln=1, align="C")
    pdf.set_font("Arial", size=13)
    pdf.cell(200,10,"B.Tech ("+semester+" Semester ("+SessionYear+"))", ln=1, align="C")
    pdf.set_font("Arial",'b', size=13)
    pdf.cell(200,10,subject+"("+subject_code+")", ln=1, align="C")
    pdf.set_font("Times", size=10)
    pdf.cell(167,10,"Max Marks : 30", align="left")
    pdf.cell(100,10,"Time : 3 Hours",ln=1, align="right")
    pdf.set_font("Times", size=10)
    pdf.cell(100,10,"Note: There are three sections in this paper . All sections are compulsory.",ln=1, align="left")
    pdf.set_font("Arial",'b', size=13)
    pdf.cell(134,10,"Section A", align="left")
    pdf.set_font("Arial",'i', size=11)
    pdf.cell(100,10,"Max marks for this section are 10",ln=1, align="left")
    pdf.set_font("Arial",'b', size=10)
    pdf.cell(100,10,"Attempt ALL Questions.",ln=1, align="left")
    pdf.set_font("Arial", size=10)
    for i in range(10):
        c=len(list1[i])
        ans=90
        if(c>90):
            for index in range(90,c):
                if(list1[i][index]==' '):
                    ans=index
                    break
            t1=list1[i][0:ans]
            t2=list1[i][ans:]
            pdf.cell(170,6,"Q"+str(i+1)+": "+t1,ln=1,align="left")
            pdf.cell(170,6,"     "+t2,ln=1,align="left")
        else:
            pdf.cell(170,6,"Q"+str(i+1)+": "+list1[i],ln=1,align="left")
    pdf.set_font("Arial",'b', size=13)
    pdf.cell(134,15,"Section B", align="left")
    pdf.set_font("Times",'i', size=11)
    pdf.cell(100,15,"Max marks for this section are 12",ln=1, align="left")
    pdf.set_font("Arial",'b', size=10)
    pdf.cell(100,10,"Attempt any FOUR Questions.",ln=1, align="left")
    pdf.set_font("Arial", size=10)
    for i in range(6):
        c=len(list2[i])
        ans=90
        if(c>90):
            for index in range(90,c):
                if(list2[i][index]==' '):
                    ans=index
                    break
            t1=list2[i][0:ans]
            t2=list2[i][ans:]
            pdf.cell(170,6,"Q"+str(i+1)+": "+t1,ln=1,align="left")
            pdf.cell(170,6,"     "+t2,ln=1,align="left")
        else:
            pdf.cell(170,6,"Q"+str(i+1)+": "+list2[i],ln=1,align="left")
    pdf.set_font("Arial",'b', size=13)
    pdf.cell(133,15,"Section C", align="left")
    pdf.set_font("Times",'i', size=11)
    pdf.cell(100,15,"Max marks for this section are 8",ln=1, align="left")
    pdf.set_font("Arial",'b', size=10)
    pdf.cell(100,10,"Attempt any TWO Questions.",ln=1, align="left")
    pdf.set_font("Arial", size=10)
    for i in range(3):
        c=len(list3[i])
        ans=90
        if(c>90):
            for index in range(90,c):
                if(list3[i][index]==' '):
                    ans=index
                    break
            t1=list3[i][0:ans]
            t2=list3[i][ans:]
            pdf.cell(170,6,"Q"+str(i+1)+": "+t1,ln=1,align="left")
            pdf.cell(170,6,"     "+t2,ln=1,align="left")
        else:
            pdf.cell(170,6,"Q"+str(i+1)+": "+list3[i],ln=1,align="left")
    pdf.output("final1.pdf")
print("Enter the Subject Name for which you want to generate question paper?")
subject=input().upper()
section_a=list()
section_b=list()
section_c=list()
list1=[]
list2=[]
list3=[]
file_name=os.getcwd()+"\\Subjects\\"+subject+".txt"
try:
    with open(file_name,'r') as file:
        data = file.read().split("\n")
except:
    print("File does not exists! Please make questions list of the subject first .")
    exit()
print(data)
for inputs in data:
    inp=inputs.split("::")
    question=inp[0]
    category=inp[1]
    if(category=='E'):
        section_a.append(question)
    elif(category=='M'):
        section_b.append(question)
    else:
        section_c.append(question)
if(len(section_a)<10 or len(section_b)<6 or len(section_c)<3):
    print("Please enter atleast 10 questions of Easy Category, 6 Questions of Medium Category and 4 Questions of Hard Category!")
else:
    output_text_name=os.getcwd()+"\\Subjects\\"+subject+" Question Paper.txt"
    f = open(output_text_name,'w')
    print("Enter the Subject Code?")
    subject_code=input().upper()
    print("Enter the Semester and SessionYear seperated by double_colon(::) . eg: 5::2018-2019 ")
    input_s=input().split("::")
    semester=input_s[0]
    SessionYear=input_s[1]
    firstLine="----------------------------------------------"+SessionYear+"----------------------------------------------\n"
    secondLine="----------------------------------------"+subject+" "+subject_code+"-----------------------M.M=30-------\n"
    thirdLine="----------------------------------------------Semester-"+semester+"---------------------------------------------\n"
    f.write(firstLine)
    f.write(secondLine)
    f.write(thirdLine)
    f.write("__SECTION A__:(Attempt All Questions) \n")
    count=1
    length=len(section_a)
    list_range=random.sample(range(0,length),10)
    for x in list_range:
        list1.append(section_a[x])
        temp_str=(str)(count)+")"+section_a[x]+"    [1]\n"
        f.write(temp_str)
        count+=1
    f.write("\n__SECTION B__:(Attempt any 4 Questions) \n")
    count=1
    length=len(section_b)
    list_range=random.sample(range(0,length),6)
    for x in list_range:
        list2.append(section_b[x])
        temp_str=(str)(count)+")"+section_b[x]+"    [3]\n"
        f.write(temp_str)
        count+=1
    f.write("\n__SECTION C__:(Attempt any 2 Questions) \n")
    count=1
    length=len(section_c)
    list_range=random.sample(range(0,length),3)
    for x in list_range:
        list3.append(section_c[x])
        temp_str=(str)(count)+")"+section_c[x]+"    [4]\n"
        f.write(temp_str)
        count+=1
    f.write("------------------------------------------------The End----------------------------------------------\n")
    f.close()
    pdfgen(list1,list2,list3,subject,SessionYear,subject_code,semester)
file.close()