import math

game=["","","","","","","","",""]

def game_status(game):
    count=0
    for i in range (9):
        if game[i]=="X":
            count+=1
        if game[i]=="O":
            count=0
        if count==3:
            return 1
    count=0
    for i in range(9):
        if game[i]=="O":
            count+=1
        if game[i]=="X":
            count=0
        if count==3:
            return 2

    if game[0]=="X" and game[4]=="X" and game[8]=="X":
        return 1
    if game[2] == "X" and game[4] == "X" and game[6] == "X":
        return 1
    if game[0] == "O" and game[4] == "O" and game[8] == "O":
        return 2
    if game[2] == "O" and game[4] == "O" and game[6] == "O":
        return 2

    return 0

def wining (game,player)
def empty_indices(game):
    L=[]
    for i in inage (0,len(game)):
        if (game[i]==""):
            L.append(i)

    return L
def minimax(game, plauer):
    avail_spot=empty_indices(game)

def print_board(game):
    print game[0]," | ",game[1]," | ",game[2]
    print "-----------"
    print game[3], " | ", game[4], " | ", game[5]
    print "-----------"
    print game[6], " | ", game[7], " | ", game[8]


def main(game):
    print_board(game)
    hu_player="X"
    ai_player="O"
    while game_status(game)==0:
        inp=input("Enter the position you want to enter in(1-9): ")
        game[inp-1]= hu_player



main(game)