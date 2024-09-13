import re
def solution(files):
    return sorted(files, key = lambda x:
        (re.split("[0-9]", x)[0].lower(),
        int(re.findall("[0-9]+", x)[0])))