# CM/(r+v)^2 = g
C = 6.674e-11
M = 5.972e24
R = 6.371e6


def g_pospesek(v: float | int) -> float | int:
    return C * M / (R + v)**2


print("OIS je zakon!")


def izpis(v, g):
    print(f"Na nadmorska višina: {v} je gravitacijski pospešek {g}")
