class Person:
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address
    def introduce(self):
        print("Nama             : " + self.name)
        print("Tanggal Lahir    : " + self.birthday)
        print("Tempat Tinggal   : " + self.address)

p = Person("Muhammad Alfiansyah", "2004-02-07", "Karanganyar - Gumukmas - Jember")
p.introduce()