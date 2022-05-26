# Jade data pipeline installation TMCS server 
Schedule batch query from DTG server to Jade server and moving the data directory into transfering area.
## Prerequisite
 * Python 3+
 * psycopg2

## Installation and running pipeline
### 1. Installation 
copy query.py and script to jade server

copy table_column.json to working directory

copy jade_pipeline.py script to DTG server 

### 2. running pipeline script
execution schedule jade pipeline script at DTG server 
```python
baccdtg01li$ python jade_pipeline.py
```

# Jade data pipeline installation Big data server 
insert directory of batch query from jade to PostgreSQL 
## Prerequisite
  * Python 3+
  * psycopg2
    
## Installation and running pipeline
### 1. Preparation user in PostgreSQL DB

```sql
CREATE ROLE jade 
LOGIN
PASSWORD 'jade';

GRANT SELECT,INSERT,UPDATE,DELETE 
ON <table> 
TO jade;
```
### 2. Restore Source database  
https://drive.google.com/file/d/1Dt7VB4ASGmR1D6wYQ12VBUb6zGcSWy4j/view?usp=sharing

create Jade database and restore backup database via pgadmin
      
### 3. Python package install
install package via requirement.txt file
```python
# install psycopg2
pip install -r requirement.txt
```
copy all_coln_dtype.json to working directory
### 4. Insert to Database
```python
Usage : python insert.py <file directory>
```
schedule insert.py for batch insertion

edit user,password,database in insert.py file as it should be.
