import csv

dpsArray = ["Ashe", "Bastion", "Doomfist", "Hanzo", "Junkrat", "Mccree", "Mei", "Pharah",
            "Reaper", "Soldier76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker"]

tanksArray = ["D.Va", "Orisa", "Reinhardt",
              "Roadhog", "Winston", "Wrecking Ball", "Zarya"]

supportsArray = ["Ana", "Baptiste", "Brigitte",
                 "Lucio", "Mercy", "Moira", "Zenyatta"]
result = []


def combine(Array):
    for x in Array:
        for i in Array:
            temp = []
            temp.append(x)
            temp.append(i)
            if temp[0] != temp[1]:
                result.append(temp)


combine(supportsArray)


print("The len of result: ", len(result))
sort = {tuple(item) for item in map(sorted, result)}
print("The len of sort: ", len(sort))

with open('supports.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(sort)
    csv_writer.writerow(result)
