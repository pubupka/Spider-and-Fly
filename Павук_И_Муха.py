from math import sqrt
f = open(r"C:\Users\Halim\OneDrive\Рабочий стол\Олимпиадки\Тесты к задачам и мои заметки\Паук и муха\input_s1_20.txt")

s1, s2, s3 = list(map(int, f.readline().split(" "))), list(map(int, f.readline().split(" "))), list(map(int, f.readline().split(" ")))
a, b, c = s1[0], s1[1], s1[2]  # размеры комнаты
Sx, Sy, Sz = s2[0], s2[1], s2[2]  # координаты паука
Fx, Fy, Fz = s3[0], s3[1], s3[2]  # координаты мухи


def calc (a, b, Sx, Sy, Sz, Fx, Fy, Fz):
    if Sy == b and Fy == 0 or Fy == b and Sy == 0:
        return round(sqrt(min(b + (a-Sx) + (a-Fx), b + Sx + Fx) ** 2 + (Sz - Fz) ** 2), 3)
    elif Sx == a and Fx == 0 or Fx == a and Sx == 0:
        return round(sqrt(min(a + (b-Sy) + (b-Fy), a + Sy + Fy) ** 2 + (Sz - Fz) ** 2), 3)
    else:
        return round(sqrt((abs(Sx - Fx) + abs(Sy - Fy)) ** 2 + (Sz - Fz) ** 2), 3)


if 0 < Sz < c and 0 < Fz < c:
    print(calc(a, b, Sx, Sy, Sz, Fx, Fy, Fz))
elif 0 < Sy < b and 0 < Fy < b:
    print(calc(c, a, Sz, Sx, Sy, Fz, Fx, Fy))
elif 0 < Sx < a and 0 < Fx < a:
    print(calc(c, b, Sz, Sy, Sx, Fz, Fy, Fx))

# Диагональ ааааааааааааааааа
elif (abs(Sx - Fx) == 0 or abs(Sx - Fx) == a) and (abs(Sy - Fy) == 0 or abs(Sy - Fy) == b) and (abs(Sz - Fz) == 0 or abs(Sz - Fz) == c):
    print(min(calc(a, b, Sx, Sy, Sz, Fx, Fy, Fz), calc(c, b, Sz, Sy, Sx, Fz, Fy, Fx), calc(c, a, Sz, Sx, Sy, Fz, Fx, Fy)))

# Противоположные грани
elif abs(Sz - Fz) == 0 or abs(Sz - Fz) == c:
    print(min(calc(c, b, Sz, Sy, Sx, Fz, Fy, Fx), calc(c, a, Sz, Sx, Sy, Fz, Fx, Fy)))
elif abs(Sy - Fy) == 0 or abs(Sy - Fy) == b:
    print(min(calc(a, b, Sx, Sy, Sz, Fx, Fy, Fz), calc(c, b, Sz, Sy, Sx, Fz, Fy, Fx)))
elif abs(Sx - Fx) == 0 or abs(Sx - Fx) == a:
    print(min(calc(a, b, Sx, Sy, Sz, Fx, Fy, Fz), calc(c, a, Sz, Sx, Sy, Fz, Fx, Fy)))
