# CM/(r+v)^2 = g
C = 6.674e-11
M = 5.972e24
R = 6.371e6


def g_pospesek(v):
    return C * M / (R + v)**2


print("OIS je zakon!")


def izpis(v, g, unit="m"):
    print(
        f"Na nadmorska višina: {v:.1f} {unit} je gravitacijski pospešek {g:.2f} m/s^2".replace(".", ","))


# v = eval(input("Vnesite nadmorsko višino: "))
# arg naj bo v km
def finale(v):
    g = g_pospesek(v*1000)
    izpis(v/1000, g, unit="km")


finale(0.0)
finale(10.0)
finale(1000.0)
finale(100000.0)
