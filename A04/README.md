# A04 – SQLite database from CSV files

- Each CSV file given on the command line becomes a table with the same name. Column names come from the first line of the file.
- If the table already exists, it is not created again.
- Then the script answers question 1:
  How many cities in the database are from Albania?


# How to run

```bash
git clone https://github.com/martin-sojciak/ci2.git
cd ci2/A04
python3 db.py city.csv country.csv countrylanguage.csv   
python3 db.py                                           
```

