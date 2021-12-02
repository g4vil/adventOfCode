FILE = "./sonarLog.txt"

def list_logs(file):
    logs = []
    f = open(file, "r")
    for line in f:
        logs.append(int(line.replace("\n", "")))
    return logs

def count_increased(list):
    count_up = 0
    # count_down = 0
    actual = list[0]
    
    for i in list:
        if i > actual:
            actual = i
            count_up += 1
        else:
            actual = i
            
    print("Total increases: " + str(count_up))

def sum_thress(list):
    count_up = 0
    count_down = 0
    sums = []    
    for i in range(0, len(list)):
        if i == len(list) - 2:
            sums.append(list[i] + list[i+1])
        elif i == len(list) - 1:
            sums.append(list[i])
        else:
            sums.append(list[i] + list[i+1] + list[i+2])
    
    actual = sums[0]
    
    for i in sums:
        if i > actual:
            actual = i
            count_up += 1
        else:
            actual = i
            
    count_increased(sums)

def run():
    count_increased(list_logs(FILE))
    sum_thress(list_logs(FILE))

if __name__ == '__main__':
    run()