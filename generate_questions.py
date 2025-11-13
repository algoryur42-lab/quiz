import json

quiz_questions = [
    {
        "question": "Какая планета Солнечной системы является самой крупной?",
        "options": ["Марс", "Юпитер", "Сатурн", "Венера"],
        "correct_answer": 1,
        "points": 5,
        "category": "Астрономия"
    },
    {
        "question": "Столицей какой страны является город Оттава?",
        "options": ["США", "Канада", "Австралия", "Великобритания"],
        "correct_answer": 1,
        "points": 3,
        "category": "География"
    },
    {
        "question": "Какой оператор в Python используется для целочисленного деления?",
        "options": ["/", "//", "%", "**"],
        "correct_answer": 1,
        "points": 7,
        "category": "Программирование"
    },
    {
        "question": "Кто написал роман 'Преступление и наказание'?",
        "options": ["Лев Толстой", "Фёдор Достоевский", "Антон Чехов", "Иван Тургенев"],
        "correct_answer": 1,
        "points": 4,
        "category": "Литература"
    },
    {
        "question": "Какая функция в Python используется для вывода текста в консоль?",
        "options": ["print()", "input()", "output()", "console()"],
        "correct_answer": 0,
        "points": 6,
        "category": "Программирование"
    },
    {
        "question": "Какой химический элемент обозначается символом 'Au'?",
        "options": ["Серебро", "Алюминий", "Золото", "Аргон"],
        "correct_answer": 2,
        "points": 4,
        "category": "Химия"
    },
    {
        "question": "Какое ключевое слово используется для создания функции в Python?",
        "options": ["function", "def", "func", "define"],
        "correct_answer": 1,
        "points": 8,
        "category": "Программирование"
    },
    {
        "question": "В каком году произошла Великая Октябрьская социалистическая революция?",
        "options": ["1905", "1914", "1917", "1922"],
        "correct_answer": 2,
        "points": 5,
        "category": "История"
    },
    {
        "question": "Какой метод используется для добавления элемента в конец списка в Python?",
        "options": ["append()", "add()", "insert()", "push()"],
        "correct_answer": 0,
        "points": 7,
        "category": "Программирование"
    },
    {
        "question": "Какое животное является самым быстрым на суше?",
        "options": ["Гепард", "Лев", "Антилопа", "Леопард"],
        "correct_answer": 0,
        "points": 3,
        "category": "Биология"
    }
]
def question_generation():
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(quiz_questions, f, ensure_ascii=False, indent=2)