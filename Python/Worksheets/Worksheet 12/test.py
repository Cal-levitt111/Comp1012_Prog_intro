
class UniModule:

    def __init__(self, code, name, year, credit, grade=0, pFP=False, discovery=False) -> None:
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit
        self.grade = grade
        self.pFP = pFP
        self.discovery = discovery

    def display_details(self) -> None:
        st_PFP = "PFP"
        st_Disc = "Disc"
        if not self.pFP:
            st_PFP = "NPFP"
        if not self.discovery:
            st_Disc = "NPFP"

        print(self.code+":"+self.name+":Y"+str(self.year)+":"+str(self.credit)+"CR:"+str(self.grade)+"GRD:"+st_PFP+":"+st_Disc)


COMP1011 = UniModule("COMP1011", "Intro to Prog.", 1, 10, discovery=True)
COMP1011.display_details()


