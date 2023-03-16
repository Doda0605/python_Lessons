list = []
count = 0
max = 0
min = 0
sv = 0.0
while True:
    broj = input()
    if broj == "Done":
        break
    if broj.isnumeric():
        list.append(float(broj))
        count += 1
print("Uneseno brojeva: ", count)
min = list[0]
max = list[0]
for x in list:
    print(x)
    if x > max:
        x = max
    if x < min:
        x = min
    sv = sv + x

sv /= count

print("SV: ", sv, " min: ", min, "max: ", max)
list.sort(reverse=False)
for x in list:
    print(x)