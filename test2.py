def  hello_hello( ):
	"Return a greeting"
	return ( "Hello Hello!" )  # docstring style, spacing, extra parentheses

def add(x,y):return x+y  # no spaces, single line

def RepeatMessage(msg, times =2 ):
    for i in range(times): print(msg)  # one-line loop, bad spacing

def    finalFunction():
    message = "Done!"
    for char in message: pass
    return
    print("Dead code")

def infinite_loop():
    while True:
        pass

def MIXEDcaseFunction(  arg1 ,arg2=5):return arg1+ arg2

class  MyClass:
 def __init__ ( self ):
  self.value=10

 def compute( self):
  if(self.value>5): print( "Computing..." )

 def badIndent(self):
  x=1
   y=2
  return x+y

x, y = 10, 20
z = x + y

if __name__=="__main__":
    print(hello_hello( ))
    result = add(2 ,3 )
    RepeatMessage("Test",3)
    finalFunction()
    infinite_loop()
    print(MIXEDcaseFunction(1))
    obj = MyClass()
    obj.compute()
    obj.badIndent()
