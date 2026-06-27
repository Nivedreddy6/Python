class faculty:
    def __init__(self,f_name,desc,qual):
        self.f_name=f_name
        self.desc=desc
        self.qual=qual
    def show(self):
        print("Facualty Name is:",self.f_name)
        print("Facualty Designation is:",self.desc)
        print("Facualty Qualification is:",self.qual)
class student:
    def __init__(self,s_name,age,course,year):
        self.s_name=s_name
        self.age=age
        self.course=course
        self.year=year
    def s_show(self):
        print("Student Name   Is: ",self.s_name)
        print("Student Age    Is: ",self.age)
        print("Student Course Is: ",self.course)
        print("Student year Of Study Is: ",self.year)
class university(faculty, student):
    def __init__(self,
                 f_name, desc, qual,
                 s_name, age, course, year):

        faculty.__init__(self, f_name, desc, qual)
        student.__init__(self, s_name, age, course, year)

    def display(self):
        self.show()
        self.s_show()


obj = university(
    "Koushik", "Asst Professor", "M.Tech",
    "Ganesh", 22, "B.Tech", 2
)

obj.display()
