"""
This is a file to test the Subscription class of the Subcription subsystem.
Author: Author: Edson Alvarez - edisonalaverzv10@gmail.com
"""

import pytest
from unittest.mock import MagicMock
from workshop_pro.core_subsystem.user_authentication import User
from workshop_pro.vehicles_subsystem.vehicle import Vehicle
from workshop_pro.workshop_pro.subscription_subsystem.subcription import Subscription

class TestSubscription:
    """This class tests the Subscription class"""

    @pytest.fixture
    def subscription(self):
        """Fixture to create a Subscription instance"""
        return Subscription()

    @pytest.fixture
    def user(self):
        """Fixture to create a User instance"""
        user = MagicMock(spec=User)
        user.username = "test_user"
        return user

    @pytest.fixture
    def vehicle(self):
        """Fixture to create a Vehicle instance"""
        vehicle = MagicMock(spec=Vehicle)
        vehicle.__str__.return_value = "Test Vehicle"
        return vehicle

    def test_add_subscriber(self, subscription, user):
        """Test adding a subscriber"""
        subscription.add_subscriber(user)
        assert user in subscription.subscribers

    def test_add_existing_subscriber(self, subscription, user, capsys):
        """Test adding an existing subscriber"""
        subscription.add_subscriber(user)
        subscription.add_subscriber(user)
        captured = capsys.readouterr()
        assert "Subscriber test_user is already in the list." in captured.out

    def test_remove_subscriber(self, subscription, user, capsys):
        """Test removing a subscriber"""
        subscription.add_subscriber(user)
        subscription.remove_subscriber(user.username)
        assert user not in subscription.subscribers
        captured = capsys.readouterr()
        assert "Subscriber test_user removed." in captured.out

    def test_remove_nonexistent_subscriber(self, subscription, user, capsys):
        """Test removing a non-existent subscriber"""
        subscription.remove_subscriber(user.username)
        captured = capsys.readouterr()
        assert "Subscriber test_user not found." in captured.out

    def test_add_vehicle(self, subscription, vehicle, capsys):
        """Test adding a vehicle to the newsletter vehicles"""
        subscription.add_vehicle(vehicle)
        assert vehicle in subscription.newsletter_vehicles
        captured = capsys.readouterr()
        assert "Vehicle Test Vehicle added to newsletter vehicles." in captured.out

    def test_send_newsletter(self, subscription, user, vehicle, capsys):
        """Test sending a newsletter"""
        subscription.add_subscriber(user)
        for _ in range(5):
            subscription.add_vehicle(vehicle)
        subscription.send_newsletter()
        captured = capsys.readouterr()
        assert "Sending newsletter vehicles to subscribers." in captured.out
        assert f"Newsletter sent to {user}." in captured.out

    def test_send_newsletter_few_vehicles(self, subscription, user, vehicle, capsys):
        """Test sending a newsletter with fewer than 5 vehicles"""
        subscription.add_subscriber(user)
        subscription.add_vehicle(vehicle)
        subscription.send_newsletter()
        captured = capsys.readouterr()
        assert "Sending entire catalog to subscribers." in captured.out
        assert f"Newsletter sent to {user}." in captured.out
