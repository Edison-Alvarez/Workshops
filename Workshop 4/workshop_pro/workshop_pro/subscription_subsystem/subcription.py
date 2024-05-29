"""
This module contains the Subscription class

Author: Edison Alvarez - edisonalaverzv10@gmail.com
"""
from ..core_subsystem import User
from ..vehicles_subsystem import Vehicle


class Subscription:
    """
    Manages subscribers and newsletter shipments for a vehicle catalog.

    Attributes:
        subscribers (list of str): A list of usernames who are subscribed to the newsletter.
        newsletter_vehicles (list of Vehicle): A list of the latest vehicles created.
    """

    def __init__(self):
        self.subscribers = []
        self.newsletter_vehicles = []

    def add_subscriber(self, user: User):
        """
        Adds a subscriber to the list.

        Args:
            username (str): The username of the subscriber to add.
        """
        if user not in self.subscribers:
            self.subscribers.append(user)
            print(f"Subscriber {user.username} added.")
        else:
            print(f"Subscriber {user.username} is already in the list.")

    def remove_subscriber(self, username: str):
        """
        Removes a subscriber from the list.

        Args:
            username (str): The username of the subscriber to remove.
        """
        for user in self.subscribers:
            if username == user.username:
                self.subscribers.remove(user)
                print(f"Subscriber {user.username} removed.")
            else:
                print(f"Subscriber {user.username} not found.")

    def add_vehicle(self, vehicle: Vehicle):
        """
        Adds a newly created vehicle to the list of newsletter_vehicles.

        Args:
            vehicle (Vehicle): The vehicle object to add.
        """
        self.newsletter_vehicles.append(vehicle)
        print(f"Vehicle {vehicle} added to newsletter vehicles.")

    def send_newsletter(self):
        """
        Sends a newsletter to all subscribers.

        Determines the number of vehicles in newsletter_vehicles. If it is less than 5,
        sends the entire catalog list; otherwise, only sends the newsletter_vehicles list.
        """
        if len(self.newsletter_vehicles) < 5:
            print("Sending entire catalog to subscribers.")
            # Logic to send the entire catalog
        else:
            print("Sending newsletter vehicles to subscribers.")
            # Logic to send only the newsletter_vehicles list

        # Simulating the sending process
        for subscriber in self.subscribers:
            print(f"Newsletter sent to {subscriber}.")
