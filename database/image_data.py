from urllib.request import urlopen
from PIL import Image

### image <-> file <-> binary manipulations
def get_binary_data_from_image_file(image_file):
    with open(image_file, 'rb') as file:
        binary_data = file.read()
    return binary_data

def download_image_file_from_image_url(image_url):
	image = Image.open(urlopen(image_url))
	image.save('current_download.jpg')

def convert_image_url_to_binary(image_url):
    download_image_file_from_image_url(image_url)
    binary_data = get_binary_data_from_image_file('./current_download.jpg')
    return binary_data

def get_image_from_binary(binary_data):
    with open("./output.jpg" ,"wb") as fs2:
        fs2.write(binary_data)
        write_image_from_binary(binary_data)
    return

### data formatting
def get_binparams_concert_images(concert_data):
    concert_id = concert_data['metadata']['id']
    image_urls = concert_data['images']
    image_binary_data = convert_image_url_to_binary(image_urls['1'])
    binparams = (image_urls['1'], image_binary_data, concert_id)
    return binparams

### image querys
def get_insert_image_query():
    insert_query = 'INSERT INTO [master].[dbo].[program_images] (url, image, concert_id) VALUES (?,?,?)'
    return insert_query

def get_select_images_query(id):
    select_query = 'SELECT * FROM [master].[dbo].[program_images] WHERE concert_id={}'.format(id)
    print(select_query)
    return select_query

