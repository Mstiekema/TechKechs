import sys

input = sys.stdin.readline

# Global vars
inputs = []

# Function defs


def check_person():
    print("person")


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
inputs.pop()

n_people = int(n_people)
n_projects = int(n_projects)

while n_people > 0:
    check_person()
    n_people -= 1

while n_projects > 0:
    check_project()
    n_projects -= 1

print(inputs)
