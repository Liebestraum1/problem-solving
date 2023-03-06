def solution(wallpaper):
    lux, luy, rdx, rdy = 51, 51, 0, 0
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if wallpaper[row][col] == '#':
                lux = min(lux, row)
                rdx = max(rdx, row)
                luy = min(luy, col)
                rdy = max(rdy, col)
    return [lux, luy, rdx+1, rdy+1]