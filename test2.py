def hello_hello( ):
	"Return a greeting"
	return ( "Hello Hello!" )

def add(x,y):return x+y

def RepeatMessage(msg, times =2 ):
    for i in range(times): print(msg)

def    finalFunction():
    message = "Done!"
    for char in message: pass
    return
    print("Dead code")

def infinite_loop():
    while True:
        pass

if __name__=="__main__":
    print(hello_hello( ))
    result = add(2 ,3 )
    RepeatMessage("Test",3)
    finalFunction()
    infinite_loop()
