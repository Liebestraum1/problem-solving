def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        cd, cp = cap, cap
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        distance = max(len(deliveries), len(pickups))
        answer += 2 * distance
        for i in range(len(deliveries)-1, -1, -1):
            if cd == 0:
                break
            if cd >= deliveries[i]:
                cd -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= cd
                cd = 0
        for i in range(len(pickups)-1, -1, -1):
            if cp == 0:
                break
            if cp >= pickups[i]:
                cp -= pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= cp
                cp = 0
    return answer