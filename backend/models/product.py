from backend.db_config import connect_db

class Product:
    def __init__(self, name, category, price, stock_quantity) :
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def add_product(self):
        conn = connect_db()
        try: 
            cursor = conn.cursor()
            query = """INSERT INTO Products(name, category, price, stock_quantity)
                       Values (?, ?, ?, ?)"""
            cursor.execute(query, (self.name, self.category, self.price, self.stock_quantity))
            conn.commit()
            print("Product added Successfully.")
        except Exception as e:
            print('Failed to add product:', e)
        finally:
            if conn:
                conn.close()
        
    @staticmethod
    def view_all_products():
        conn = connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print('Failed to fetch all products', e)

        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete_product(product_id):
        conn = connect_db()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Products WHERE product_id = ?", (product_id))
            conn.commit()
            print('Product deleted successfully.')
        except Exception as e:
            print('Failed to delete product:',e)
        finally:
            if conn:
                conn.close()