# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SNbTXEflQPbPndA8GPBRE9rbnQfpB6OT
"""

# Student Grades Management System

# def Graded():
Students = {}
def Add_Std(name , grade):
  Students[name] = float(grade)
  print(Students)
  print('----------------------------------------------------------')
  print('----------Student Added Successfully----------------------')
  print('----------------------------------------------------------')
  main()

def View_Grades():
    if not Students:
        print("No student records found.")
    else:
        print("\nStudent : Grades ")
        for name, grade in Students.items():
            print(f"{name}: {grade}")
    print('----------------------------------------------------------')
    main()


def Calculate_Avg():
    if Students:
        average = sum(Students.values()) / len(Students)
        print(f"\nThe average grade is: {average:.2f}")
    else:
        print("No student records found.")
    print('----------------------------------------------------------')





def View_Above_Avg():
    if Students:
        avg = sum(Students.values()) / len(Students)
        above_avg = [name for name, grade in Students.items() if grade > avg]
        print("\nStudents with grades above average:" if above_avg else "No students have grades above average.")
        print("\n".join(above_avg) if above_avg else "")
    else:
        print("No student records found.")
    print('----------------------------------------------------------')
    main()


def View_Below_Avg():
    """Function to display students with grades below average."""
    if not Students:
        print("No student records found.")
    else:
        avg = sum(Students.values()) / len(Students)
        below_avg = [name for name, grade in Students.items() if grade < avg]
        if below_avg:
            print("\nStudents with grades below average:")
            for student in below_avg:
                print(student)
        else:
            print("No students have grades below average.")
    print('----------------------------------------------------------')


def main():
    print('----------------------------------------------------------')
    print('---------Welcome To Student Grades Management System------')
    print('----------------------------------------------------------')
    print(' Press 1 to Add Student \n Press 2 to View all student grades \n Press 3 to Calculate average grade \n Press 4 to View students above average \n Press 5 to  View students below average \n press 6 Exit')
    print('----------------------------------------------------------')
    user_Select = input()
    if user_Select == '1':
      print('Enter Student Name :')
      name = input()
      print('Enter Student Grade :')
      grade = input()
      Add_Std(name , grade)

    elif user_Select == '2':
      View_Grades()

    elif user_Select == '3':
      Calculate_Avg()

    elif user_Select == '4':
      View_Above_Avg()

    elif user_Select == '5':
      View_Below_Avg()

    elif user_Select == '6':
      print("-------------Exiting the system. Goodbye!-----------------")
      return
    else:
      print("Invalid choice. Please select a valid option (1-6).")
main()

