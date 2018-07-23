class employee:

    def __init__(self,fname,lname,sal):
        self.firstname=fname
        self.lastname=lname
        self.salary=sal

    def get_name(self):
        return "%s %s" %(self.firstname, self.lastname)

    def get_mail(self):
        return "%s.%s@inapp.com" %(self.firstname.lower(),self.lastname.lower())

    def getsal(self):
        return "your salary is %s" %(self.salary)



e1=employee("Supriya","Prasanth",25000)
print(e1.get_name())
print(e1.get_mail())
print(e1.getsal())

