# errors and exception

# a=-5

# assert (a>=0), 'assertion error'

# try:
#     a=5/0
# except Exception as e:
#     print("error!",e)
# finally:
#     print("Getting Ahead...")            

class ValueTooHighError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_case(x):
    if(x>100):
        raise ValueTooHighError('Value is too high',x)
    if(x<0):
        raise ValueTooSmallError('value too small error',x)        
    
try:
    test_case(101)
except ValueTooHighError as e:
    print(e.message,e.value)
except ValueTooSmallError as e:
    print(e.message,e.value)
finally:
    print("kaam khalllas vayo")    
