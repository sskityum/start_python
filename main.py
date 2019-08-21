from wrap import wrap_calc, wrap_message
# from wrap import *

@wrap_calc
def calc(x, y):
    return x + y

@wrap_calc
def render(x, y):
    print(x, y)
    return x, y


@wrap_calc
def pow(x, y):
    return x**y 

@wrap_message
def message(text):
    print(text)

# if __name__ == '__main__':
#     ready_func = wrap_calc(render)
#     print(render(4, 5))
#     print(ready_func(4, 5))

if __name__ == '__main__':
    print(calc(4, 5))
    print(render(4, 5))
    print(pow(4, 5))
    message('Куда то пишем?')
    