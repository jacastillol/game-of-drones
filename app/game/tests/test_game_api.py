from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Player

from game.serializers import PlayerSerializer


PLAYERS_URL = reverse('game:player-list')


class PublicGameApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_players(self):
        """Test retrieving all players"""
        Player.objects.create(name='Mayita', victories=0,
                              defeats=0)
        Player.objects.create(name='Moiso', victories=0,
                              defeats=0)

        res = self.client.get(PLAYERS_URL)

        players = Player.objects.all().order_by('-name')
        serializer = PlayerSerializer(players, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_player_successful(self):
        """Test creating a new player"""
        payload = {'name': 'Mayita', 'victories': 0, 'defeats': 0}
        self.client.post(PLAYERS_URL, payload)

        print('PLAYERS_URL: ',PLAYERS_URL)
        exists = Player.objects.filter(
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_player_invalid(self):
        """Test creating a new player with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(PLAYERS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
