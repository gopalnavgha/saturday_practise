print("hi hellow how are you im fine")



a =int(input('enter number'))
b = int(input('enter second number:'))

def addition(a,b):
        return print('a+b:',a+b)




addition(a,b)

class car:
        brand ='tata'
        def __init__(self,model,noc):
                self.model = model
                self.noc = noc
        def display(self):
                print('Car brand is:',self.brand)
                print('model_no:',self.model)
                print('noc_no:',self.noc)

obj = car('indica104','ABCSD1233ASDFD')
print(obj.display())
print(obj.brand)
print(obj.model)
print(obj.noc)

