def solution(numbers):
    for i in range(len(numbers)):
        bn = format(numbers[i], 'b')
        if bn.rfind('0') in (len(bn)-1, len(bn)-2):
            numbers[i] += 1
        elif bn.rfind('0') == -1:
            numbers[i] += 2**len(bn) - 2**(len(bn)-1)
        else:
            numbers[i] += 2 ** (len(bn) - bn.rfind('0')-1) - 2**(len(bn) - bn.rfind('0') - 2)
    return numbers