""" Implementation of Battle class.

This class contains code for game combat.

__author__ = "Er Tian Ru"
"""
from army import Army, Fighter, Soldier, Archer, Cavalry
from stack_adt import ArrayStack


class Battle:
    DRAW = 0
    PLAYER_ONE_WIN = 1
    PLAYER_TWO_WIN = 2
    STACK_FORMATION = 0
    QUEUE_FORMATION = 1

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """ Initialises an army for each player and sets them stack formation.
        Returns the winner after combat.

        :param player_one: name of player 1
        :param player_two: name of player 2
        :complexity: Best O(1) if either one army is empty,
                    worst O(n1*k), where n1 is the length of army.force, and
                    k is amount of life each unit has
        """
        army1 = Army()
        army1.choose_army(player_one, self.STACK_FORMATION)

        army2 = Army()
        army2.choose_army(player_two, self.STACK_FORMATION)

        return self.__conduct_combat(army1, army2, self.STACK_FORMATION)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """ Initialises an army for each player and sets them queue formation.
        Returns the winner after combat.

        :param player_one: name of player 1
        :param player_two: name of player 2
        :complexity: Best O(1) if either one army is empty,
                    worst O(n1*k), where n1 is the length of army.force, and
                    k is amount of life each unit has
        """
        army1 = Army()
        army1.choose_army(player_one, self.QUEUE_FORMATION)

        army2 = Army()
        army2.choose_army(player_two, self.QUEUE_FORMATION)

        return self.__conduct_combat(army1, army2, self.QUEUE_FORMATION)

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """ conducts combat based on the formation. Determines and returns winner after combat.

        :param army1: Army of player 1
        :param army2: Army of player 2
        :param formation: formation
        :complexity: Best O(1) if either one army is empty,
                    worst O(n1*k), where n1 is the length of army.force, and
                    k is amount of life each unit has
        """

        if formation == self.STACK_FORMATION:
            self.stack_combat(army1, army2)
        elif formation == self.QUEUE_FORMATION:
            self.queue_combat(army1, army2)

        if army2.force.is_empty() and not army1.force.is_empty():
            winner = self.PLAYER_ONE_WIN
        elif army1.force.is_empty() and not army2.force.is_empty():
            winner = self.PLAYER_TWO_WIN
        elif army1.force.is_empty() and army2.force.is_empty():
            winner = self.DRAW
        else:
            raise Exception("error in __conduct_combat(): army1 and army2 both not empty")

        return winner

    def stack_combat(self, army1: Army, army2: Army) -> None:
        """ combat with stack formation

        :param army1: Army of player 1
        :param army2: Army of player 2
        :complexity: Best O(1) if either one army is empty,
                    worst O(n1*k), where n1 is the length of army.force, and
                    k is amount of life each unit has
        """
        while not army1.force.is_empty() and not army2.force.is_empty():
            unit1 = army1.force.pop()
            unit2 = army2.force.pop()

            self.unit_fight(unit1, unit2)

            if unit1.is_alive() and unit2.is_alive():
                unit1.lose_life(1)
                unit2.lose_life(1)
                army1.force.push(unit1)
                army2.force.push(unit2)
            elif unit1.is_alive() and not unit2.is_alive():
                unit1.gain_experience(1)
                army1.force.push(unit1)
            elif not unit1.is_alive() and unit2.is_alive():
                unit2.gain_experience(1)
                army2.force.push(unit2)

    def queue_combat(self, army1: Army, army2: Army) -> None:
        """ combat with queue formation

        :param army1: Army of player 1
        :param army2: Army of player 2
        :complexity: Best O(1) if either one army is empty,
                    worst O(n1*k), where n1 is the length of army.force, and
                    k is amount of life each unit has
        """
        while not army1.force.is_empty() and not army2.force.is_empty():
            unit1 = army1.force.serve()
            unit2 = army2.force.serve()

            self.unit_fight(unit1, unit2)

            if unit1.is_alive() and unit2.is_alive():
                unit1.lose_life(1)
                unit2.lose_life(1)
                army1.force.append(unit1)
                army2.force.append(unit2)
            elif unit1.is_alive() and not unit2.is_alive():
                unit1.gain_experience(1)
                army1.force.append(unit1)
            elif not unit1.is_alive() and unit2.is_alive():
                unit2.gain_experience(1)
                army2.force.append(unit2)

    def unit_fight(self, unit1: Fighter, unit2: Fighter) -> None:
        """ combat between two units

        :param unit1: unit of player 1
        :param unit2: unit of player 2
        :complexity: Best = Worst = O(1)
        """
        if unit1.get_speed() > unit2.get_speed():
            unit2.defend(unit1.get_attack_damage())
            if unit2.is_alive():
                unit1.defend(unit2.get_attack_damage())
        elif unit1.get_speed() == unit2.get_speed():
            unit1.defend(unit2.get_attack_damage())
            unit2.defend(unit1.get_attack_damage())
        elif unit1.get_speed() < unit2.get_speed():
            unit1.defend(unit2.get_attack_damage())
            if unit1.is_alive():
                unit2.defend(unit1.get_attack_damage())
