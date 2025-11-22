from generate_questions import question_generation
import json
from random import randint
from inputimeout import inputimeout, TimeoutOccurred
import time
import os

def delete_lines(n=1):
    for _ in range(n):
        print('\033[1A\033[2K', end='')  # вверх + очистить
    print('\r', end='')

def clear_console():
    """Очищает консоль для Windows, Linux и macOS"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, Unix
        os.system('clear')

question_generation()

with open('questions.json', 'r', encoding ='utf-8') as f:
	quiz_questions = json.load(f)

try:
    with open('quiz_results.json', 'r', encoding ='utf-8') as res:
	    quiz_results = json.load(res)
except FileNotFoundError:
    quiz_results = []    

print('Добро пожаловать на викторину!\nНа каждый вопрос выделяется 15 секунд, если вы не успели ответить за выделенное время, вопрос пропускается.')
name = input('Введите имя:')
clear_console()
for i in range(3, 0, -1):
    print(f'Викторина начнётся через {i}')
    time.sleep(1)
    clear_console()
print("Викторина началась!!!")
time.sleep(0.5)
clear_console()
score = 0
total = 0
begin = time.time()
for question in quiz_questions:
    total += question['points']
    print(f"Категория вопроса: {question['category']}")
    print(question['question'])
    for i, option in enumerate(question['options'],1):
        print(f"{i}. {option}")
    start = time.time()
    while True:
        try:
            answer = inputimeout(prompt='Введите номер ответа:',timeout=15-int(time.time()-start))
            if int(answer) - 1 == question['correct_answer']:
                score += question['points']
                print("\n✅ Правильно!")
            else:
                print(f"\n❌ Неправильно. Правильный ответ: {question['correct_answer'] + 1}")
            break
        except ValueError:
            delete_lines()
            print('Пожалуйста введите только номер ответа.')
            time.sleep(1)
            delete_lines()
        except TimeoutOccurred:
            print(f'\n⏰ Время вышло. Правильный ответ: {question['correct_answer'] + 1}')
            break

    time.sleep(1.5)
    clear_console()
time_spent = round(time.time()-begin, 1)
print(f'\nВы набрали {score} очков из {total}')
print(f'Общее время прохождения викторины: {time_spent}')

data_result = {'name':name, 'score':score, 'time_spent':time_spent}

quiz_results.append(data_result)

sorted_results = sorted(quiz_results, key=lambda x: (-x['score'], x['time_spent']))

from tabulate import tabulate
print('Таблица с результатами:')
print(tabulate(sorted_results, headers="keys", tablefmt="grid"))

with open('quiz_results.json', 'w', encoding='utf-8') as res:
    json.dump(sorted_results, res, ensure_ascii=False, indent=2)