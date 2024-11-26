import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return x if x > 0 else 0


def elu(x):
    return x if x > 0 else 0.01 * (math.exp(x) - 1)


def activation_func():
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return

    act_name = input('Input activation Function (sigmoid|relu|elu): ')
    if act_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{act_name} is not supported')
        return

    x = float(x)
    if act_name == 'sigmoid':
        print(f'{act_name}: f({x}) = {sigmoid(x)}')
    elif act_name == 'relu':
        print(f'{act_name}: f({x}) = {relu(x)}')
    else:
        print(f'{act_name}: f({x}) = {elu(x)}')


activation_func()
