Algorithm

1:- display board
    first players move
2:- get input of position
3:- check input position empty or not for input
4:- if board position empty: insert into board
        if check for winner==True return You won
        else 
            check board empty or not
            if empty:- goto step 2 with computer chance:
                again check for winner
                if check for winner==True return You Loose  
            else: 
                if:-  check for winner player ==True return You won
                if:-  check for winner computer== True return You Loose
                else:-  return Tie
