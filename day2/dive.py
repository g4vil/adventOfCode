FILE = "./diveLog.txt"

def generate_list(file):
    f = open(file, "r")
    logs = []
    for line in f:
        line = line.replace("\n", "")
        line = line.split(" ")
        logs.append(line)
        
    for i in range(0, len(logs)):
        logs[i][1] = int(logs[i][1])
            
    return logs

def calculate_aimin(list):
    horizontal_position, depth, aim = 0, 0, 0
    for i in range(0, len(list)):
        if list[i][0] == 'forward':
            horizontal_position += list[i][1]
            depth += list[i][1] * aim
        elif list[i][0] == 'down':
            aim += list[i][1]
        elif list[i][0] == 'up':
            aim -= list[i][1]
        else:
            continue
    return horizontal_position * depth
    
def run():
    print(calculate_aimin(generate_list(FILE)))

if __name__ == "__main__":
    run()