inventory = {'Gold': 5, 'Oil': 0, 'Wood': 10}

def add_item(inventory, item, qty):
    tmp = inventory.get(item)
    if tmp is None:
        inventory[item] = qty
    else:
        inventory[item] += qty
    return inventory

#print(add_item(inventory, 'Gold', 7))

def remove_item(inventory, item, qty):
    tmp = inventory.get(item)
    if tmp is None or tmp - qty < 0:
        return inventory
    if tmp >= qty:
        inventory[item] -= qty
        if inventory[item] == 0:
             del inventory[item]

    return inventory

#print(remove_item(inventory, 'Gold', 7))

def get_item_count(inventory, item):
    return inventory.get(item, 0)

#print(get_item_count(inventory, 'Wood'))


prices = {"AAPL": 150, "TSLA": 800, "GOOG": 2800, "AMZN": 3400}

def get_most_expensive_asset(prices:dict) -> str:
    max_price = None
    max_name = ''
    for name, price in prices.items():
        if max_price is None or price > max_price:
            max_price = price
            max_name = name
    return max_name

#print(get_most_expensive_asset(prices))


inv1 = {"Gold": 3, "Silver":5}
inv2 = {"Silver": 2, "Bronze":10}

def merge_inventories(inv1, inv2) -> dict:
    merged_dict = {}
    for inv in (inv1, inv2):
        for name, count in inv.items():
            if name not in merged_dict:
                merged_dict[name] = count
            else:
                merged_dict[name] += count
    return merged_dict

#print(merge_inventories(inv1,inv2))

#pythonic shortcut
def merge_inventories2(inv1, inv2):
    merged_dict = {}
    for inv in(inv1,inv2):
        for name, count in inv.items():
            merged_dict[name] = merged_dict.get(name, 0) + count

    return merged_dict

#print(merge_inventories2(inv1, inv2))


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def count_words(words:list) -> dict:
    result = {}
    for el in words:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1


    return result

#print(count_words(words))

#pythonic trick

def count_words2(words:list) -> dict:
    result = {}
    for el in words:
        result[el] = result.get(el,0) + 1
    return result

#print(count_words2(words))

balances = {"Ivan": 100, "Petr": -50, "Anna": 0, "Oleg": 200, "Dima": -10}

def get_positive_balances(balances:dict) -> dict:
    positive = {}
    for name, balance in balances.items():
        if balance > 0:
            positive[name] = balance

    return positive

#print(get_positive_balances(balances))

def get_positive_balances2(balances:dict) -> dict:
    return {name:balance for name, balance in balances.items() if balance > 0 }

print(get_positive_balances2(balances))