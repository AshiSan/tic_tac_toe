board = [[7, 8, 9], 
         [4, 5, 6], 
         [1, 2, 3]]

print("")
count = 0 

def Feld(x):
    for row in x:
        for element in row:
            print(f"| {element} | ", end="")
        print("")

def zeichen_setzen(spieler, zeichen):
    bool = False

    for i in range(3):
        for j in range(3):
            if board[i][j] == spieler_input:
                board[i][j] = zeichen
                return True

    if bool == False:
        print("")
        print("DU MUSST EINE GANZZAHL ZWISCHEN 1-9 EINGEBEN !!!")

def won(player):
    global count

    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            print(f"{player} won!")
            count = 9
            return True

        if set(board[i]) == {player}:
            print(f"{player} won!")
            count = 9
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(f"{player} won!")
        count = 9
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"{player} won!")
        count = 9
        return True 


while count != 9:
    Feld(board)
    print("")
    if won("O"):
        break

    spieler_input = int(input("X ist am Zug. Auf welche Zahl möchtest du dein Zeichen setzen? "))
    zeichen_setzen(spieler_input, "X")
    count += 1

    Feld(board)
    print("")
    if won("X"):
        break

    if count == 9:
        break

    spieler_input = int(input("O ist am Zug. Auf welche Zahl möchtest du dein Zeichen setzen? "))
    zeichen_setzen(spieler_input, "O")
    count += 1


