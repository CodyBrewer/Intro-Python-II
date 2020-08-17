class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.take_message = 'You place ' + name + ' in your backpack.'
        self.drop_message = 'You drop ' + name + ' in the cave.'        

    def __str__(self):
        return f'{self.name}, {self.description}'

    def on_take_room(self, player):
        print('heloo')
        print(f'\n{self.take_message}')
        player.items.append(self)
        player.room.items.remove(self)

    def on_drop_room(self, player):
        print(f'\n{self.drop_message}')
        player.room.items.append(self)
        player.items.remove(self)