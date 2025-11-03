students = ["Amir" , "Sarah" , "Tom" , "Aisha" , "Leo"] # declares initial list
students.append("John")
students.append("Roger") # adds 2 students to the end of the list
students.remove("Amir") # removes specified student
students.insert(0,"Garry") # adds garry to the start of the list
sortedStudents = students.sort() # sorts the list alphabetically
print(f"Current students: {students}")