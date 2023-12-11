def Rdash_OperationFun(Front,Right,Down,Left,Up,Back):
    t1=Down[0][2]
    t2=Down[1][2]
    t3=Down[2][2]

    Down[0][2]=Front[0][2]
    Down[1][2]=Front[1][2]
    Down[2][2]=Front[2][2]

    Front[0][2]=Up[0][2]
    Front[1][2]=Up[1][2]
    Front[2][2]=Up[2][2]

    Up[0][2]=Back[0][2]
    Up[1][2]=Back[1][2]
    Up[2][2]=Back[2][2]

    Back[0][2]=t1
    Back[1][2]=t2
    Back[2][2]=t3

    temp1=Right[0][2]
    temp2=Right[0][1]
    temp3=Right[0][0]

    Right[0][0]=Right[0][2]
    Right[0][1]=Right[1][2]
    Right[0][2]=Right[2][2]

    Right[0][2]=Right[2][2]
    Right[1][2]=Right[2][1]
    Right[2][2]=Right[2][0]

    Right[2][2]=Right[2][0]
    Right[2][1]=Right[1][0]
    Right[2][0]=Right[0][0]

    Right[2][0]=temp3
    Right[1][0]=temp2
    Right[0][0]=temp1

    return Front,Right,Down,Left,Up,Back