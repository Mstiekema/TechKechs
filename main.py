import sys

input = sys.stdin.readline

# Global vars
inputs = []
skillsDict = {}
result = []
projects = {}


def update_skill(person, skill):
    skillsDict[skill][person] += 1


def check_person():
    name, n_skills = inputs[0].split(" ")  # get name and number of skills
    inputs.pop(0)
    for i in range(int(n_skills)):  # for each skill
        skill, level = inputs[0].split(" ")
        if skill not in skillsDict.keys():
            skillsDict[skill] = {}
        skillsDict[skill][name] = int(level)
        inputs.pop(0)


def check_project():
    # Name, Days to complete, Score, Best before, n of skill required
    name, Di, Si, Bi, Ri = inputs[0].split(" ")
    skills_required = int(Ri)
    roles = []
    inputs.pop(0)

    while skills_required > 0:
        skill, level = inputs[0].split(" ")
        skill_level = (skill, int(level))
        roles.append(skill_level)
        inputs.pop(0)
        skills_required -= 1

    projects[name] = {
        "Di": Di,
        "Si": Si,
        "Bi": Bi,
        "roles": sorted(roles)
    }


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


days_to_take = [{project: projects[project]["Di"]} for project in projects]
# days_to_take = sorted(days_to_take)
while len(projects) > 0:
    assigned = False
    items = days_to_take[0].items()
    temp = days_to_take[0]
    days_to_take.pop(0)
    name, days = list(items)[0]
    project = projects[name]
    skills_req = project["roles"]
    for role, level in skills_req:
        assigned = False
        skillList = skillsDict[role].items()
        p_name, p_level = tuple(skillList)[0]

        # if not name in result:
        #     result[name] = []

        if p_level >= level:
            result.append((name, p_name))
            skillsDict[role][p_name] += 1
            assigned = True
    # if no roles are assigned, do not delete the project and put the project on the end
    days_to_take.append(temp)

    # if it is not empty, delete it
    if assigned:
        del projects[name]


# Print completed projects
project_names = [project for project, people in result]
print(len(set(project_names)))

current_item = ""
all_people = []
# Print each project and their participants
for project, people in result:

    all_people.append(people)
    if current_item != project:
        all_people = []
        current_item = project
        # all_people.append(people)
        print(project)
    else:
        print(" ".join(all_people))
