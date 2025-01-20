# author : Manoj
# class : customer
class Customer:
    # __init__ method
    def __init__(self, customer_name, customer_email_id, customer_phone_number, customer_address, customer_pincode, product_code, product_description, product_quantity, purchase_date_time, amount, transaction_type, transaction_id):
        self.customer_name = customer_name
        self.customer_email_id = customer_email_id
        self.customer_phone_number = customer_phone_number
        self.customer_address = customer_address
        self.customer_pincode = customer_pincode
        self.product_code = product_code
        self.product_description = product_description
        self.product_quantity = product_quantity
        self.purchase_date_time = purchase_date_time
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_id = transaction_id

    #  __str__ method
    def __str__(self):
        return f"Customer[Name: {self.customer_name}, Email: {self.customer_email_id}, PhoneNumber: {self.customer_phone_number}, Address: {self.customer_address}, Pincode: {self.customer_pincode}, ProductCode: {self.product_code}, ProductDescription: {self.product_description}, ProductQuantity: {self.product_quantity}, PurchaseDateTime: {self.purchase_date_time}, Amout: {self.amount}, TransactionType: {self.transaction_type}, TrasanctionId: {self.transaction_id}]"
