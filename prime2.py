def prm(x):
    for p_num in range(2, x+1):

        for p_div in range(2, x+1):
            if(p_num % p_div == 0):
                break;

        if (p_num == p_div):
            print(p_div)


prm(500)