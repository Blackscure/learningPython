def main():
    x = get_int("Whats' x")
    print(f"x is {x}")


def get_int(promt):
    while True:
        try:
            return int(input("What is x?"))
        except ValueError:
            pass

main()