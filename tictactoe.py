p = [
    0,0,0,
    0,0,0,
    0,0,0
]

#0 if empty
#1 if cross
#2 if circle

def draw_grid():
    print(num2move(p[0])+"|"+num2move(p[1])+"|"+num2move(p[2]))
    print("  -------")
    print(num2move(p[3])+"|"+num2move(p[4])+"|"+num2move(p[5]))
    print("  -------")
    print(num2move(p[6])+"|"+num2move(p[7])+"|"+num2move(p[8]))

def num2move(num):
    match num:
        case 0:
            return "   "
        case 1:
            return " X "
        case 2:
            return " O "

draw_grid()