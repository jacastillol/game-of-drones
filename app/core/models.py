from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)
    victories = models.IntegerField()
    defeats = models.IntegerField()

    def __str__(self):
        return f'({self.name}|{self.victories}|{self.defeats})'

    def defeated(self):
        """Increase number of defeats value"""
        self.defeats += 1

    def won(self):
        """Increase number of victories value"""
        self.victories += 1
