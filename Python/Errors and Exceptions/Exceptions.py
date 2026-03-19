# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        e="integer division or modulo by zero"
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')
