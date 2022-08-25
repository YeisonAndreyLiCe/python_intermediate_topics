from timeit import repeat


def make_repeater(n):
    def repeater(x):
        assert type(x) == str, "The argument must be a string"
        return x * n
    return repeater

def run():
    repeat_5 = make_repeater(5)("hello")
    print(repeat_5)

def make_division_by(n):
    return lambda x: x / n


        
if __name__ == "__main__":
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)
    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))