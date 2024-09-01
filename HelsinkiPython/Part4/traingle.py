# Copy here code of line function from previous exercise
def line(x, st):
    x_int = int(x)
    if st == "":
        print("*"* x_int)
    else:
        print(st[0]* x_int)

def triangle(size):
    # You should call function line here with proper parameters
    x = 1
    num = 1
    while x < (size +1):
        line(num, "#")
        num += 1
        x +=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
