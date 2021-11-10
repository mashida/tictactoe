# глобальные константы
EX = "Х"
ZERO = "О"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def ask_yes_no(question):
    """Задает вопрос ответом "да" или "нет"."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет принадлежность первого хода."""
    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")
    if go_first == "y":
        print("\nHy что ж, даю тебе фору: играй крестиками.")
        human = EX
        computer = ZERO
    else:
        print("\nTвoя удаль тебя погубит... Буду начинать я.")
        computer = EX
        human = ZERO
    return computer, human


def new_board():
    """Создает новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """создает список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            result = board[row[0]]
            return result
        if EMPTY not in board:
            return TIE
    return None


def human_move(board):
    """Получает ход человека."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Tвoй ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nCмeшнoй человек! Это поле уже занято. Выбери дpyroe.\n")
    print("Ладно ... ")
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    # создадим рабочую копию доски. потому что функuия будет менять некоторые значения в списке
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        # если следующим ходом может победить компьютер. выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
        # выполнив проверку. отменим внесенные изменения
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        # если следующим ходом может победить человек. блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
        # выполнив проверку. отменим внесенные изменения
        board[move] = EMPTY
    # поскольку следующим ходом ни одна сторона не может победить.
    # выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


#  Эта функция используется для того, чтобы чередовать ходы по мере того, как игроки будут их совершать.
def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == EX:
        return ZERO
    else:
        return EX


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры."""
    if the_winner != TIE:
        print("Tpи", the_winner, " в ряд!\n")
    else:
        print("Hичья!\n")
    if the_winner == computer:
        print("хахаха! я крут!")
    elif the_winner == human:
        print(
            "O нет. этого не может быть! Неужели ты как-то сумел перехитрить меня, белковый? \n" 
            "Клянусь: я, компьютер, не допущу этого больше никогда!")
    elif the_winner == TIE:
        print(
            "Teбe несказанно повезло. дружок: ты сумел свести игру вничью. \n"
            "Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить. ")
