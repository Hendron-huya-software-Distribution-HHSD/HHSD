## -- Compaliation files --
import sys
import shutil #todo: make it run!

def readf(file):
    with open(file, 'r') as f:
        return f.read()

def parse(file):
    i = 0
    ch = None
    result = []
    while i < len(file):
        ch = file[i]
        if ch == ':':
            j = i
            while i < len(file):
                if file[i] == '>':
                    break
                i += 1
            result.append(file[j:i])
            i -= 1
        elif ch == '"':
            j = i
            i += 1
            while i < len(file):
                if file[i] == '"':
                    break
                i += 1
            result.append(file[j:i+1])
            j = i
        elif ch.isalpha():
            j = i
            while i < len(file):
                if not file[i].isalpha():
                    break
                i += 1
            result.append(file[j:i])
        elif ch not in '\n \t':
            result.append(ch)
        i += 1
    return result
def run(file, args=None):
    labels = {}
    stack = []
    for ind, t in enumerate(file):
        if t[0] == ':':
            labels[t] = ind
    print(labels)
    if ':main' not in labels and args==None:
        print("error: main function not defined")
        sys.exit(1)
    i = labels[':main']+1
    while i < len(file):
        if file[i] == '!':
            if ':'+file[i+1] not in labels:
                print(f"error, label {':'+file[i+1]} not found")
                sys.exit(1)
            stack.append(i+1)
            i = labels[':'+file[i+1]]
        elif file[i] == '&':
            print(file[i+1])
            i += 1
        elif file[i] == '<':
            if len(stack) == 0:
                break
            i = stack.pop()
        i += 1
if __name__ == '__main__':
    mainf = readf(sys.argv[1])
    p = parse(mainf)
    run(p)