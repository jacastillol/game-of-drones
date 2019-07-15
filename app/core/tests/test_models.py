from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_player_str(self):
        """Test the player string representation"""
        player = models.Player.objects.create(
            name='Mayita',
            victories=0,
            defeats=0
        )
        self.assertEqual(str(player),
                         '({}|{}|{})'
                         .format(player.name,
                                 player.victories,
                                 player.defeats))

    def test_defeated_player_and_is_counted(self):
        """Test the defaets' player value is incresed when fail the match"""
        player = models.Player.objects.create(
            name='Mayita',
            victories=0,
            defeats=0
        )
        defeats = player.defeats
        player.defeated()
        self.assertEqual(player.defeats, defeats+1)

    def test_victorious_player_and_is_counted(self):
        """Test the victories' player value is incresed when fail the match"""
        player = models.Player.objects.create(
            name='Mayita',
            victories=0,
            defeats=0
        )
        victories = player.victories
        player.won()
        self.assertEqual(player.victories, victories+1)
