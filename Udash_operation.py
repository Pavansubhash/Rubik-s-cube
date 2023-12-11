def up_dash_OperationFun(Front,Right,Down,Left,Up,Back):
    
    t1 = Right[0][0]
    t2 = Right[0][1]
    t3 = Right[0][2]

    Right[0][0] = Front[0][0]
    Right[0][1] = Front[0][1]
    Right[0][2] = Front[0][2]

    Front[0][0] = Left[0][0]
    Front[0][1] = Left[0][1]
    Front[0][2] = Left[0][2]

    Left[0][0]=Back[2][2]
    Left[0][1]=Back[2][1]
    Left[0][2]=Back[2][0]

    Back[2][2] = t1
    Back[2][1] = t2
    Back[2][0] = t3

    # t1 = Left[0][0]
    # t2 = Left[0][1]
    # t3 = Left[0][2]

    # Left[0][0] = Front[0][0]
    # Left[0][1] = Front[0][1]
    # Left[0][2] = Front[0][2]

    # Front[0][0] = Right[0][0]
    # Front[0][1] = Right[0][1]
    # Front[0][2] = Right[0][2]

    # Right[0][0]=Back[0][2]
    # Right[0][1]=Back[0][1]
    # Right[0][2]=Back[0][0]

    # Back[0][0]=t3
    # Back[0][1]=t2
    # Back[0][2]=t1

    temp1=Up[0][2]
    temp2=Up[0][1]
    temp3=Up[0][0]

    Up[0][0]=Up[0][2]
    Up[0][1]=Up[1][2]
    Up[0][2]=Up[2][2]

    Up[0][2]=Up[2][2]
    Up[1][2]=Up[2][1]
    Up[2][2]=Up[2][0]

    Up[2][2]=Up[2][0]
    Up[2][1]=Up[1][0]
    Up[2][0]=Up[0][0]

    Up[2][0]=temp3
    Up[1][0]=temp2
    Up[0][0]=temp1

    return Front,Right,Down,Left,Up,Back