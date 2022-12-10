#Programmers lv.0, 캐릭터의 좌표
def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == "left" and answer[0] > -(board[0]//2):
            answer[0] -= 1
        if i == "right" and answer[0] < (board[0]//2):
            answer[0] += 1
        if i == "up" and answer[1] < (board[1]//2):
            answer[1] += 1
        if i == "down" and answer[1] > -(board[1]//2):
            answer[1] -= 1       
    return answer