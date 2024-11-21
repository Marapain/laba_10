# Автор: Клепач_Костянтин
# Опис: Ця програма створює текстовий файл, записує в нього своє прізвище та питання,
#       а також реалізує обробку виключних ситуацій під час роботи з файлами.

def write_question_to_file(file_name, surname, question):
    """
    Записує в файл прізвище та питання.
    :param file_name: Ім'я файлу для запису.
    :param surname: Прізвище автора питання.
    :param question: Питання, яке треба записати.
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Прізвище: {surname}\n")
            file.write(f"Питання: {question}\n")
        print(f"Дані успішно записано у файл: {file_name}")
    except Exception as e:
        print(f"Помилка під час запису у файл: {e}")

# Виклик функції для створення файлу та запису даних
file_name = "student_questions.txt"
surname = "Іваненко"
question = "Як працює функція open() у Python? Наведіть приклад із параметрами режиму роботи."
write_question_to_file(file_name, surname, question)

# Читання створеного файлу для перевірки
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        print("\nВміст файлу:")
        print(file.read())
except FileNotFoundError:
    print(f"Файл {file_name} не знайдено.")
except Exception as e:
    print(f"Помилка під час читання файлу: {e}")
