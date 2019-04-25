
x = 6

def ex0():
    x = 1
    y = 3
    print(x+y)
    if x < y:
        print(x,"is less than",y)
    else:
        print(x,"is not less than",y)

def ex1():
    z = 5
    print(z)

def ex2():
    z = 7
    print(z)
    print(x)
    x = x + 1

def ex3():
    global x
    x = x*10
    
def style(font = 'Arial',
          font_size = 11,
          bg_color = 'white',
          font_color = 'black'):
    print(font)
    print(font_size)
    print(bg_color)
    print(font_color)


ex0()

style(font = 'Times New Roman',
      font_size = 20,
      bg_color = 'red')

