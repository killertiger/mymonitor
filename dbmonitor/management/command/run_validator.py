import MySQLdb

from django.core.management import BaseCommand

from dbmonitor.models import Query, ExecutionHistory


class Command(BaseCommand):
    def get_conector(self):
        db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB")
        db.cursor()
        return db

    def execute_query(self, query):
        db = self.getConector()
        db.execute(query)
        db.fetchall()

        row_count = db.rowcount

        db.close()

        return row_count

    def handle(self, *args, **options):
        queries = Query.objects.all()
        for query in queries:
            row_count = self.executeQuery(query.text)
            history = ExecutionHistory(query = query, total=row_count)
            history.save()
