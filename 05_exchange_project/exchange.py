import random

class Player:
    def __init__(self, name:str, cash:float, inventory: dict):
        self.name = name
        self.cash = cash
        self.inventory = inventory


    def show_balance(self):
        return f"Игрок {self.name}. Наличные: {self.cash:.2f}$. Активы: {self.inventory}"




class Asset:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def update_price(self):
        change = random.uniform(-0.1, 0.1)
        self.price = self.price * (1 + change)
        if self.price < 1.0:
            self.price = 1.0


gamer = Player('Иван', 1000.00, {})
gold = Asset("Gold", 100.00)
oil = Asset("Oil", 50.0)
crypto = Asset("Crypto", 50.0)

def buy_asset(player:Player, asset: Asset, quantity:int) -> bool:

    total = asset.price * quantity
    if player.cash >= total:
        player.cash -= total
        if asset.name in player.inventory:
            player.inventory[asset.name] += quantity
        else:
            player.inventory[asset.name] = quantity

        return True
    return False


print(buy_asset(gamer, gold, 5))


def sell_asset(player: Player, asset: Asset, quantity : int) -> bool:
    if asset.name not in player.inventory:
        return False

    if player.inventory[asset.name] < quantity:
        return False

    player.cash += asset.price * quantity
    player.inventory[asset.name] -= quantity

    if player.inventory[asset.name] == 0:
        del player.inventory[asset.name]

    return True

print(sell_asset(gamer, gold, 3))
