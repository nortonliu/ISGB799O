import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
# Read the file by pandas
data=pd.read_csv("Students.txt",sep="\t")

instruction=("""Welcome to student system. Enter \"1,2,3,4,5,6,7\" to excute:
1. Display all student records
2. Display students whose last name begins with a certain string (case insensitive)
3. Display all records for students whose graduating year is a certain year
4. Display a summary report of number and percent of students in each program, for students graduating on/after a certain year
5. Display students whose last name includes a certain string (case sensitive)
6. Quit
7. Show instruction
      """)
# Show the menu
print(instruction)

# Keep the instance of the data in memory for the duration of the program
# Not re-read the data from the file for each user query.
while True:
    # Enter order
    order=str(input("Please enter the order: ")).lower()
    # On after for the graduation year
    year=set()
    for i in data.GradYear:
        year.add(i)
    if order=="1":
    # Show all data
        print(data)
    elif order=="2":
    #  Find last name begin with certain letters (case insensitive)
        Name=str(input("please input last name with a certain string: "))
        # more than 1 initial character
        if len(Name) > 1:
            Name = (Name[0].upper() + Name[1:].lower()).replace(" ", "")
        # Initial character only
        else:
            Name = Name.upper()
        if True in list(data.Last.str.contains(Name)):
            print(data[data.Last.str.contains(Name)])
        else:
            print("No record")
    elif order=="3":
    # Year summary report 1
        Grad_year=int(input("Please enter the year you want to check: "))
        if Grad_year in year:
                print(data[data.GradYear==Grad_year])
        else:
                print("No record found")
    elif order=="4":
    # Year summary report 2
        Year=int(input("Please enter the year you want to check: "))
        if Year in year:
            # Set a data frame by the graduation frequency
            frame1=pd.DataFrame(data[data.GradYear==Year].DegreeProgram.value_counts(normalize=True))
            frame1.columns=["Frequency"]
            # Turn graduation frequency to percentage
            frame1["Frequency"] = frame1["Frequency"].apply(lambda x: format(x, '.2%'))
            # Set another data frame by the real student amount
            frame2=pd.DataFrame(data[data.GradYear==Year].DegreeProgram.value_counts())
            frame2.columns=["Number"]
            # Combine 2 data frames together
            frame = frame1.join(frame2)
            print(frame)
            # Additional Function: press Y or y can show the pie chart
            chart=str(input("Do you want to see pie chart?(Y/N)")).upper()
            if chart=="Y":
                labels = list(frame.index)
                sizes = list(frame["Number"])
                plt.pie(sizes, labels=labels, autopct='%1.1f%%')
                # Title shows the exact year
                plt.title('Pie Chart on/after ' + str(Year))
                plt.axis('equal')
                plt.show()
        else:
            # Year is not included
            print("Wrong year")
    elif order == "5":
        # Additional Function: Find student if the last name include the input (case sensitive)
        Name=str(input("please input last name with a certain string: "))
        # Just include in the name
        if True in list(data.Last.str.contains(Name)):
            print(data[data.Last.str.contains(Name)])
        else:
            print("No record")
    elif order=="6":
        # Quit the SQT
        break
    elif order=="7":
        # Show the menu again
        print(instruction)
    else:
        # Not enter between 1-7
        print("Wrong order. Enter 6 to see all instruction.")