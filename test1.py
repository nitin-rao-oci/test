def   HelloWorld( ):
   return(  "Hello, World!" )

def GOODBYE_WORLD(): print("Goodbye!") ; print ("Again!")

def anotherFunction( x ,y= 2):return(x+y)

def __BADfunction123(): 
	"""Bad docstring style""" 
	for i in range(  3 ): print ( i ) 

class   badlyFormatted:
 def __init__(self):self.val= 0 

 def DoThing(self ) :
      if(self.val==0):print ("Doing the thing!")

 def methodWithLogicError(self):
    items = [1, 2, 3]
    for i in range(len(items)):
     print(items[i+1])

x=42;y= 13 ;z= x+y

def misplaced(): pass; return None

if __name__=="__main__":
 HelloWorld()
 GOODBYE_WORLD()
 anotherFunction(3 )
 __BADfunction123()
 obj = badlyFormatted()
 obj.DoThing()
 obj.methodWithLogicError()
 if z> 50 :print( "Big number" )
