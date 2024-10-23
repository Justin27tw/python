#11210312邱嘉誠
while True:
    A=input("請輸入數字A：")
    B=input("請輸入數字B：")
    A=int(A)
    B=int(B)
    if(A%2==0):
        if(A<B):
            total=0
            for i in range(A, B+2, 2):
                total+=i
        else:
            break
    else:
        if(A<B):
            A+=1
            total=0
            for i in range(A, B+2, 2):
                total+=i
        else:
            break
    print("A+B=",total)
        
    
