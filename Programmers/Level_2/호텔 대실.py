def solution(book_time):
    from heapq import heappop, heappush
    book = []
    stack = [0]
    for checkin, checkout in book_time:
        it = int(checkin[:2]) * 60 + int(checkin[3:])
        ot = int(checkout[:2]) * 60 + int(checkout[3:]) + 10
        book.append([it, ot])

    book.sort(key = lambda x: x[0])
    for checkin, checkout in book:
        if checkin >= stack[0]:
            heappop(stack)
        heappush(stack, checkout)
    return len(stack)