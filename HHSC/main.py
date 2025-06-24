## -- Script console --
import sys

if __name__ == '__main__':
    crd = ""
    while True:
        inp = input('/ ')
        if inp == 'exit' or inp == 'e' or inp == 'q':
            break
        elif inp == 'cd':
            pass
        else:
            sys.stdout.write(f"command <{inp}> not a binary or script\n")
