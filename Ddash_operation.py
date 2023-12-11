def down_dash_operationFun(Front,Right,Down,Left,Up,Back):

    t1 = Front[2][0]
    t2 = Front[2][1]
    t3 = Front[2][2]

    Front[2][0] = Right[2][0]
    Front[2][1] = Right[2][1]
    Front[2][2] = Right[2][2]

    Right[2][0] = Back[0][2]
    Right[2][1] = Back[0][1]
    Right[2][2] = Back[0][0]

    Back[0][2] = Left[2][0]
    Back[0][1] = Left[2][1]
    Back[0][0] = Left[2][2]

    Left[2][0] = t1
    Left[2][1] = t2
    Left[2][2] = t3

    temp1=Down[0][2]
    temp2=Down[0][1]
    temp3=Down[0][0]

    Down[0][0]=Down[0][2]
    Down[0][1]=Down[1][2]
    Down[0][2]=Down[2][2]

    Down[0][2]=Down[2][2]
    Down[1][2]=Down[2][1]
    Down[2][2]=Down[2][0]

    Down[2][2]=Down[2][0]
    Down[2][1]=Down[1][0]
    Down[2][0]=Down[0][0]

    Down[2][0]=temp3
    Down[1][0]=temp2
    Down[0][0]=temp1

    return Front,Right,Down,Left,Up,Back