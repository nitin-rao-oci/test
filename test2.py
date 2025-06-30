def hello_hello( ):
	"Return a greeting" # Docstring should use triple quotes
	return ( "Hello Hello!" ) # Extra parentheses and spacing

def add(x,y):return x+y # no spaces, one-liner

def RepeatMessage(msg, times =2 ):
    for i in range(times): print(msg) # one-line loop, bad spacing

def    finalFunction():
    print( "Done!" )

if __name__=="__main__":
    print(hello_hello( ))
    result = add(2 ,3 )
    RepeatMessage("Test",3)
    finalFunction()
