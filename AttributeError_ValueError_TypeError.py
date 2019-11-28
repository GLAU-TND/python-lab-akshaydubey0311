#type error..........

try:
    a = 5
    b = "Python"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
else:
    print ('Success, no error!')
 
 
 #Value error
 
try:
    print (float('Python'))
except ValueError:
    print ('ValueError: could not convert string to float: \'Python\'')
else:
    print ('Success, no error!')
    
    
 #Attribute error
   
   
class Attributes(object):
    a = 2
    print (a)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")
