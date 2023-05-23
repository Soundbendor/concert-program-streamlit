def get_binparams_concert_metadata(concert_data):
    metadata = concert_data['metadata']
    binparams = (
        metadata['season'][:4], 
        metadata['first_conductor'], 
        metadata['orch'], 
        metadata['first_location'], 
        metadata['first_venue'], 
        metadata['event_name'], 
        metadata['first_date'], 
        metadata['num_perfs'], 
        metadata['first_soloist'], 
        metadata['id']
    )
    return binparams

### query creation
def get_insert_metadata_query():
    insert_metadata_query = 'INSERT INTO [master].[dbo].[concert_metadata] (season, first_conductor, orch, first_location, first_venue, event_name, first_date, num_perfs, first_soloist, id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    return insert_metadata_query

def get_select_metadata_query(id):
    select_query = 'SELECT * FROM [master].[dbo].[concert_metadata] WHERE id={}'.format(id)
    return select_query
