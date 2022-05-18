# Jade data pipeline installation Big data TMCS server part
  Jade's TMCS part is all about scheduling query data from
  
## 1. Preparation user in PostgreSQL DB
      create jade user with insert,update permission
## 2. Restore Source database  
      via pgadmin UI
## 3. Python 
      Assume that server already has python installed so... install only package via requirement.txt file
      pip install -r requirement.txt
## 4. 


# Jade data pipeline installation Big data server part
    
## Installation and running pipeline
### 1. Preparation user in PostgreSQL DB
      create jade user with insert,update permission
      ~~~~sql
      CREATE ROLE jade 
      LOGIN
      PASSWORD 'jade';
      
      GRANT SELECT,INSERT,UPDATE,DELETE 
      ON <table> 
      TO jade;
      ~~~~
### 2. Restore Source database  
      revia pgadmin
      
      
### 3. Python 
      Assume that server already has python installed so... install only package via requirement.txt file
      ```python
      pip install -r requirement.txt
      ```
### 4. Insert to Database
    ```python
    
    ```
