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
restore backup database via pgadmin
      
### 3. Python package install
```python
# install psycopg2
pip install -r requirement.txt
```
### 4. Insert to Database
```python
Usage : python insert.py <file directory>
```
