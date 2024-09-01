# Copy here code of line function from previous exercise
def line(x, st):
    x_int = int(x)
    if st == "":
        print("*"* x_int)
    else:
        print(st[0]* x_int)

def triangle(size):
    x = 1
    num = 1
    while x < (size +1):
        line(num, "#")
        num += 1
        x +=1

if __name__ == "__main__":
    triangle(5)
