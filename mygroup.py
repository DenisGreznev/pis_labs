groupmates = [
    {
        "name": "Анна",
        "surname": "Асеева",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Андрей",
        "surname": "Банчук",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Владимир",
        "surname": "Власов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Волков",
        "surname": "Вячеслав",
        "exams": ["Руссикий язык", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Грезнев",
        "surname": "Денис",
        "exams": ["Прикладные информационные системы", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15),
          u"Фамилия".ljust(10),
          u"Экзамены".ljust(30),
          u"Оценки".ljust(20),
          u"Средний балл".ljust(15))
    
    for student in students:
        # Рассчитываем средний балл для каждого студента
        avg_mark = sum(student["marks"]) / len(student["marks"])
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20),
              f"{avg_mark:.2f}".ljust(15))

def filter_students_by_average_mark(students, min_average_mark):

    # Фильтруем список студентов, оставляя только тех, средний балл которых выше заданного.
    filtered_students = []
    for student in students:
        # Рассчитываем средний балл
        average_mark = sum(student["marks"]) / len(student["marks"])
        # Проверяем, выше ли средний балл заданного порога
        if average_mark > min_average_mark:
            filtered_students.append(student)
    
    return filtered_students
    
print("Список всех студентов:")
print_students(groupmates)
print("-" * 100)

# Запрос порогового балла у пользователя
try:
    threshold = float(input("Введите минимальный средний балл для фильтрации: "))
except ValueError:
    print("Ошибка: Введено некорректное число.")
    # Используем значение по умолчанию, если ввод некорректен
    threshold = 4.0 

# Фильтрация и вывод результатов
filtered = filter_students_by_average_mark(groupmates, threshold)

print("-" * 100)
print(f"Студенты, средний балл которых выше {threshold}:")

if filtered:
    print_students(filtered)
else:
    print("Студенты, удовлетворяющие условию, не найдены.")
