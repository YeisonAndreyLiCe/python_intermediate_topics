import time 

def fibo_gen():
    num1 = 0
    num2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield num1
        elif counter == 1:
            counter += 1
            yield num2
        else:
            aux = num1 + num2
            num1, num2 = num2, aux
            counter += 1
            yield aux
if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        if element > 10:
            break
        print(element)
        time.sleep(0.1)