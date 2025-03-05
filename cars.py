class honda():

    def petral(self):
        print("most honda cars use regular unleaded gasoline ")
    
    def cost(self):
        print("most honda car cost around 23000 to over 50000")

    def speed(self):
        print("the average speed of a honda car is 130mph")

class tesla():

    def petral(self):
        print("teslas are electric")
    
    def cost(self):
        print("most tesla cars cost around 38000 $")

    def speed(self):
        print("the average speed of a tesla car is 130mph")

obj_hon = honda()
obj_tes = tesla()


for car in (obj_hon, obj_tes):
    car.petral()
    car.cost()
    car.speed()