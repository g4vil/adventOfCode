FILE = "./diveLog.txt"

def logsList(file):
    f = open(file, "r")
    logs = []
    for line in f:
        line = line.replace("\n", "")
        line = line.split(" ")
        logs.append(line)
        
    for i in range(0, len(logs)):
        logs[i][1] = int(logs[i][1])
            
    return logs

def calculate_dive(list):
    forward, depth = 0, 0
    for i in range(0, len(list)):
        if list[i][0] == 'forward':
            forward += list[i][1]
        elif list[i][0] == 'down':
            depth += list[i][1]
        elif list[i][0] == 'up':
            depth -= list[i][1]
        else:
            continue
        
    dive = forward * depth
    return dive
    
def run():
    print(calculate_dive(logsList(FILE)))

if __name__ == "__main__":
    run()