from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._score = 0
        self._lives = MAXIMUM_LIVES
        self._volleys = 0
    
    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1

    def add_score(self):
        """Adds the given points to the score."""
        self._score +=1

    def add_volley(self):
        """Adds a volley to the volleys count"""
        self._volleys += 1

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def get_score(self):
        """Gets the score.

        Returnss:
            A number representing the score.
        """
        return self._score

    def get_volleys(self):
        """Gets number of volleys.

        Returns:
            The number of volleys.
        """
        return self._volleys

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1

    def reset_volleys(self):
        """Resets volleys to zero."""
        self._volleys = 0   


    def reset(self):
        """Resets the stats back to their default values."""

        self._score = 0
        self._lives = DEFAULT_LIVES
        self._volleys = 0
 