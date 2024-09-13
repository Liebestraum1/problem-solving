def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    for city in cities:
        if city in cache:
            answer += 1
            cache.append(city)
            cache.remove(city)
        else:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
            answer += 5
    return answer