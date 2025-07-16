def  hello_hello( ):
	"Return a greeting"
	return ( "Hello Hello!" )  # docstring style, spacing, extra parentheses

def add(x, y):
    return x + y

def repeat_message(msg, times=2):
    for _ in range(times):
        print(msg)

def final_function():
    message = "Done!"
    for char in message:
        pass
    return

def infinite_loop():
    while True:
        pass

def mixed_case_function(arg1, arg2=5):
    return arg1 + arg2

class MyClass:
    def __init__(self):
        self.value = 10

    def compute(self):
        if self.value > 5:
            print("Computing...")

    def bad_indent(self):
        x = 1
        y = 2
        return x + y

x, y = 10, 20
z = x + y

if __name__ == "__main__":
    print(hello_hello())
    result = add(2, 3)
    repeat_message("Test", 3)
    final_function()
    # Note: infinite_loop() creates an endless loop; consider removing or handling termination.
    print(mixed_case_function(1))
    obj = MyClass()
    obj.compute()
    obj.bad_indent()
