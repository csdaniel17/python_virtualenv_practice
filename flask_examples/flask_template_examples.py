from flask import Flask, render_template
import pg

db = pg.DB(dbname='restaurants2_db')

app = Flask('MyApp')

@app.route('/')
# def restaurants():
#     query = db.query('select * from restaurant')
#     return render_template(
#         'restaurant_list.html',
#         title='List of restaurants near ATV',
#         restaurants=query.namedresult())

def reviews():
    query = db.query('''
        select
            restaurant.name, review.stars
        from
            restaurant
        left outer join
            review on restaurant.id = review.restaurant_id
        ''')
    return render_template(
        'reviews.html',
        title='Restaurant reviews',
        reviews=query.namedresult())


if __name__ == '__main__':
    app.run(debug=True)
