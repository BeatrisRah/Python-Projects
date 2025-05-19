import sys

def create_new_line(newLine: str):
    with open('demo.txt', 'a') as text_file:
        text_file.write(newLine)

def read_file():
    with open('demo.txt') as text_file:
        print(text_file.read())

def check_args():
    if len(sys.argv) > 1:
        return True
    return False


if __name__ == '__main__':
    if check_args():
        match(sys.argv[1]):
            case 'c':
                if sys.argv[2]: 
                    create_new_line(sys.argv[2])
            case 'r':
                read_file()