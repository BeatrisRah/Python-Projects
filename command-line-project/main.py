import sys

def get_sum(num1, num2):
    return(int(num1) + int(num2))

if __name__ == '__main__':
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    print('Res', get_sum(num1, num2))
    print(f'arg1 ${sys.argv[0]}')