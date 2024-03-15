from child_class import Child

class Grandchild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


test = Grandchild("Ivan Ivanov", 33, "Sofia")
print(test.get_name(), test.get_age(), test.get_address())