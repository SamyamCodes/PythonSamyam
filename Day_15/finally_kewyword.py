def func1():
        
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index value:"))
        print(l[i])
    except:
        print("Some error occured.")

    finally:
        print("I am always executing.")

x = func1()
print(x)