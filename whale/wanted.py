from collections import UserList

var1 = UserList()
var1.attr1 = "passed"
print(var1.attr1)  # prints passed

var2 = UserList()
print(var2.attr1)  # prints passed


class CustomList(list):
    def trim(self):
        if self:
            self.pop()
        if self:
            self.pop(0)


xl = {
    "A": "X",
    "B": "X",
    "C": "X",
    "D": "X",
    "E": "Y",
    "F": "Y",
    "G": "Y",
}
