import sys

input = sys.stdin.readline

# Global vars
inputs = []
personDict = {}

# Function defs


def check_person():
    skillList = []
    name, n_skills = inputs[0].split(" ") #get name and number of skills
    inputs.pop(0)
    for i in range(int(n_skills)): #for each skill
        skillList.append(inputs[0].split(" ")) #add it to the persons skill list
        inputs.pop(0)
    personDict[name] = skillList
    print(name, personDict[name])


def check_project():
    print("project")


# Input
while True:
    text = input().strip()
    if text:
        inputs.append(text)
    else:
        break

# Runtime
n_people, n_projects = inputs[0].split(" ")
inputs.pop(0)

n_people = int(n_people)
n_projects = int(n_projects)

while n_people > 0:
    check_person()
    n_people -= 1

while n_projects > 0:
    check_project()
    n_projects -= 1

print(inputs)
