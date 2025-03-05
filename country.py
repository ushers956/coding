class india():
    def capital(self):
        print("new delhi is the capital of india")

    def language(self):
        print("hindi is the most wide spoken language in india")

    def type(self):
        print("india is a develepment country")


class USA():
    def capital(self):
        print("washinton, D.C. is the capital of usa")

    def language(self):
        print("english is the primary language of usa")

    def type(self):
        print("USA is a develeped country")

obj_ind = india()
obj_usa = USA()


for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()