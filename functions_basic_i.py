#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #error la priemra funcion no está definida


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())# 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())# 5


#5
def number_of_great_lakes():
    print(5) #5
x = number_of_great_lakes()
print(x) # None


#6
def add(b,c):
    print(b+c) #3 y 5
print(add(1,2) + add(2,3)) #Error 


#7
def concatenate(b,c):
    return str(b)+str(c) #Retorna "2" + "5" se suma sin espacio "25"
print(concatenate(2,5)) #25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) # 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())  #10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))#7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))#21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #8


#11
b = 500
print(b) #500
def foobar():
    b = 300
    print(b)
print(b) #500
foobar() #300
print(b) #500


#12
b = 500
print(b)#500
def foobar():
    b = 300
    print(b)
    return b
print(b)#500
b=foobar()#300
print(b)#300


#13
b = 500
print(b)#500
def foobar():
    b = 300
    print(b)#300
    return b
print(b)#500
b=foobar()
print(b)#300


#14
def foo():
    print(1)#1
    bar()
    print(2)#2
def bar():
    print(3)#3             Explicandolo sería que en la párte final se llama a la funcion foo() se ejecuta el primer print luego se llama a la funcion bar() y se imprime lo que esta dentro de esta funcion luego sale y regresa a la anterior funcion en la cual imprime 2
foo()


#15
def foo():
    print(1)# 1 se imprimer en primer lugar
    x = bar()
    print(x)# 5 se imprimer en tercer lugar
    return 10 
def bar():
    print(3)#3 se imprime en segundo lugar
    return 5
y = foo()
print(y) #10 se imprime en cuarto lugar