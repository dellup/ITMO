from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()


    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("free_cars.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не могу открыть базу данных",
                                           "Нажмите Cancel, чтобы выйти", QtWidgets.QMessageBox.Cancel)
            return False
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS free_cars (id INTEGER PRIMARY KEY AUTOINCREMENT, Type VARCHAR(30),"
                   "Load REAL, Length REAL, Weight REAL, Height REAL)")
        query.exec("CREATE TABLE IF NOT EXISTS busy_cars (id INTEGER PRIMARY KEY AUTOINCREMENT, Type VARCHAR(30),"
                   "Load REAL, Length REAL, Weight REAL, Height REAL)")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def clear_table(self, table_name):
        query = QtSql.QSqlQuery()
        query.exec(f"DELETE FROM {table_name}")

    def add_new_query(self, type, load, length, weight, height, table_name):
        sql_query = f"INSERT INTO {table_name} (Type, Load, Length, Weight, Height) VALUES (?, ?, ?, ?, ?)"
        query_values = [type, load, length, weight, height]
        self.execute_query_with_params(sql_query, query_values)

    def replace_query(self, num):
        query = QtSql.QSqlQuery()
        query.exec_(f"SELECT * FROM free_cars WHERE id = {num}")
        inf = []
        if query.next():
            for i in range(query.record().count()):
                value = query.value(i)
                inf.append(value)
        self.delete_query(num, "free_cars")
        self.add_new_query(inf[1], inf[2], inf[3], inf[4], inf[5], "busy_cars")

    def delete_query(self, id, table_name):
        sql_query = f"DELETE FROM {table_name} WHERE id = ?"
        query_values = [id]
        self.execute_query_with_params(sql_query, query_values)

    def get_count(self, table_name):
        sql_query = f"SELECT COUNT(id) FROM {table_name}"
        query = self.execute_query_with_params(sql_query)

        if query.next():
            return str(query.value(0))
        return '0'

    def get_all_ids(self, table_name):
        ids = []
        query = QtSql.QSqlQuery()
        query.exec_(f"SELECT id FROM {table_name}")
        while query.next():
            id_value = query.value(0)
            ids.append(id_value)
        return ids

    def get_all_info(self):
        info = []
        query = QtSql.QSqlQuery()
        query.exec_(f"SELECT * FROM free_cars")
        while query.next():
            row = []
            for i in range(query.record().count()):
                value = query.value(i)
                row.append(value)
            info.append(row)
        return info
