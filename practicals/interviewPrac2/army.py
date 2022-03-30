""" Implementation of parent Fighter class and its child classes

Defines an abstract parent class for fighter units and non-abstract
child classes for Soldier, Archer, and Cavalry.
"""
__author__ = "Er Tian Ru"

from abc import abstractmethod, ABC
from queue_adt import CircularQueue
from stack_adt import ArrayStack


class Fighter(ABC):
    """ Abstract parent class Fighter """

    def __init__(self, life: int, experience: int) -> None:
        """ Initializes a new fighter

        :param arg1: unit life
        :param arg2: unit experience
        :pre: life and experience must be >= 0.
        """
        if life < 0:
            raise ValueError()
        elif experience < 0:
            raise ValueError()

        self.life = life
        self.experience = experience
        self.speed = 0
        self.attack_damage = 0

    def is_alive(self) -> bool:
        """ Returns True if the fighter’s life is greater than 0.

        :complexity: Best = Worst = O(1)
        """
        return self.life > 0

    def lose_life(self, lost_life: int) -> None:
        """ decreases life of fighter by the amount indicated by lost life.

        :param arg1: lost life (life to be deducted)
        :pre: lost_life must be >= 0
        :complexity: Best = Worst = O(1)
        """
        if lost_life < 0:
            raise ValueError()
        self.life -= lost_life

    def get_life(self) -> int:
        """ returns the fighter's life.

        :complexity: Best = Worst = O(1)
        """
        return self.life

    @abstractmethod
    def gain_experience(self, gained_experience: int) -> None:
        """ increases the experience of the unit by the amount indicated by gained experience.

        :param arg1: experience gained
        :pre: gained_experience must be >= 0
        :complexity: Best = Worst = O(1)
        """
        if gained_experience < 0:
            raise ValueError()
        self.experience += gained_experience

    def get_experience(self) -> int:
        """ returns the experience of the unit.

        :complexity: Best = Worst = O(1)
        """
        return self.experience

    def get_speed(self) -> int:
        """returns the speed of the unit.

        :complexity: Best = Worst = O(1)
        """
        return self.speed

    def get_cost(self) -> int:
        """returns the cost of the unit.

        :complexity: Best = Worst = O(1)
        """
        return self.COST

    def get_attack_damage(self) -> int:
        """ returns the amount of damage performed by the unit when it attacks.

        :complexity: Best = Worst = O(1)
        """
        return self.attack_damage

    @abstractmethod
    def defend(self, damage: int) -> None:
        """ Evaluates the life lost after defence expression and changes life accordingly.

        :param arg1: damage done on unit
        :pre: damage must be >= 0.
        :complexity: Best = Worst = O(1)
         """
        if damage < 0:
            raise ValueError()

    def get_unit_type(self) -> str:
        """ returns unit type of fighter

         :complexity: Best = Worst = O(1)
         """
        return self.UNIT_TYPE

    def __str__(self) -> str:
        """ returns a string indicating the type of unit, its current life and experience

        :complexity: Best = Worst = O(1)
        """
        return '{}\'s life = {} and experience = {}'.format(self.get_unit_type(), self.life, self.experience)


class Soldier(Fighter):
    """ Child class Soldier of parent Fighter """

    COST = 1
    UNIT_TYPE = "Soldier"

    def __init__(self) -> None:
        """ Initializes a new Soldier """
        Fighter.__init__(self, 3, 0)
        self.speed = 1 - self.get_experience()
        self.attack_damage = 1 + self.get_experience()

    def calculate_speed(self) -> int:
        """ calculates speed

        :complexity: Best = Worst = O(1)
        """
        return 1 - self.get_experience()

    def calculate_attack_damage(self) -> int:
        """ returns the amount of damage performed by the unit when it attacks.

        :complexity: Best = Worst = O(1)
        """
        return 1 + self.get_experience()

    def gain_experience(self, gained_experience: int) -> None:
        """ increases the experience of the unit by the amount indicated by gained experience.

        :param arg1: experience gained
        :pre: gained_experience must be >= 0
        :complexity: Best = Worst = O(1)
        """
        Fighter.gain_experience(self, gained_experience)
        self.speed = self.calculate_speed()
        self.attack_damage = self.calculate_attack_damage()

    def defend(self, damage: int) -> None:
        """ Evaluates the life lost after defence expression and changes life accordingly.

        :param arg1: damage done on unit
        :pre: damage must be >= 0.
        :complexity: Best = Worst = O(1)
        """
        super(Soldier, self).defend(damage)
        lost_life = 0
        if damage > self.get_experience():
            lost_life = 1
        self.lose_life(lost_life)


