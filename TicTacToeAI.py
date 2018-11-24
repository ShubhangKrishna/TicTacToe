

game=[0,1,2,3,4,5,6,7,8]
hu_player="X"
ai_player="O"
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

def wining (game,player):  

    if (game[0]==player and game[4]==player and game[8]==player) or (game[2] == player and game[4] == player and game[6] == player) or (game[0] == player and game[1] == player and game[2] == player) or  (game[3] == player and game[4] == player and game[5] == player) or (game[6] == player and game[7] == player and game[8] == player) or (game[0] == player and game[3] == player and game[6] == player) or (game[1] == player and game[4] == player and game[7] == player) or (game[3]==player and game[5]==player and game[8]==player):
        return True
    else: 
        return False  
    

def empty_indices(game):
    L=[]
    for i in range (0,len(game)):
        if (game[i]==""):
            L.append(i)

    return L
def minimax(game_in, player):
    game=game_in
    avail_spot=empty_indices(game)
    score=-1
    if wining(game,hu_player):
        score=-10
        return score

    elif wining(game,ai_player):
        score=10
        return score
    elif len(avail_spot)==0:
        return score
    

    moves=[]
    #print moves
    print avail_spot
    for i in range (0,len(avail_spot)):
        move={}
        #game[avail_spot[i]]=move[i]
        move[i]=game[avail_spot[i]]

        game[avail_spot[i]]=player

        if (player==ai_player):
            result =minimax(game,hu_player)
            move.score = result[score]

        game[avail_spot[i]]=move[i]

        moves.append(move)
    print game
    print moves
    best_move=-1

    if player==ai_player:
        best_score=-10000
        for i in range (0,len(moves)):
            if moves[i]>best_score:
                best_score=moves[i]
                best_move=i
    else:
        best_score=10000
        for i in range(0,len(moves)):
            if moves[i]<best_score:
                best_move=i


    return moves[best_move]



def print_board(game):
    print game[0]," | ",game[1]," | ",game[2]
    print "-----------"
    print game[3], " | ", game[4], " | ", game[5]
    print "-----------"
    print game[6], " | ", game[7], " | ", game[8]


def main(game):
    print_board(game)
    while game_status(game)==0:
        inp=input("Enter the position you want to enter in(1-9): ")
        game[inp-1]= hu_player
        ai_play=minimax(game,hu_player)
        if ai_play==-10: 
            print "Human Wins"
            break

        elif ai_play==-1: 
            print "Tie"
            break

        elif ai_play==10:
            print "Computer wins"
            break
        else:
            game[ai_play]=ai_player
            print_board(game)


main(game)