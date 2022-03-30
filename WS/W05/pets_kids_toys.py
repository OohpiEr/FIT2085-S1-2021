""" Pets, Kids and Toys implementation.
"""
from abc import ABC, abstractmethod
import math


class PlayerIsNotCurrentlyPlaying(Exception):
    """ Exception raised when a Player is incorrectly
    assumed to be already playing."""

    def __init__(self):
        Exception.__init__(self)


class PlayableFull(Exception):
    def __init__(self):
        Exception.__init__(self)


class Player(ABC):
    pass


class Playable(ABC):
    def __init__(self, name, maxplayers: int = math.inf):
        self.name = name
        self.maxplayers = maxplayers
        self.players = []

    def add_player(self, player: Player):
        assert player is not None
        assert player.playing_with is not self
        if len(self.players) < self.maxplayers:
            self.players.append(player)
        else:
            raise PlayableFull()

    def remove_player(self, player: Player):
        assert player is not None
        assert player.playing_with is self
        self.players.remove(player)


class Player(ABC):
    """ A player can play or stop playing."""

    def __init__(self, name):
        self.name = name
        self.playing_with = None

    def play(self, playable: Playable) -> bool:
        if self.playing_with is not None:
            if self.playing_with is playable:
                return True
            else:
                self.stop_playing()

        try:
            playable.add_player(self)
            self.playing_with = playable
            print("{} is now playing with {}".format(self.name, playable.name))
            return True
        except PlayableFull:
            print("{} cannot play with {}".format(self.name, playable.name))
            return False

    def stop_playing(self):
        if self.playing_with is None:
            raise PlayerIsNotCurrentlyPlaying()
        self.playing_with.remove_player(self)
        print("{} has stopped playing with {}".format(self.name, self.playing_with.name))
        self.playing_with = None


class Kid(Player):
    def __init__(self, name) -> None:
        Player.__init__(self, name)


class Pet(Player, Playable):
    def __init__(self, name) -> None:
        Player.__init__(self, name)
        Playable.__init__(self, name)


class Toy(Playable):
    def __init__(self, name, maxplayers: int) -> None:
        Playable.__init__(self, name, maxplayers)


diamond = Pet("Diamond")
syscall = Pet("Syscall")

taylor = Kid("Taylor")
connect4 = Toy("connect4", 2)

taylor.play(diamond)
taylor.play(diamond)
taylor.play(syscall)

diamond.play(connect4)
taylor.play(connect4)
syscall.play(connect4)
taylor.stop_playing()
syscall.stop_playing()