import sys


def create_new_line():
    if len(sys.argv) < 3 or not sys.argv[2]:
        print('No new line provided')
        return

    with open('demo.txt', 'a') as text_file:
        text_file.write(sys.argv[2])

def read_file():
    with open('demo.txt') as text_file:
        print(text_file.read())


commands = {
    'c': {'func':create_new_line, 'desc': 'Creates a new line in demo.txt' },
    'r':{'func':read_file, "desc":'Reads demo.txt contnent'},

}

def check_args():
    if len(sys.argv) > 1:
        return True
    return False


if __name__ == '__main__':
    if check_args() and sys.argv[1] in commands:
        commands[sys.argv[1]]['func']()
