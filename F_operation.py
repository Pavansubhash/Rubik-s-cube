

def Front_OperationFun(Front,Right,Down,Left,Up,Back):

    t1=Up[2][0]
    t2=Up[2][1] 
    t3=Up[2][2]

    Up[2][0]=Left[2][2]
    Up[2][1]=Left[1][2]
    Up[2][2]=Left[0][2]

    Left[2][2]=Down[0][2]
    Left[1][2]=Down[0][1]
    Left[0][2]=Down[0][0]

    Down[0][2]=Right[0][0]
    Down[0][1]=Right[1][0]
    Down[0][0]=Right[2][0]

    Right[0][0]=t1
    Right[1][0]=t2
    Right[2][0]=t3

    temp1=Front[0][0]
    temp2=Front[1][0]
    temp3=Front[2][0]

    Front[0][0]=Front[2][0]
    Front[1][0]=Front[2][1]
    Front[2][0]=Front[2][2]

    Front[2][0]=Front[2][2]
    Front[2][1]=Front[1][2]
    Front[2][2]=Front[0][2]

    Front[2][2]=Front[0][2]
    Front[1][2]=Front[0][1]
    Front[0][2]=Front[0][0]

    Front[0][2]=temp1
    Front[0][1]=temp2
    Front[0][0]=temp3

    return Front,Right,Down,Left,Up,Back

 