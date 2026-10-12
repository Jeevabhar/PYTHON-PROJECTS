# 1. SINGLE INHERITANCE
# Employee -> Developer

class Employee:
    def login(self):
        print("Employee logged in")


class Developer(Employee):
    def write_code(self):
        print("Developer is writing code")


print("1. Single Inheritance")
d = Developer()
d.login()
d.write_code()


# 2. MULTIPLE INHERITANCE
# Developer + Manager -> TechLead

class Manager:
    def manage_team(self):
        print("Manager is managing the team")


class TechLead(Developer, Manager):
    def lead_project(self):
        print("Tech Lead is leading the project")


print("\n2. Multiple Inheritance")
tl = TechLead()
tl.login()
tl.write_code()
tl.manage_team()
tl.lead_project()


# 3. MULTILEVEL INHERITANCE
# Employee -> Manager -> ProjectManager

class ProjectManager(Manager):
    def manage_project(self):
        print("Project Manager is managing the project")


print("\n3. Multilevel Inheritance")
pm = ProjectManager()
pm.manage_team()
pm.manage_project()


# 4. HIERARCHICAL INHERITANCE
# Employee -> Tester
# Employee -> Designer

class Tester(Employee):
    def test_software(self):
        print("Tester is testing software")


class Designer(Employee):
    def design_ui(self):
        print("Designer is designing UI")


print("\n4. Hierarchical Inheritance")

tester = Tester()
tester.login()
tester.test_software()

designer = Designer()
designer.login()
designer.design_ui()


# 5. HYBRID INHERITANCE
# Combination of multiple + hierarchical inheritance

class SeniorDeveloper(Developer):
    def review_code(self):
        print("Senior Developer is reviewing code")


class LeadDeveloper(SeniorDeveloper, Manager):
    def lead_development(self):
        print("Lead Developer is leading development")


print("\n5. Hybrid Inheritance")
ld = LeadDeveloper()
ld.login()
ld.write_code()
ld.review_code()
ld.manage_team()
ld.lead_development()
