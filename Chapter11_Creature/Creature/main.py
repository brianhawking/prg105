from Creature import Creature, Orc, OrcBoss


def main():
    rabbit = Creature("rabbit", True, (10, 250, 10), "bunny.gif")
    orc = Orc((-100, 200, 50), "org.gif", "axe", 150, 150)
    griksnak = OrcBoss((300, 150, 35), "orc_boss.gif", "greatsword", 350, 200, "Griksnak", "jump and slash")

    print(rabbit)
    print(orc)
    print(griksnak)


# ==== START =================
main()
