import pg

db = pg.DB(dbname='restaurants2_db')

query = db.query('select * from restaurant')
print query


# insert into db
rest_name = raw_input("Enter a restaurant name: ")
rest_address = raw_input("What is the address? ")
rest_category = raw_input("What is the category of food? ")

db.insert('restaurant', name= rest_name, address= rest_address, category= rest_category)


# update db
rest_id = raw_input("What is the id of the restaurant you would like to update? ")
rest_updated_address = raw_input("What is the new address? ")

db.update('restaurant', {'id': rest_id, 'address': rest_updated_address})


# delete some data
rest_to_delete = raw_input("What is the id of the restaurant would you like to delete? ")

db.delete('restaurant', {'id': rest_to_delete})
