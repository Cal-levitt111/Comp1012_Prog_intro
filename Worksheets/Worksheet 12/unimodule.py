class UniModule:

    def __init__(self, code, name, year, credit, grade=0, PFP=False,
                 discovery=False) -> None:
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit
        self.grade = grade
        self.PFP = PFP
        self.discovery = discovery

    def display_details(self) -> None:
        st_PFP = "PFP"
        st_Disc = "Disc"
        if not self.PFP:
            st_PFP = "NPFP"
        if not self.discovery:
            st_Disc = "NDisc"

        print(self.code + ":" + self.name+":Y" + str(self.year) + ":" +
              str(self.credit) +
              "CR:" + str(self.grade) + "GRD:" + st_PFP+":" + st_Disc)


class Transcript:

    def __init__(self) -> None:
        self.modules = []

    def add_module(self, item) -> None:
        if item in self.modules:
            print(ValueError("module already exists!"))
        elif not isinstance(item, UniModule):
            print(ValueError("expected item be an instance of UniModule"))
        else:
            self.modules.append(item)

    def print_transcript(self) -> None:
        for item in self.modules:
            item.display_details()


COMP1012 = UniModule("COMP1011", "Intro to Prog.", 1, 10, grade=75,
                     discovery=True)
COMP1121 = UniModule("COMP1121", "Databases", 1, 10, PFP=True)
COMP1211 = UniModule("COMP1211", "Comp. Arch.", 1, 10, grade=80, PFP=True)
t_student1 = Transcript()
t_student1.add_module(COMP1012)
t_student1.add_module(COMP1121)
t_student1.add_module(COMP1211)
t_student1.add_module("test1")
t_student1.add_module(COMP1211)
t_student1.print_transcript()
