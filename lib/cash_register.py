#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0
    pass
  def add_item(self, item, price, quantity=1):
    for _ in range(quantity):
      self.items.append(item)
    self.total = self.total + (price * quantity)
    self.last_transaction = price * quantity
    pass
  def apply_discount(self):
    self.total = self.total * (1 - self.discount/100)
    if self.discount > 0:
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    pass
  def void_last_transaction(self):
    self.total -= self.last_transaction
    self.last_transaction = 0
  pass
