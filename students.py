# students.py
from data_store import students

def add_student(id, name, department, grade, clubs):
    if id in students:
        print("Bu ID zaten mevcut.")
        return

    students[id] = {
        "name": name,
        "department": department,
        "grade": grade,
        "clubs": set(clubs),
        "events": set()
    }

    print(f"{id} numaralı öğrenci eklendi.")

def remove_student(id):
    if id not in students:
        print("Öğrenci bulunamadı.")
        return

    del students[id]
    print(f"{id} numaralı öğrenci silindi.")

def get_student(id):
    return students.get(id)

def list_students():
    return list(students.values())
