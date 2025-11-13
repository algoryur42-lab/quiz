from generate_questions import question_generation
import json
from time import sleep
from random import randint
import threading

def timer_30s():
	sleep(30)
	print('\nВремя вышло!')
	flag = True

question_generation()

with open('questions.json', 'r', encoding ='utf-8') as f:
	quiz_questions = json.load(f)

print('Добро пожаловать на викторину!\nНа каждый вопрос выделяется 30 секунд, если вы не успели ответить за выделенное время, вопрос пропускается.')
input('Нажмите на любую клавишу для начала викторины:')
score = 0
total = 0
for question in quiz_questions:
	total += question['points']
	t = threading.Thread(target=timer_30s)
	print(f"Категория вопроса: {question['category']}")
	print(question['question'])
	for i, option in enumerate(question['options'],1):
		print(f"{i}. {option}")
	t.start()
	while True:
		try:
			if int(input('Введите вариант ответа:'))-1 == question['correct_answer']:
				score += question['points']
			break
		except ValueError:
			print('Пожалуйста введите только номер правильного варианта ответа!')
print(f'Вы набрали {score} очков из {total}')