import pg

# connect to the PostrgreSQL database
db = pg.DB(dbname='github_db')

# make a query
query = db.query('select * from coder')
# show data
print query


# multi line query
query1 = db.query('''
    select
        *
    from
        project
    where
        stars is not NULL
    order by
        stars desc
    limit
        10
''')
# show data
print query1


## 3 ways to get result of query

# 1. get a list of tuples
tupled_result = query.getresult()
print tupled_result

# shown as:
# [(1, 'Sandhya', 'sandhya@me.com'), (2, 'Carolyn', 'carolyn@me.com'), (3, 'Kyle', 'kyle@me.com'), (4, 'Allen', 'allen@me.com'), (5, 'Shanda', 'shanda@me.com'), (6, 'Cody', 'cody@me.com')]


# 2. git a list of dictionaries
dictionaried_result = query.dictresult()
print dictionaried_result

# shown as:
# [{'email_address': 'sandhya@me.com', 'id': 1, 'name': 'Sandhya'}, {'email_address': 'carolyn@me.com', 'id': 2, 'name': 'Carolyn'}, {'email_address': 'kyle@me.com', 'id': 3, 'name': 'Kyle'}, {'email_address': 'allen@me.com', 'id': 4, 'name': 'Allen'}, {'email_address': 'shanda@me.com', 'id': 5, 'name': 'Shanda'}, {'email_address': 'cody@me.com', 'id': 6, 'name': 'Cody'}]


# **3. get a list of named tuples, which are basically objects with attributes
named_result_ex = query.namedresult()
print named_result_ex

# shown as:
# [Row(id=1, name='Sandhya', email_address='sandhya@me.com'), Row(id=2, name='Carolyn', email_address='carolyn@me.com'), Row(id=3, name='Kyle', email_address='kyle@me.com'), Row(id=4, name='Allen', email_address='allen@me.com'), Row(id=5, name='Shanda', email_address='shanda@me.com'), Row(id=6, name='Cody', email_address='cody@me.com')]


# **recommended - named result because it is most convenient
named_result = query.namedresult()
for coder in named_result:
    print "Coder: %s, Email: %s" % (coder.name, coder.email_address)
