import mysql.connector

from dbmonitor.models import ExecutionHistory, Query, ExecutionHistoryDetail


class ValidatorBusiness:
    def get_conector(self, connection, database='mysql'):
        db = mysql.connector.connect(host=connection.host, user=connection.username, password=connection.password,
                                     database=database)
        return db

    def execute_query(self, database, query):
        db = self.get_conector(query.connection, database)
        cursor = db.cursor()
        try:
            cursor.execute(query.text)
            cursor.fetchall()

            row_count = cursor.rowcount
        finally:
            cursor.close()
            db.close()

        return row_count

    def get_databases(self, connection, rule):
        db = self.get_conector(connection)
        cursor = db.cursor()

        try:
            sql = "SELECT DISTINCT SCHEMA_NAME AS `database` " \
                  " FROM information_schema.SCHEMATA " \
                  " WHERE {} " \
                  " ORDER BY SCHEMA_NAME".format(rule.rule_text)
            cursor.execute(sql)
            query_result = cursor.fetchall()

            return query_result
        finally:
            cursor.close()
            db.close()

    def register_history(self, query, found_list):
        history = ExecutionHistory(query=query, total=len(found_list))
        history.save()

        for found in found_list:
            detail = ExecutionHistoryDetail(execution_history=history, database_name=found["database"],
                                            total=found["count"])
            detail.save()

    def validate_all_monitors(self):
        queries = Query.objects.filter(is_active=True)
        for query in queries:
            found_list = []
            dblist = self.get_databases(query.connection, query.rule)
            for db in dblist:
                row_count = self.execute_query(db[0], query)
                found_list.append({'database': db[0], 'count': row_count})
            self.register_history(query, found_list)

