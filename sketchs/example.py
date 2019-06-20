import time
cont = 0
i = 0
while i < 5:

    time.sleep(0.005)

    print(i)
    i = i + 1
    
    # if i == 1:
    #     i = 0
    
    cont = cont + 1

    if cont == 15:
        print(cont)
        break
    

print(i)



