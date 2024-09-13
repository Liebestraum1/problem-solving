def solution(m, musicinfos):
    answer = []
    flat = {'C#':'1', 'D#':'2', 'F#':'3', 'G#':'4', 'A#':'5'}
    for note, change in flat.items():
        m = m.replace(note, change)
        for i in range(len(musicinfos)):
            musicinfos[i] = musicinfos[i].replace(note, change)
    for music in musicinfos:
        info = music.split(',')
        playtime = (int(info[1][:2]) * 60 + int(info[1][3:])) - (int(info[0][:2]) * 60 + int(info[0][3:]))
        played = (info[3] * (playtime // len(info[3]) + 1))[:playtime+1]
        print(m, played)
        if m in played:
            answer.append((playtime, info[2]))
    return max(answer, key = lambda x: x[0])[1] if answer else '(None)'