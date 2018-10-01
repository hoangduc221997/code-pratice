map_sokoban = { "x":5 , "y":5}
player = {"x":0, "y":4}
boxes = [
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3},
]

destination = [
    {"x":2,"y":1},
    {"x":3,"y":2},
    {"x":4,"y":3}
]
while True:
    for y in range (map_sokoban["y"]):
        for x in range (map_sokoban["x"]):
            box_is_here = False
            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    box_is_here = True
            des_is_here = False
            for des in destination:
                if des ['x'] == x and des['y'] == y:
                    des_is_here = True
            player_is_here = False
            if x == player ['x'] and y == player['y']:
                player_is_here = True

            if player_is_here:
                print("P",end="")
            elif box_is_here:
                print("B", end="")
            elif des_is_here:
                print("D", end="")
            else:
                print("-", end="")
        print()

    win = True
    for box in boxes:
        if box not in destination:
            win = False
    if win:
        print ("You Winn hihi")
        break

    move = input ("Your Move?").upper()

    dx = 0
    dy = 0

    if move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    elif move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    
  

    if 0 <= player['x'] + dx < map_sokoban['x'] and  0<= player ['y'] + dy < map_sokoban['y']:
        player ['x'] += dx
        player ['y'] += dy

    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy
    