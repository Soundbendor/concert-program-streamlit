# Database Connection Scripts

In this folder are all the files used to connect data saved in ../nyphilharmonic_data/{file_folder}/{file_name}

To use these scripts, you can alter the JSON file loads and function calls in database_connection.py.
For example use cases, see the bottom of database_conncetion.py.
Then to run the scripts use, first ensure the database server is running, and the correct login information is hardcoded at the top of database_conneciton.py including: db_server, db_name, db_username. Then on the command line run:  ```python database_connection.py <database password>```
