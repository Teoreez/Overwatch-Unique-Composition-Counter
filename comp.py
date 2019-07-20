import csv

dpsArray = ["Ashe", "Bastion", "Doomfist", "Hanzo", "Junkrat", "Mccree", "Mei", "Pharah",
            "Reaper", "Soldier76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker"]

tanksArray = ["D.Va", "Orisa", "Reinhardt",
              "Roadhog", "Winston", "Wrecking Ball", "Zarya", "Sigma"]

supportsArray = ["Ana", "Baptiste", "Brigitte",
                 "Lucio", "Mercy", "Moira", "Zenyatta"]

resultdps = [[x, y] for x in dpsArray for y in dpsArray if x != y]
resulttank = [[x, y] for x in tanksArray for y in tanksArray if x != y]
resultsupport = [[x, y]
                 for x in supportsArray for y in supportsArray if x != y]

dps = {tuple(item) for item in map(sorted, resultdps)}
tank = {tuple(item) for item in map(sorted, resulttank)}
sup = {tuple(item) for item in map(sorted, resultsupport)}

print(len(dps))
print(len(tank))
print(len(sup))

comps = [[x, y, z] for x in dps for y in tank for z in sup]


print(len(comps))
with open('compsSigmaTank.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(comps)
