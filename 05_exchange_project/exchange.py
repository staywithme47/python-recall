import os.path
import random
import json


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


def get_portfolio_value(player: Player, assets: list[Asset]) -> float:
    total = 0

    for item_name, qty in player.inventory.items():
        for asset in assets:
            if asset.name == item_name:
                total += asset.price * qty

    total += player.cash
    return total


def get_cheapest_asset(assets: list[Asset]) -> Asset | None:
    cheapest_asset = None

    for asset in assets:
        if cheapest_asset is None or asset.price < cheapest_asset.price:
            cheapest_asset = asset

    return cheapest_asset


def most_expensive_asset(assets: list[Asset]) -> Asset | None:
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


def create_new_game(player_name):
    player = Player(name=player_name, cash=1000.00, inventory={})
    assets = [Asset("Gold", 100.00), Asset("Oil", 50.0), Asset("Crypto", 10.0)]
    return player, assets


def save_game(player: Player, assets:list[Asset], filename = "savegame.json"):
    player_data = {"name": player.name, "cash": player.cash, "inventory" : player.inventory}
    inventory_assets = [{"name": x.name, "price": x.price} for x in assets]
    full_data = {"player": player_data, "assets": inventory_assets}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(full_data, f)
    return True


def load_game(filename: str) -> tuple[Player, list[Asset]]:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    player = Player(name= data["player"]["name"], cash= data["player"]["cash"], inventory= data["player"]["inventory"])
    assets = [Asset(name=x["name"], price=x["price"]) for x in data["assets"]]

    return player, assets


def play_game():
    player_name = input('Введите имя игрока:')
    save_file = f"{player_name}.json"

    if os.path.exists(save_file):
        ans = input("Найдено сохранение. Загрузить? (y/n): ")
        if ans.lower() == "y":
            player, assets = load_game(save_file)

        else:
            player, assets = create_new_game(player_name)
    else:
        player,assets = create_new_game(player_name)

    while True:
        for asset in assets:
            asset.update_price()
            print(f"{asset.name} : {asset.price: .2f}$")
        print(player.show_balance())
        action_str = input("Выберите действие: \n 1. Купить актив  \n 2. Продать актив \n 3. Пропустить ход \n 4. Выйти из игры")
        if not action_str.isdigit():
            print("Ошибка, введите число!")
            continue
        action = int(action_str)
        if action == 4:
            user_answer = input("Хотите сохранить прогресс: Y/N?")
            if user_answer.lower() == "y":
                save_game(player, assets, filename=save_file)
                print("Сохранено успешно")
            print("Выходим из игры")
            break
        elif action == 1:
            user_choice = input("Какой актив вы хотите купить? ")
            selected_asset = None

            for a in assets:
                if a.name.lower() == user_choice.lower():
                    selected_asset = a
                    break

            if selected_asset is None:
                print("Такого актива нет на рынке.")
            else:
                qty_str = input("Сколько единиц вы хотите купить? ")
                if not qty_str.isdigit():
                    print("Ошибка: нужно ввести число.")
                    continue

                qty = int(qty_str)
                if qty <= 0:
                    print("Количество должно быть больше нуля.")
                else:
                    if buy_asset(player, selected_asset, qty):
                        print("Успешная покупка!")
                    else:
                        print("Недостаточно средств!")


        elif action == 2:

            user_choice = input("Какой актив вы хотите продать? ")

            selected_asset = None

            for a in assets:

                if a.name.lower() == user_choice.lower():
                    selected_asset = a

                    break

            if selected_asset is None:
                print("Такого актива нет на рынке.")

            else:
                qty_str = input("Сколько единиц вы хотите продать? ")

                if not qty_str.isdigit():
                    print("Ошибка: нужно ввести число.")
                    continue

                qty = int(qty_str)

                if qty <= 0:
                    print("Количество должно быть больше нуля.")
                else:
                    if sell_asset(player, selected_asset, qty):
                        print("Успешная продажа!")
                    else:
                        print("У вас нет столько единиц этого актива!")
        elif action == 3:
            print("Ход пропущен")


if __name__ == "__main__":
    play_game()