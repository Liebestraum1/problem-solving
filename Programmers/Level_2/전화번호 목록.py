def solution(phone_book):
    h = set(phone_book)
    
    for i in phone_book:
        temp = ''
        for number in i[:-1]:
            temp += number
            if temp in h:
                return False
    return True