import sys
import pyodbc
import json
import image_data
import meta_data

# define file to be input to database
file_folder = "nyphilharmonic_metadata"
file_name = "output.json"

# define database login information
db_server = 'tcp:localhost,1433'
db_name = 'master'
db_username = 'sa'
db_password = sys.argv[1]

### open file with JSON data, return data object
def load_concerts_json():
    file = open(f'../nyphilharmonic_data/{file_folder}/{file_name}')
    concerts = json.load(file)
    return concerts 

### create connection with database using pyODBC, return connection and cursor
def connect_to_database():
    server = db_server
    name = db_name 
    username = db_username
    password = db_password

    connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+name+';ENCRYPT=no;UID='+username+';PWD='+ password)
    cursor = connection.cursor()
    return connection, cursor

### query parameter creation
def set_bin_params_from_json():
    binparams = (1, pyodbc.Binary(binary_data))
    return binparams

### execute functions to insert data
def insert_concert_images(concert_data, cursor):
    insert_query = get_insert_image_query()
    binparams = get_binparams_concert_images(concert_data)
    execute_insert_query(insert_query, binparams, cursor)

def insert_concert_metadata(concert_data, cursor):
    insert_query = get_insert_metadata_query()
    binparams = get_binparams_concert_metadata(concert_data)
    execute_insert_query(insert_query, binparams, cursor)

### query execution
def execute_insert_query(insert_query, binparams, cursor):
    cursor.execute(insert_query, binparams)

def execute_select_query(select_query, cursor):
    cursor.execute(select_query)

def save_selection_to_cursor(cursor):
    selection = []
    for i in cursor:
        selection += i
    return selection

### execute functions for SELECT queries
def select_concerts(cursor):
    select_query = meta_data.get_select_metadata_query()
    execute_select_query(select_query, cursor)
    selection = save_selection_to_cursor(cursor)
    print(selection)

def select_concert(id, cursor):
    select_metadata_query = meta_data.get_select_metadata_query(id)
    execute_select_query(select_metadata_query, cursor)
    metadata_selection = save_selection_to_cursor(cursor)

    select_image_query = image_data.get_select_images_query(id)
    execute_select_query(select_image_query, cursor)
    image_selection = save_selection_to_cursor(cursor)
    return metadata_selection, image_selection

def pretty_print_select(id, cursor):
    print("\n== For concert id: ", id)
    metadata, image = select_concert(id, cursor)
    print("Metadata: ", metadata)
    print("Image: ", image)



### examples of usage

connection, cursor = connect_to_database()
concerts = load_concerts_json()

## to load metadata into db 
# connection, cursor = connect_to_database()
# concerts = load_concerts_json()
# get_binparams_concert_metadata(concerts)
# insert_concerts(concerts, cursor)
# connection.commit()

## to print metadata from db
# select_concert('14687', cursor)
# pretty_print_select(14687, cursor)

