class Student:
    def __init__(self,firstname,secondname,country,age):
        self.firstname=firstname
        self.secondname=secondname
        self.age=age
        self.country=country
        

    def year(self):
            year_of_birth=2022-self.age
            return f"Hello your year of birth is {year_of_birth}"
    def names(self):
                return f"Hello your name is  {self.firstname}  {self.secondname}" 

 
    def initial(self):
                    return f"Hello your initials are {self.firstname[0]}  {self.secondname[0]}" 

        



