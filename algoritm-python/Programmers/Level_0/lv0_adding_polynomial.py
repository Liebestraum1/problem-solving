#Programmers lv.0, 다항식 더하기
def solution(polynomial):
    answer = polynomial.split(" + ")
    figures = 0
    constant = 0
    for i in answer:
        if "x" in i:
            if i[0] == "x":
                figures += 1
            else:
                figures += int(i.rstrip("x"))
        else:
            constant += int(i)
    
    if figures == 0:
        return str(constant)
    elif figures == 1:
        return ("x" + " + " + str(constant)).replace(" + 0", "")
    else:
        return (str(figures) + "x" + " + " + str(constant)).replace(" + 0", "")