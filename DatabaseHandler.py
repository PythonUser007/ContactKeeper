import sqlite3

class Db_Functions:
    def table_creation(self):
        connection = sqlite3.connect('D:/Python/databases/Project.db')
        phonebook_cursor = connection.cursor()
        phonebook_cursor.execute('''
            CREATE TABLE PhoneBook(
               Name text,
               EmailId text,
               PhoneNo text
               )'''
                                 )
        print("Table created successfully!!!")
        connection.commit()
        connection.close()



    def insert_record(self, data_point):
        connection = sqlite3.connect('D:/Python/databases/Project.db')
        phonebook_cursor = connection.cursor()
        try:
            print("Trying to insert record...")
            phonebook_cursor.executemany("insert into PhoneBook values (?,?,?)", data_point)
            print("Record Inserted")
        except sqlite3.OperationalError:
            print("The table is not present. Going ahead with Table creation...")
            self.table_creation()
            print("Inserting Record...")
            phonebook_cursor.executemany("insert into PhoneBook values (?,?,?)", data_point)
            print("Record Inserted")
        finally:
            connection.commit()
            connection.close()

    def fetch_record(self, search_key):
        connection = sqlite3.connect('D:/Python/databases/Project.db')
        phonebook_cursor = connection.cursor()
        search_key = "%"+search_key+"%"
        result = []
        try:
            result = phonebook_cursor.execute("select * from PhoneBook where upper(Name) like ?", (search_key.upper(),))
        except sqlite3.OperationalError:
            return result
        else:
            result = result.fetchall()
            return result
        finally:
            connection.close()