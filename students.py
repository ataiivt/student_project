students = []

def add_student(name):
    if not name:
        return "Ошибка: имя не указано"

    students.append(name)
    return "Студент добавлен"