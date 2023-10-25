# This class will create a dictionary from the information retrieved from the database
class CreateDictionary:
  def dictionary_operation(self, user_data, cart_data):
    self.user_data = user_data  # user data such as first name, last name.., this is a list of tuple
    self.cart_data = cart_data  # cart informations such as order status, shipping method etc.., this is a list of tuple
    self.user_data = [self.detail for self.detail in  self.user_data[0]] # list of tuple to list
    self.cart_data = [self.detail for self.detail in self.cart_data[0]]  # list of tuple to list
    self.user_cart = self.user_data  + self.cart_data  # combining user data and cart data list into a single list
    print(self.cart_data)
    print( self.user_cart)
    # dictionary keys
    self.user_columns = [
    'CUSTOMER FIRSTNAME',
    'CUSTOMER LASTNAME',
    'CUSTOMER TITLE',
    'CUSTOMER EMAIL-ADDR',
    'CUSTOMER COMPANY',
    'CUSTOMER ADDR1',
    'CUSTOMER ADDR2',
    'CUSTOMER CITY',
    'CUSTOMER STATE',
    'CUSTOMER PROVINCE',
    'CUSTOMER COUNTRY',
    'CUSTOMER ZIP-CODE',
    'CUSTOMER BUSINESS PHONE',
    'CUSTOMER CODE',
    'CUSTOMER ID',
    'DATE ORDERED',
    'ORDER STATUS',
    'SHIPPING METHOD',
    'CART COMMENT',
    'PAYMENT METHOD',
    'PAYMENT APROOVED',
    'TOTAL AMOUNT',
    'CURRENCY QUOTE',
    'SEND EMAIL END USER',
    'ORIGIN',
    'MY BILL TO',
    'MY SHIP TO',
    'SHIPPING_COST'
]
    self.user_cart_dict = dict(zip(self.user_columns, self.user_cart)) # zip function for combing both lists 
    return self.user_cart_dict
