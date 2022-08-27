from unicodedata import name


class Student:
    def __init__(self, name:str,subjects:list,marks:list):
        self.name = name
        self.subjects = subjects
        self.marks = marks

    def print_stu(self):
        str_out = ""
        for mark,sub in zip(self.marks,self.subjects):
            str_out = str_out+"\n"+str(mark)+"\t"+str(sub)
        return str_out
    