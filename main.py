# Крестики-нолики
# Компьютер играет в крестики-нолики против пользователя

# вывести на экран инструкции для игрока
# решить, кому принадлежит первый ход
# создать пустую доску для игры в "Крестики-нолики"
# отобразить эту доску
# до тех пор пока никто не выиграл или не состоялась ничья
# если сейчас ход пользователя
# получить ход из пользовательского ввода
# изменить вид доски
# иначе
# рассчитать ход компьютера
# изменить вид доски
# вывести на экран обновленный вид доски
# осуществить переход хода
# поздравить победителя или констатитровать ничью

from functions import *
# импорт функций
# насколько верно я вызвал функцию из другого файла?
from manual import manual


def main() -> None:
    # основная часть
    print("Этo инструкция для игры в 'Крестики-нолики':")
    print(f"{manual}")
    computer, human = pieces()
    turn = EX
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    input("\n\nHaжмитe Enter. чтобы выйти.")


if __name__ == '__main__':
    main()
