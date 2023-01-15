# 1. Напишите программу, удаляющая из текста все слова, содержащие "а" "б" "в"
#  I вариант пытался с работой через текстовый документ
# f = open ('text.txt', encoding='utf-8')
# f = f.split()
# for i in range(len(f)):
#     if f[i] == 'а' or f[i] == 'б' or f[i] == 'в':
#         del f[i]
# II вариант
# text = 'Как то летом на рассвете заглянул в соседский сад, там смуглянка молдованка собирает виноград'
# result = ' '.join(filter(lambda w: w[i] not in ["а", "б", "в"], text.split()))
# print(result)

# 3. Игра крестики-нолики на двоих

# print("*" * 10, "Игра Крестики-Нолики", "*" * 10)
# board = list(range(1,10))
# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0 + i *3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#         print("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+ "? ")
#         try:
#             player_answer = int(player_answer)
#         except: 
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#     if player_answer >= 1 and player_answer <= 9:
#         if (str(board[player_answer - 1]) not in "XO"):
#             board[player_answer - 1] = player_token
#             valid = True
#         else:
#             print("Эта клетка уже занята!")
#     else: 
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#     win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board [each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter %2 == 0:
#             take_input('X')
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "Выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# a = 'AACCBBBBBAAADDDDDDDD'
# print(a)
# result = ""
# count = 1
# for i in range(len(a)):
#     if i<len(a)-1 and a[i] == a[i+1]:
#         count+=1
#     else:
#         result += str(count) + a[i]
#         count = 1
# print(result)

