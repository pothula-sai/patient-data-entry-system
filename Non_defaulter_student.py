student_data = {1:'sai',2:'ram', 3:'shiva', 4:'push', 5:'krish', 6:'ramu', 7:'rahul', 8: 'pocso',9:'king',10:'happy'}

defaulter_students = ["shiva", "krish", "rahul"]



non_defaulter_students = {}

for student_id,student_name in student_data.items():
    if student_name not in defaulter_students:
        non_defaulter_students[student_id] = [student_name]
print("non_defaulter_students:", non_defaulter_students)
