while True:
    try:
        N=int(input())
        num=0
        for i in range(N):
            if str(i*i).endswith(str(i)):
                num+=1
        print(num)
    except:
        break
