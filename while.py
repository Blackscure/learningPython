cars = ["Volvo", "Subaru", "Mistubishi", "Toyota","Volkswagen"]

i = 0

while i < len(cars):
    print(cars[i])

    i =  i + 1

# list comprehension offers short hand
thislist = ["mango", "banana", "apple"]

[print(x) for x in thislist]

