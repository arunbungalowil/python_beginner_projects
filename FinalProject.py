import Database as db
import DocumentWrite as dw
import DictionaryOp as do
db_connection = db.DatabaseConnection('clarity_test_1.db') # create a database object
db_connection.connection()                               # connect to the database

user_input= int(input('Enter 1 for getting a document for your quote number\nEnter 2 for getting a predifined document'))
if user_input == 1:
    customer_quote_id = input('Enter the quote number')      # collect the quote number from the user it is a combination of user id and cart id
    if len(customer_quote_id) != 12:
       raise Exception('Quote id must be 12 character long')
    else:
        customer_user_id = customer_quote_id[:6].lstrip('0')  # first 6 characters represent the user id, and removing the zeros at the left side
        customer_cart_id = customer_quote_id[6:].lstrip('0')  # remaining 6 characters represent the cart id and removing the zeros at the left side

elif user_input == 2:
    customer_user_id = "1001"  # if user gives no quote id use the default user id and cart id
    customer_cart_id = "1"
query_user = '''
SELECT
    ci.CUSTOMER_FIRST_NAME,
    ci.CUSTOMER_LAST_NAME,
    ci.CUSTOMER_TITLE,
    ci.CUSTOMER_E_MAIL_ADDR,
    ci.CUSTOMER_COMPANY,
    ci.CUSTOMER_ADDR1,
    ci.CUSTOMER_ADDR2,
    ci.CUSTOMER_CITY,
    ci.CUSTOMER_STATE,
    ci.CUSTOMER_PROVINCE,
    ci.CUSTOMER_COUNTRY,
    ci.CUSTOMER_ZIP_CODE,
    ci.CUSTOMER_BUSINESS_PHONE,
    ci.customer_code
FROM CUSTOMER_INFO AS ci
WHERE ci.CUSTOMER_ID = ?;
'''
query_cart = '''
SELECT
    c.CUSTOMER_ID ,
    c.DATE_ORDERED,
    c.ORDER_STATUS,
    c.SHIPPING_METHOD,
    c.CART_COMMENT,
    c.PAYMENT_METHOD,
    c.PAYMENT_APROOVED,
    c.TOTALAMOUNT,
    c.currency_quote,
    c.send_email_end_user,
    c.Origin,
    c.MY_BILL_TO,
    c.MY_SHIP_TO,
    c.SHIPPING_COST
FROM  CART AS c 
WHERE c.USERID = ? AND c.CART_ID = ?;
'''
query_cart_item = '''
SELECT
    ci.CATALOGCODE,
    ci.DESCRIPTION,
    ci.USER_DESCRIPTION,
    ci.DESCRIPTION_LONG,
    ci.BASE_QUANTITY,
    ci.NETPRICE,
    ci.RecurringPrice,
    ci.CURRENCY,
    ci.PRODUCT_WEIGHT,
    ci.UnitOfMeasure,
    ci.ITEM_DELIVERY_STATUS,
    ci.ITEM_DELIVERY_METHOD
FROM  CART_ITEM AS ci 
WHERE ci.USERID = ? AND ci.CART_ID = ?;
'''


cart_data = db_connection.database_execute_query(query_cart,customer_user_id, customer_cart_id)
customer_id = cart_data[0][0]
query_cart_item_data = db_connection.database_execute_query(query_cart_item,customer_user_id,customer_cart_id)
user_data = db_connection.database_execute_query(query_user, customer_id) 
print(customer_user_id)
print(customer_cart_id)
print(customer_id)

create_dict = do.CreateDictionary()
user_cart_dict = create_dict.dictionary_operation(user_data,cart_data)
print(user_cart_dict)
print(query_cart_item_data)
document_write = dw.DocumentWrite(user_cart_dict,query_cart_item_data,customer_user_id,customer_cart_id)
document_write.write_quote_number()
document_write.open_document()
document_write.write_data_to_first_table()
document_write.add_first_paragraph()
document_write. order_table_create()
document_write.add_second_paragraph()
document_write.write_data_to_third_table()
document_write.save_document()
db_connection.database_disconnect()
###################################################################################################################



   
   