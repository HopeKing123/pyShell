a = 100


def func():
#    a = 10

    def inner_func():
#        a = 1
        print(a)
    inner_func()


func()