class Archer(Fighter):
    """ Child class Archer of parent Fighter """

    COST = 2
    UNIT_TYPE = "Archer"

    def __init__(self) -> None:
        """ Initializes a new Soldier """
        Fighter.__init__(self, 3, 0)
        self.speed = 3
        self.attack_damage = (2 * self.get_experience()) + 1

    def calculate_attack_damage(self) -> int:
        """ returns the amount of damage performed by the unit when it attacks.

        :complexity: Best = Worst = O(1)
        """
        return (2 * self.get_experience()) + 1

    def gain_experience(self, gained_experience: int) -> None:
        """ increases the experience of the unit by the amount indicated by gained experience.

        :param arg1: experience gained
        :pre: gained_experience must be >= 0
        :complexity: Best = Worst = O(1)
        """
        Fighter.gain_experience(self, gained_experience)
        self.attack_damage = self.calculate_attack_damage()

    def defend(self, damage: int) -> None:
        """ Evaluates the life lost after defence expression and changes life accordingly.

        :param arg1: damage done on unit
        :pre: damage must be >= 0.
        :complexity: Best = Worst = O(1)
        """
        super(Archer, self).defend(damage)
        lost_life = 1
        self.lose_life(lost_life)


class Cavalry(Fighter):
    """ Child class Cavalry of parent Fighter """

    COST = 3
    UNIT_TYPE = "Cavalry"

    def __init__(self) -> None:
        """ Initializes a new Soldier """
        Fighter.__init__(self, 4, 0)
        self.speed = 2 + self.get_experience()
        self.attack_damage = 1 + self.get_experience()

    def calculate_speed(self) -> int:
        """ calculates speed

        :complexity: Best = Worst = O(1)
        """
        return 2 + self.get_experience()

    def calculate_attack_damage(self) -> int:
        """ returns the amount of damage performed by the unit when it attacks.

        :complexity: Best = Worst = O(1)
        """
        return 1 + self.get_experience()

    def gain_experience(self, gained_experience: int) -> None:
        """ increases the experience of the unit by the amount indicated by gained experience.

        :param arg1: experience gained
        :pre: gained_experience must be >= 0
        :complexity: Best = Worst = O(1)
        """
        Fighter.gain_experience(self, gained_experience)
        self.speed = self.calculate_speed()
        self.attack_damage = self.calculate_attack_damage()

    def defend(self, damage: int) -> None:
        """ Evaluates the life lost after defence expression and changes life accordingly.

        :param arg1: damage done on unit
        :pre: damage must be >= 0.
        :complexity: Best = Worst = O(1)
        """
        super(Cavalry, self).defend(damage)
        lost_life = 0
        if damage > (self.get_experience() / 2):
            lost_life = 1
        self.lose_life(lost_life)


class Army:
    def __init__(self) -> None:
        """ Initializes a new Army """
        self.name = None
        self.force = None
        self.budget = 30

    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
        """ returns True if the total costs of the units provided are less than or equal the allocated budget

        :param arg1: number of soldiers
        :param arg2: number of archers
        :param arg3: number of cavalry
        :complexity: Best = Worst = O(1)
        """
        total_cost = (soldiers * Soldier.COST) + (archers * Archer.COST) + (cavalry * Cavalry.COST)
        return total_cost <= self.budget

    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int) -> None:
        """ Sets formation of an army to stack (formation = 0) or queue (formation = 1) form and binds the name and force
        variables.

        :param arg1: name of player
        :param arg2: number of soldiers
        :param arg3: number of archers
        :param arg4: number of cavalry
        :param arg4: type of formation (stack formation = 0, queue formation = 1)
        :complexity: Best = Worst = O(n)
        """
        stack_formation = 0
        queue_formation = 1
        self.name = name

        num_fighers = sold + arch + cav
        if formation == stack_formation:
            self.force = ArrayStack(num_fighers)

            for i in range(cav):
                c = Cavalry()
                self.force.push(c)
            for i in range(arch):
                a = Archer()
                self.force.push(a)
            for i in range(sold):
                s = Soldier()
                self.force.push(s)
        elif formation == queue_formation:
            self.force = CircularQueue(num_fighers)

            for i in range(cav):
                c = Cavalry()
                self.force.append(c)
            for i in range(arch):
                a = Archer()
                self.force.append(a)
            for i in range(sold):
                s = Soldier()
                self.force.append(s)
        else:
            raise Exception('invalid formation')

    def choose_army(self, name: str, formation: int) -> None:
        """ Reads 3 integers, s, a, c (number of soldiers, archers, and cavalry wanted) and assigns the army.

        :param arg1: name of player
        :param arg2: type of formation (stack formation = 0, queue formation = 1)
        :complexity: Best = Worst = O(1)
        """
        while True:

            print("\nPlayer " + name + " choose your army as S A C\n"
                                       "where S is the number of soldiers\n"
                                       "      A is the number of archers\n"
                                       "      C is the number of cavalries")
            try:
                s = int(input("S: "))
                a = int(input("A: "))
                c = int(input("C: "))
            except ValueError as e:
                print("S, A and C must be an integer")
            else:
                if self.__correct_army_given(s, a, c):
                    self.__assign_army(name, s, a, c, formation)
                    break
                else:
                    print('total costs of units exceeded budget of 30 money')

    def __str__(self) -> str:
        """returns a string containing the information of each army element in force.

        :complexity: Best = Worst = O(n)
        """
        string = ""
        if self.force is None:
            return string

        for i in range(len(self.force) - 1, -1, -1):
            string += '{}\'s life = {} and experience = {},'.format(self.force[i].get_unit_type(),
                                                                    self.force[i].get_life(),
                                                                    self.force[i].get_experience())
        return string[:-1]
