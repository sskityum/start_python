from wrap import wrap_calc, wrap_message, wrap_time

@wrap_time
@wrap_calc
def calc(x, y):
    return x + y

@wrap_time
@wrap_calc
def render(x, y):
    print(x, y)
    return x, y

@wrap_time
@wrap_calc
def pow(x, y):
    return x**y 

@wrap_time
@wrap_message
def message(text):
    print(text)

if __name__ == '__main__':
    print(calc(4, 5))
    print()
    print(render(4, 5))
    print()
    print(pow(4, 5))
    print()
    message('Куда то пишем...')
    