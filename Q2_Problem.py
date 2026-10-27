marks1 = int(input("Enter subject 1 marks: "))
marks2 = int(input("Enter subject 2 marks: "))
marks3 = int(input("Enter subject 3 marks: "))

Total_percentange = (marks1+marks2+marks3)/3

if(marks1>=33 and marks2>=33 and marks3>=33 and Total_percentange>=40):
    print("Congratulations, You Passed!")
else:
    print("Boohoo you failed")
