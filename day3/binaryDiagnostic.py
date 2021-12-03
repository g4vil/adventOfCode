FILE = './binaryDiagnostic.txt'

def binaryList(file):
    f = open(file, "r")
    binarys = []
    for line in f:
        line = str(line)
        line = line.replace('\n',"")
        binarys.append(line)
        
    return binarys

def most_rep(list):
    ones, ceros = 0, 0
    for i in range(len(list)):
        if list[i] == 1:
            ones += 1
        else:
            ceros += 1
    
    if ones > ceros:
        return 1
    else:
        return 0
    
def minus_rep(list):
    ones, ceros = 0, 0
    for i in range(len(list)):
        if list[i] == 1:
            ones += 1
        else:
            ceros += 1
    
    if ones < ceros:
        return 1
    else:
        return 0
    
def makeDecimals(gamma, epsilon):
    gamma_decimal = 0
    epsilon_decimal = 0
    gamma, epsilon = gamma[::-1], epsilon[::-1]
    for i in range(len(gamma)):
        if gamma[i] == '0':
            pass
        elif gamma[i] == '1':
            gamma_decimal += 2**i
    
    for i in range(len(epsilon)):
        if epsilon[i] == '0':
            pass
        else:
            epsilon_decimal += 2**i

    return gamma_decimal * epsilon_decimal

def promedium(list):
    first, second, third, fourth, five, six, seven, eigth, nine, ten, eleven, twelve = [], [], [], [], [], [], [], [], [], [], [], []
    for i in range(len(list)):
        for j in range(len(list[0])):
            c = int(list[i][j])
            if j == 0:
                first.append(c)
            elif j == 1:
                second.append(c)
            elif j == 2:
                third.append(c)
            elif j == 3:
                fourth.append(c)
            elif j == 4:
                five.append(c)
            elif j == 5:
                six.append(c)
            elif j == 6:
                seven.append(c)
            elif j == 7:
                eigth.append(c)
            elif j == 8:
                nine.append(c)
            elif j == 9:
                ten.append(c)
            elif j == 10:
                eleven.append(c)
            elif j == 11:
                twelve.append(c)
                
    gamma = str(most_rep(first)) + str(most_rep(second)) + str(most_rep(third)) + str(most_rep(fourth)) + str(most_rep(five)) + str(most_rep(six)) + str(most_rep(seven)) + str(most_rep(eigth)) + str(most_rep(nine)) + str(most_rep(ten)) + str(most_rep(eleven)) + str(most_rep(twelve))
    epsilon = str(minus_rep(first)) + str(minus_rep(second)) + str(minus_rep(third)) + str(minus_rep(fourth)) + str(minus_rep(five)) + str(minus_rep(six)) + str(minus_rep(seven)) + str(minus_rep(eigth)) + str(minus_rep(nine)) + str(minus_rep(ten)) + str(minus_rep(eleven)) + str(minus_rep(twelve))

    return makeDecimals(gamma, epsilon)
            
    
def run():
    print(promedium(binaryList(FILE)))

if __name__ == '__main__':
    run()