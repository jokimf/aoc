# Does not work

class Blueprint:
    def __init__(self, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost):
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost

    def ore_robot_cost(self):
        return self.ore_robot_cost()

    def clay_robot_cost(self):
        return self.clay_robot_cost()

    def obsidian_robot_cost(self):
        return self.obsidian_robot_cost()

    def geode_robot_cost(self):
        return self.geode_robot_cost()


blueprints = {
    1: Blueprint(3, 4, (4, 13), (3, 7))
    , 2: Blueprint(4, 4, (4, 20), (2, 12))
    , 3: Blueprint(3, 3, (3, 9), (3, 7))
    , 4: Blueprint(3, 4, (4, 18), (2, 11))
    , 5: Blueprint(4, 3, (4, 16), (2, 15))
    , 6: Blueprint(2, 3, (3, 11), (3, 14))
    , 7: Blueprint(2, 4, (4, 17), (3, 11))
    , 8: Blueprint(4, 4, (2, 14), (4, 19))
    , 9: Blueprint(2, 3, (3, 18), (2, 19))
    , 10: Blueprint(3, 3, (3, 19), (3, 17))
    , 11: Blueprint(2, 4, (4, 11), (3, 8))
    , 12: Blueprint(4, 4, (4, 17), (2, 13))
    , 13: Blueprint(3, 4, (2, 15), (2, 13))
    , 14: Blueprint(3, 4, (3, 18), (4, 16))
    , 15: Blueprint(4, 4, (4, 5), (3, 15))
    , 16: Blueprint(2, 3, (3, 13), (2, 20))
    , 17: Blueprint(3, 3, (2, 7), (2, 9))
    , 18: Blueprint(4, 3, (4, 15), (3, 12))
    , 19: Blueprint(3, 4, (4, 18), (3, 8))
    , 20: Blueprint(4, 4, (2, 7), (4, 13))
    , 21: Blueprint(3, 4, (4, 5), (4, 8))
    , 22: Blueprint(2, 3, (2, 14), (3, 8))
    , 23: Blueprint(2, 4, (2, 15), (3, 16))
    , 24: Blueprint(3, 4, (4, 18), (3, 13))
    , 25: Blueprint(2, 4, (4, 15), (2, 20))
    , 26: Blueprint(2, 4, (3, 17), (4, 20))
    , 27: Blueprint(3, 3, (3, 17), (2, 13))
    , 28: Blueprint(3, 3, (3, 15), (2, 8))
    , 29: Blueprint(4, 3, (4, 19), (4, 12))
    , 30: Blueprint(4, 4, (4, 14), (2, 16))
}  # ore, ore, (ore,clay), (ore,obsidian)


def det(map_entry):
    bp = map_entry[1]
    ore, clay, obsidian, geode = 0, 0, 0, 0
    ore_p, clay_p, obsidian_p, geode_p = 1, 0, 0, 0

    # 1: Blueprint(3, 4, (4, 13), (3, 7))
    for i in range(24):
        # buy
        if ore >= bp.geode_robot_cost()[0] and obsidian >= bp.geode_robot_cost()[1]:
            geode_p += 1
            ore -= bp.geode_robot_cost()[0]
            obsidian -= bp.geode_robot_cost()[1]
        elif ore >= bp.obsidian_robot_cost()[0] and clay >= bp.clay_robot_cost():
            obsidian_p += 1
            ore -= bp.obsidian_robot_cost()[0]
            clay -= bp.obsidian_robot_cost()[1]
        elif ore >= bp.clay_robot_cost():
            clay_p += 1
            ore -= bp.clay_robot_cost()
        elif ore >= bp.ore_robot_cost():
            ore_p += 1
            ore -= bp.ore_robot_cost()

        # collect
        ore += ore_p
        clay += clay_p
        obsidian += obsidian_p
        geode += geode_p

    return map_entry[0] * geode


total = 0
for a in blueprints.items():
    print(a)
    total += det(a)

print(total)
