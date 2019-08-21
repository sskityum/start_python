def wrap_calc(func):
    def result_func(x, y):
        x = x**2
        y = y**2
        return func(x, y)
    return result_func

def wrap_message(func):
    def result_func(text):
        print('От Директора')
        func(text)
        print('Спасибо, что пишете нам')
    return result_func