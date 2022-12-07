import time

h= int(time.strftime('%H'))
m= int(time.strftime("%M"))

def trabajo():
    hr = 19-h
    mt = 59-m
    return "Te quedan {} horas y {} minutos de curro.".format (hr,mt) 

if (h >19):
    print("Ya devieras estar fuera del trabajo")
else:
    print("Son las: {}:{}".format(h,m))
    print(trabajo())

