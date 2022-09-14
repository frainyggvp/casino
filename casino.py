import random, time

balance = int(1000)
games_played = int(0)
wins = 0
def print_stats(): # информация
	print("Игр сыграно:", games_played, "\nПобед:", wins, "\nВаш баланс:", balance)

def choose_game(): # выбор игры
	print("Доступные игры:")
	time.sleep(0.5)
	print("-РУЛЕТКА (1) \n-ОДНОРУКИЙ БАНДИТ (2)")
	choise=input("Выберите игру: ")
	if choise == "1":
		lottery()
	elif choise == "2":
		slot_machine()
	else:
		print("Неверный ввод. Напишите индекс необходимой игры")
		time.sleep(1)
		choose_game()

def lottery(): # игра лотерея
	global balance, games_played, wins
	ticket = int(input("Введите целое число от 0 до 36: "))

	if isinstance(ticket, str): # проверка валидности ввода и сама игра
		print("Необходимо ввести число от 0 до 36!")
		lottery()
	elif ticket > 36:
		print("Необходимо ввести целое число от 0 до 36!")
		lottery()
	elif ticket < 0:
		print("Необходимо ввести целое число от 0 до 36!")
		lottery()

	bet = int(input("Введите вашу ставку: "))

	if bet > balance: # проверка баланса
		print("Недостаточно средств на балансе!")
		lottery()
	elif bet < 0:
		print("Вы серьёзно?")
		lottery()
	else:
		games_played = games_played + 1
		print("Отлично, крутим рулетку...")
		time.sleep(1)
		winticket = random.randint(0, 36)
		print("Выпало число", winticket)
		time.sleep(1)
		if winticket == ticket:
			balance = balance + bet * 36
			print("Победа! Ваше число совпало с выигрышным. На баланс поступило", (bet * 36), "рублей\n")
			wins = wins + 1
			print_stats()
			choose_game()
		else:
			balance = balance - bet
			print("Неудача! Ваше число не совпало с выигрышным. С баланса снято", (bet), "рублей\n")
			print_stats()
			choose_game()

def slot_machine(): # однорукий бандит
	global balance, games_played, wins

	bet = int(input("Введите вашу ставку: "))

	if bet > balance: # проверка баланса
		print("Недостаточно средств на балансе!")
		slot_machine()
	elif bet < 0:
		print("Вы серьёзно?")
		slot_machine()
	else:
		int1 = random.randint(1, 9)
		int2 = random.randint(1, 9)
		int3 = random.randint(1, 9)
		time.sleep(1)

	print(int1, int2, int3)
	time.sleep(1)
	if int1 == int2 == int3:
		games_played = games_played + 1
		print("Победа! Все 3 цифры совпали. На баланс поступило", (bet * 100), "рублей")
		wins = wins + 1
		balance = balance + bet * 100
		print_stats()
		choose_game()
	else:
		games_played = games_played + 1
		print("Неудача! Цифры не совпали. С баланса снято", (bet), "рублей")
		balance = balance - bet
		print_stats()
		choose_game()

if __name__ == "__main__": # точка входа
	print("Добро пожаловать в Python-казино! (by fra1ny)")
	time.sleep(1)
	print_stats()
	choose_game()
	input()