from math import sqrt
def run():
    my_dict = {i:round(sqrt(i),2) for i in range(1,101)}
    print(my_dict)



if __name__ == "__main__":
    run()