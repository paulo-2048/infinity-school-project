from mysql.connector import Error


class Connection_to_manager:
    def __init__(self, conecction):
        self.conecction = conecction

    def insertProduct(self, sale):
        try:
            sql = 'INSERT INTO Sales_management (idCode, Product_name, Price_products, Product_category, Date) VALUES (%s, %s, %s, %s, now())'
            command = self.conecction.cursor()
            command.execute(sql, (sale.idCode, sale.name,
                            sale.price, sale.category))
            self.conecction.commit()
        except Error as e:
            print(e)
            pass

    def Listing(self):
        try:
            sql = 'SELECT * FROM  Sales_management'
            command = self.conecction.cursor()
            command.execute(sql)
            self.conecction.commit()
        except Error as e:
            print(e)
            pass

    def Delete_data(self, sale):
        try:
            sql = 'DELETE from Sales_management WHERE id = %s;'
            command = self.conecction.cursor()
            command.execute(sql(sale.idCode))
            self.conecction.commit()
        except Error as e:
            print(e)
            pass

    def Update_data(self, column, sale):
        try:
            if column == 1:
                sql = 'UPDATE Sales_management SET %s = %s WHERE idCode = %s ;'
                command = self.conecction.cursor()
                command.execute(sql('Product_name', sale.name, sale.idCode))
                self.conecction.commit()
            if column == 2:
                sql = 'UPDATE Sales_management SET %s = %s WHERE idCode = %s ;'
                command = self.conecction.cursor()
                command.execute(sql('Price_products', sale.price, sale.idCode))
                self.conecction.commit()
            if column == 3:
                sql = 'UPDATE Sales_management SET %s = %s WHERE idCode = %s ;'
                command = self.conecction.cursor()
                command.execute(
                    sql('Product_category', sale.category, sale.idCode))
                self.conecction.commit()
        except Error as e:
            print(e)
            pass
