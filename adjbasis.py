import math

RANGES = {
    "BS1" : (32, 52),
    "BS2" : (52, 69),
    "BS3" : (69, 103),
    "BS4" : (103, 134),
    "BS5" : (134, 217),
    "BS6" : (217, 331)
}

POINTS = {
    1 : {"X" : 0.00, "Y" : 0.00, "Z" : 65},
    2 : {"X" : 0.00, "Y" : 7.60, "Z" : 130},
    3 : {"X" : 9.60, "Y" : 7.60, "Z" : 260},
    4 : {"X" : 19.20, "Y" : 7.60, "Z" : 130},
    5 : {"X" : 19.20, "Y" : 0.00, "Z" : 65},
    6 : {"X" : 9.80, "Y" : 6.40, "Z" : 280},                
}

TRIANGLES = {
    1 : {"A" : POINTS[1], "B" : POINTS[5], "C" : POINTS[6]},
    2 : {"A" : POINTS[1], "B" : POINTS[2], "C" : POINTS[6]},
    3 : {"A" : POINTS[5], "B" : POINTS[4], "C" : POINTS[6]},
    4 : {"A" : POINTS[2], "B" : POINTS[3], "C" : POINTS[6]},
    5 : {"A" : POINTS[4], "B" : POINTS[3], "C" : POINTS[6]}
}

STEPX = 0.6
STEPY = 0.4

MAXX = 19.2
MAXY = 7.6

def inTriangle(x, y, TR):
    a = (TR["A"]["X"] - x) * (TR["B"]["Y"] - TR["A"]["Y"]) - (TR["B"]["X"] - TR["A"]["X"]) * (TR["A"]["Y"] - y)
    b = (TR["B"]["X"] - x) * (TR["C"]["Y"] - TR["B"]["Y"]) - (TR["C"]["X"] - TR["B"]["X"]) * (TR["B"]["Y"] - y)
    c = (TR["C"]["X"] - x) * (TR["A"]["Y"] - TR["C"]["Y"]) - (TR["A"]["X"] - TR["C"]["X"]) * (TR["C"]["Y"] - y)
 
    if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
        return True

def Z(x, y):
    for key, T in TRIANGLES.items():
        if inTriangle(x, y, T):
            detA = (T["B"]["Y"] - T["A"]["Y"]) * (T["C"]["Z"] - T["A"]["Z"]) - (T["C"]["Y"] - T["A"]["Y"]) * (T["B"]["Z"] - T["A"]["Z"])
            detB = (T["B"]["X"] - T["A"]["X"]) * (T["C"]["Z"] - T["A"]["Z"]) - (T["C"]["X"] - T["A"]["X"]) * (T["B"]["Z"] - T["A"]["Z"])
            detC = (T["B"]["X"] - T["A"]["X"]) * (T["C"]["Y"] - T["A"]["Y"]) - (T["C"]["X"] - T["A"]["X"]) * (T["B"]["Y"] - T["A"]["Y"])
            return ((y - T["A"]["Y"]) * detB - (x - T["A"]["X"]) * detA) / detC + T["A"]["Z"]                      
    return 0

SUPPS = []
SUPTYPES = {"BS1" : 0, "BS2" : 0, "BS3" : 0, "BS4" : 0, "BS5" : 0, "BS6" : 0}

x = 0
while x <= MAXX:
    ROW = []
    y = 0
    while y <= MAXY:
        z = Z(x, y)
        ROW.append({"X": x, "Y": y, "Z": z})
        for type, ran in RANGES.items():
            if ran[0] <= z < ran[1]:
                SUPTYPES[type]+=1
                break
        y+=STEPY
    SUPPS.append(ROW)
    x+=STEPX    

for R in SUPPS:
    for val in R:
        print(val)
    print()
# print(SUPPS)

print(SUPTYPES)