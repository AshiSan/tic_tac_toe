board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
print("")
count = 0 

def Feld(x):
    for row in x:
        for element in row:
            print(f"| {element} | ", end="")
        print("")

def zeichen_setzen(spieler, zeichen):
    for i in range(3):
        for j in range(3):
            if board[i][j] == spieler_input:
                board[i][j] = zeichen
                
    if bool == False:
    print("")
    print("DEINE ZAHL MUSS ZWISCHEN 1-9 LIEGEN !!!")


while count != 9:
    Feld(board)
    print("")

    spieler_input = int(input("X ist am Zug. Auf welche Zahl möchtest du dein Zeichen setzen? "))
    zeichen_setzen(spieler_input, "X")
    count += 1

    Feld(board)
    print("")

    if count == 9:
        break

    spieler_input = int(input("O ist am Zug. Auf welche Zahl möchtest du dein Zeichen setzen? "))
    zeichen_setzen(spieler_input, "O")
    count += 1
