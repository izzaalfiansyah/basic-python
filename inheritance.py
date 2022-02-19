class Person:
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address
    def my(self):
        print("Nama             : " + self.name)
        print("Tanggal Lahir    : " + self.birthday)
        print("Tempat Tinggal   : " + self.address)

class Student(Person):
    def __init__(self, name, birthday, address):
        super().__init__(name, birthday, address)
    def introduce(self):
        Person.my(self)
        print("Status           : Mahasiswa")
        print("Universitas      : Politeknik Negeri Jember")

s = Student("Muhammad Alfiansyah", "2004-02-07", "Jember")
s.introduce()