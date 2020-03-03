# Damien Connolly

student = []

def displaymenu():
    print ("what would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input ("Type one letter (a/v/q):").strip()
    return choice

def doadd():
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readmodules()
    student.append(currentStudent)
    
def readmodules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
    # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
    # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
        return modules

def displayModules(modules):
        print ("\tName \tGrade")
        for module in modules:
             print("\t{} \t{}".format(module["name"], module["grade"])) 

def doview():
    for currentStudent in student:
        print(currentStudent["name"])
    displayModules(currentStudent["modules"]);

    
choice = displaymenu()

while (choice != 'q'):
    if choice == 'a':
        doadd()
    elif choice == 'v':
        doview()
    elif choice != 'q':
        print ("\n\nplease select either a, v, or q")
    choice = displaymenu

