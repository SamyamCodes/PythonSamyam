# Copy here code of line function from previous exercise
def line(x, st):
    x_int = int(x)
    if st == "":
        print("*"* x_int)
    else:
        print(st[0]* x_int)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    x=1
    while x < (height+1):
        line(10, "#")
        x+=1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
