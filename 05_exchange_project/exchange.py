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


test_Gold = Asset("Gold", 100.00)
test_oil = Asset("Oil", 50.0)
test_crypto = Asset("Crypto", 10.0)
test_player = Player(name="Tester", cash=500.00, inventory={"Gold": 2, "Crypto": 5})

assets_list = [test_Gold, test_oil, test_crypto]

def get_portfolio_value(player: Player, assets: list[Asset]) -> float:
    total = 0

    for item_name, qty in player.inventory.items():
        for asset in assets:
            if asset.name == item_name:
                total += asset.price * qty

    total += player.cash
    return total


def get_cheapest_asset(assets: list[Asset]) -> Asset:
    cheapest_asset = None

    for asset in assets:
        if cheapest_asset is None or asset.price < cheapest_asset.price:
            cheapest_asset = asset

    return cheapest_asset


def most_expensive_asset(assets: list[Asset]) -> Asset:
    expensive_asset = None

    for asset in assets:
        if expensive_asset is None or asset.price > expensive_asset.price:
            expensive_asset = asset

    return expensive_asset


def get_average_price(assets: list[Asset]) -> float:
    avg = 0
    count = 0
    for asset in assets:
        avg += asset.price
        count += 1
    if count == 0:
        return 0.0

    return avg /count

