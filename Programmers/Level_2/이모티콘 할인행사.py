from itertools import product

def solution(users, emoticons):
    answer = []
    all_discount_rate_list = [tuple(p) for p in product([0.1, 0.2, 0.3, 0.4], repeat = len(emoticons))]
    
    for discount_rate_list in all_discount_rate_list:
        subscribers, sales = 0, 0
        for user_purchase_basline, user_subscribe_baseline in users:
            user_purchase_amount = 0
            for discount_rate, price_of_emoticon in zip(discount_rate_list, emoticons):
                if user_purchase_basline/100 <= discount_rate:
                    user_purchase_amount += (1-discount_rate) * price_of_emoticon
            if user_purchase_amount >= user_subscribe_baseline:
                subscribers += 1
            else:
                sales += user_purchase_amount
        answer.append([subscribers, sales])
    return max(answer, key=lambda x: (x[0], x[1]))