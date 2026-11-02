#!/usr/bin/env python3
"""
A04 - Creates the SQLite database "db.sqlite" from CSV files
and answers the question: How many cities in the database are from Albania?
"""
import csv
import os
import sqlite3
import sys


class Database:

    def __init__(self, args):
        """
        Saves the CSV file names and opens the connection to the database.
        """
        self.csv_files = args[1:]
        self.connection = sqlite3.connect("db.sqlite")
        self.cursor = self.connection.cursor()

    def table_exists(self, table_name):
        """
        Checks if table exists.
        """
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?",
            (table_name,),
        )
        return self.cursor.fetchone() is not None

    def import_csv(self, file_name):
        """
        Creates a table from one CSV file and fills it.
        """
        table_name = os.path.splitext(os.path.basename(file_name))[0]

        if self.table_exists(table_name):
            return

        with open(file_name, encoding="utf-8", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            columns = next(reader)  
            rows = list(reader)    

        self.cursor.execute(f"CREATE TABLE {table_name} ({', '.join(columns)})")

        placeholders = ", ".join(["?"] * len(columns)) 
        for row in rows:
            self.cursor.execute(
                f"INSERT INTO {table_name} VALUES ({placeholders})", row
            )
        self.connection.commit()
        print(f"Table {table_name} created with {len(rows)} rows.")

    def answer_question(self):
        """
        Counts the cities from Albania with an SQL query and prints
        the answer.
        """
        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM city
            JOIN country ON city.CountryCode = country.Code
            WHERE country.Name = 'Albania'
            """
        )
        count = self.cursor.fetchone()[0]
        print("How many cities in the database are from Albania?")
        print(count)

    def run(self):
        """
        Imports all CSV files from the command line,
        answers the question and closes the database connection.
        """
        for file_name in self.csv_files:
            self.import_csv(file_name)
        self.answer_question()
        self.connection.close()


if __name__ == "__main__":
    database = Database(sys.argv)
    database.run()
