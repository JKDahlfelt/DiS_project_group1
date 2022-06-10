# DiS_project_group1
DiS assignment project
### How to run:
1) Extract zip-fil "CBS" at a location of your own discretion.

2) run >$ pip install -r requirements.txt

3)  Database initialization
1. set the database name  and password to your own database password (the same as eg. in pgadmin) in the __init__.py file.
2. run schema_drop.sql, schema.sql, schema_ins.sql and schema_importCSV.sql in your database.
    2.1. Remember to change path in the schema_importCSV.sql for csv files.
3. Run Web-App; >$ python run.py
