# Homework 2: Polymorphic Pets
We're going to create a small program to manage a pet hotel. Create a base class "Pet". It should have overridable 
methods to get "check_in_fee", returning the flat cost of booking a room, and "nightly_fee", that is how much it costs
to house that type of pet per-night.

Our hotel supports 3 different kinds of pets: Cats, Dogs, and Birds. Cats cost $40 at check-in and $10 per night, Dogs
cost $30 at check-in and $30 per night, and Birds cost $10 at check-in and $15 per night. Taxes apply. Each of these
pet classes should derive Pet, and be placed in its own file.

Your system should allow adding customers, adding pets for customers, calculating how much a customer owes after so 
many days, and removing users (once they've paid their tab of course). Consider using a dictionary to map customers
to lists of Pets.
