hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage *= 2
    pass


def disarmed():
    global hero_damage
    hero_damage = (hero_damage * 10) / 100
    pass


def power_potion():
    global hero_damage
    hero_damage += 100
    pass