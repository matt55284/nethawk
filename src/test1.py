
cars = {'A':{'speed':70,
        'color':2},
        'B':{'speed':60,
        'color':3}}



def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print(k)
                dumpclean(v)
            else:
                print('%s : %s' % (k, v))
    else:
        print(obj)


dumpclean(cars)