from math import inf
from programm_modules import promotion

class Product:
  """Contains all data and functions, to interact with a specific type of product"""
  def __init__(self, name:str, price:float, quantity, active:bool=True, promotion=None):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.active = active
    self._promotion = promotion

    # self.name exceptions
    # is name a str?
    if not isinstance(self.name, str):
      raise TypeError("Error: Name must be a string!")

    # is name empty?
    if len(self.name) == 0:
      raise ValueError("Error: Name must be an empty string")

    # self.price exceptions
    # is price a float?
    if isinstance(self.price, int):
      self.price = float(self.price)
    elif not isinstance(self.price, float):
      raise ValueError("Error: Price must be a float number!")

    # is price negative?
    if self.price < 0:
      raise ValueError("Error: Price must not be negative!")

    # self.quantity exceptions
    self._validade_quanity()


  def _validade_quanity(self):
    # is quantity an int or a flaot
    if not isinstance(self.quantity, int) and not isinstance(self.quantity, float):
      raise ValueError("Error: Quantity must be an integer!")



    # is quantity negative?
    if self.quantity < 0:
      raise ValueError("Error: Quantity must not be negative")

  @property
  def quantity(self):
    return self._quantity

  @quantity.setter
  def quantity(self, value):
    """sets self.quantity"""
    if not isinstance(value, int) and not isinstance(value, float):
      raise ValueError("Quantity must be an integer or float!")

    if value < 0:
      raise ValueError("Quantity must not be negative!")

    self._quantity = value

    if self._quantity == 0:
      self.active = False


  def is_active(self):
    """shows, if the instace is active or not"""
    return self.active


  def activate(self):
    """activates the instace"""
    self.active = True


  def deactivate(self):
    """deactivates the instace"""
    self.active = False


  def show(self):
    """shows the instace-variable values of name, price and quanity"""

    if isinstance(self._promotion, promotion.Promotion):
      return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self._promotion}"

    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


  def buy(self, quantity) -> float:
    """executes a 'buy' action for the product. checks if given quanity is valid calculates new quanity of the product"""
    total_price = self.price * quantity

    # reduces price by promotion
    # if self._promotion isinstance from Poromtion class
    if isinstance(self._promotion, promotion.Promotion):
      total_price = self._promotion.apply_promotion(self, quantity)

    if self.quantity < quantity:
      # exception will be risen by store.py:38
      raise ValueError(f"Not enough {self.name}´s in stock. Only {self.quantity} {self.name}´s left.")
    else:
      self.quantity -= quantity

    if self.quantity == 0:
      self.active = False
    # f"Total Price: {total_price}, new product quantiy: {self.quantity}"

    return total_price

  @property
  def promotion(self):
    return self._promotion

  @promotion.setter
  def promotion(self, new_promotion):
    if isinstance(new_promotion, promotion.Promotion):
      self._promotion = new_promotion

    else:
      raise TypeError("promotion must be a instance of the Promotion class")


class NonStockedProduct(Product):
  def __init__(self, name, price, quantity=inf,  active=True, promotion=None,):
    super().__init__(name, price, quantity, active, promotion)

    # self.quantity exceptions
    self._validade_quanity()


  def _validade_quanity(self):
    """if self.quantity is not 'inf' ValueError will be raised"""
    if not isinstance(self.quantity, float):
      raise ValueError("Quantity for digital products must always be 'inf'")

  def set_quantity(self, quantity):
    """self.quanity must not be changed"""
    raise AttributeError("Quantity for digital products must always be 'inf'")



class LimitedProduct(Product):
  def __init__(self, name, price, quantity, maximum, active=True, promotion=None):
    super().__init__(name, price, quantity, active, promotion)
    self._maximum = maximum


  @property
  def maximum(self):
    return self._maximum


  @maximum.setter
  def maximum(self, new_maximum):
    if new_maximum < 0:
      raise ValueError("Purchuasion must not be negative!")
    else:
      self._maximum = new_maximum


  def buy(self, quantity):
    """executes a 'buy' action for the product. checks if given quanity is valid calculates new quanity of the product"""
    super().buy(quantity)
    if quantity > self._maximum:
      raise f"{str(self).upper} can only purchuated {self._maximum} times!"





  # LimitedProduct weiter ausformulieren
  # purchased x times coden












