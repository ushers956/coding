class employee:

    def __init__(self):
        print('empolyee created')

    def __del__(self):
        print("destructor called")

def create_obj():
    print('making object...')
    obj = employee()
    print('function end...')
    del obj

print('çalling create_obj() function...')
obj = create_obj()
print('program end...')