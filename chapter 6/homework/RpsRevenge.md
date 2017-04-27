# Homework 1: Rock Paper Scissors Revenge
Starting from your previous Rock Paper Scissors game, add a menu with the following options:
1. New Player - Creates a persistent save slot for a new player
2. Delete Player - Deletes the save slot of an existing player
3. Play Game - Plays a round of Rock Paper Scissors against the computer
4. Score Board - Prints the wins and losses of all existing players

Whenever a new player is created, they should input a name and a save format (e.g.
plaintext/csv/xml/json/sql). You must support at least 2 formats. Every player has
persistent save data stored on disk. Wins and losses should be recorded there. 
Create a class for player, and polymorphic classes for save files. It may look
something like this:
```python
class Player:
    @property
    def name(self):
        # your implementation here...
        return 'name'

    @name.setter
    def name(self, value):
        # your implementation here...
        pass

    @property
    def score(self):
        # your implementation here...
        return 0

    @score.setter
    def score(self, value):
        # your implementation here...
        pass


class GameSaver:
    def save(self, player):
        pass

    def load(self, player):
        pass

    def delete(self, player):
        pass


class XmlGameSaver(GameSaver):
    def __init__(self):
        # your implementation here...
        pass

    def save(self, player):
        # your implementation here...
        pass

    def load(self, player):
        # your implementation here...
        pass

    def delete(self, player):
        # your implementation here...
        pass


class JsonGameSaver(GameSaver):
    def __init__(self):
        # your implementation here...
        pass

    def save(self, player):
        # your implementation here...
        pass

    def load(self, player):
        # your implementation here...
        pass

    def delete(self, player):
        # your implementation here...
        pass


def main():
    # get user input -> say load 'Bill'
    # check save file names for 'Bill.*' (* is a wildcard that matches any pattern, e.g. Bill.xml Bill.csv Bill.py)
    def get_saver(save_type):
        print('Detected save type', save_type)
        return {    # dictionary defined in place
            'xml': XmlGameSaver(),
            'json': JsonGameSaver(),
        }.get(save_type, None)  # use key of save_type; None if not found

    saver = get_saver('xml')
    saver.save('Player Object Here')

if __name__ == '__main__':
    main()

```
 
Your program should not crash, i.e. file IO errors should be handled gracefully
and reported back to the user. How you choose to store players and their scores within 
those constraints is entirely up to you.
