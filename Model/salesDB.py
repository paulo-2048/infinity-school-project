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
            return True
        except Error as e:
            print(e)
            pass

    def listing(self):
        try:
            sql = 'SELECT * FROM  Sales_management'
            command = self.conecction.cursor()
            command.execute(sql)
            rows = command.fetchall()
            return rows
        except Error as e:
            print(e)
            pass

    def delete_data(self, idCode):
        try:
            sql = 'DELETE from Sales_management WHERE idCode = %s;'
            command = self.conecction.cursor()
            command.execute(sql, (idCode,))
            self.conecction.commit()
            return True
        except Error as e:
            print(e)
            pass

    def update_data(self, column, value, idCode):
        try:
            if column == 1:
                sql = 'UPDATE Sales_management SET Product_name = %s WHERE idCode = %s ;'
                command = self.conecction.cursor()
                command.execute(sql, (value, idCode))
                self.conecction.commit()
            if column == 2:
                sql = 'UPDATE Sales_management SET Price_products = %s WHERE idCode = %s ;'
                command = self.conecction.cursor()
                command.execute(sql, (value, idCode))
                self.conecction.commit()
            if column == 3:
                sql = 'UPDATE Sales_management SET Product_category = %s WHERE idCode = %s;'
                command = self.conecction.cursor()
                command.execute(sql, (value, idCode))
                self.conecction.commit()
                return True
        except Error as e:
            print(e)
            pass
