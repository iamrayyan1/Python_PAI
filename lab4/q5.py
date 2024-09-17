class restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = {}
        
    def add_item_to_menu(self,item,price):
        self.menu_items[item] = price
        print(f"Item {item} added to menu with price {price}")
        
    def book_tables(self,customer_name, table_number):
        if table_number not in self.book_table:
            self.book_table.append(table_number)
            print(f"table {table_number} has been booked for {customer_name}")
        else:
            print(f"table {table_number} is already bookes")
            
    def customer_order(self,customer_name, items):
        if customer_name not in self.customer_orders:
            self.customer_orders[customer_name]=[] 
        self.customer_orders[customer_name].extend(items) 
        print(f"Order for {customer_name} added: {items}")
        
    def print_menu(self):
        print("\n-----Menu-----")
        for item,price in self.menu_items.items(): 
            print(f"{item},{price}")
        
        
    def print_table_reservations(self):
        print("\n---table reservations---")
        for table in self.book_table:
            print(f"table {table} is reserved")
      
    
    def print_customer_order(self):
        print("\n---customer order---")
        for customer, orders in self.customer_orders.items():
            print(f"{customer} ordered: {orders}")
        
        

xanders = restaurant() 
xanders.add_item_to_menu("beef burger",1200)
xanders.add_item_to_menu("pizza",1100)
xanders.add_item_to_menu("pasta",600)
xanders.add_item_to_menu("fries",2000)
xanders.add_item_to_menu("juice",400)

xanders.book_tables("ahmed",4)
xanders.book_tables("Manahil",8)
xanders.book_tables("ali",2)

xanders.customer_order("Manahil",["pasta"," fries","juice"])
xanders.customer_order("ali",["beef burger","fries"])

xanders.print_menu()
xanders.print_table_reservations()
xanders.print_customer_order()
