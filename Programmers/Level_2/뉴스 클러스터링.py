def solution(str1, str2):
    list1 = [(str1[i] + str1[i+1]).lower() for i in range(len(str1)-1) if (str1[i] + str1[i+1]).isalpha()]
    list2 = [(str2[i] + str2[i+1]).lower() for i in range(len(str2)-1) if (str2[i] + str2[i+1]).isalpha()]
    
    uni, inter = 0, 0
    
    for i in set(list1 + list2):
        uni += max(list1.count(i), list2.count(i))
        inter += min(list1.count(i), list2.count(i))
    return int(inter/uni * 65536) if uni else 65536