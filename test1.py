def hello_world():
    return "Hello, World!"

def goodbye_world(): 
    print("Goodbye!")
    print ("Again!")

def another_function(x, y):
    return x + y

def bad_function_123():
    """Bad docstring style"""
    for i in range(3):
        print(i) 

class BadlyFormatted:
    def __init__(self):
        self.val = 0

    def do_thing(self):
        if self.val == 0:
            print("Doing the thing!")

    def method_with_logic_error(self):
        items = [1, 2, 3]
        for item in items[1:]:
            print(item)

def build_list(input_list):
    return [x for x in input_list if x > 0]

def append_to(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

def inclusive_range_bug():
    for i in range(1, 6):
        print(i)

def print_indexed_items(items):
    i = 0
    while i < len(items):
        print(i, items[i])
        i += 1

def total(items):
    result = 0
    for i in items:
        result += i
    return result

x = 42
y = 13
z = x + y

def misplaced():
    pass

if __name__ == "__main__":
    print(hello_world())
    goodbye_world()
    print(another_function(3, 0))
    bad_function_123()
    obj = BadlyFormatted()
    obj.do_thing()
    obj.method_with_logic_error()
    print(build_list([-1, 2, 3]))
    print(append_to("x"))
    inclusive_range_bug()
    print_indexed_items(["a", "b", "c"])
    print(total([1, 2, 3]))
    if z > 50:
        print("Big number")
