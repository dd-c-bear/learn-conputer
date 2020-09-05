def lsk(func):
    def desker():
        func()
        print('aaaa')
    return desker
@lsk
def smdder ():
    print('bbbbb')

smdder()


