from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='restaurants2_db')

app = Flask('MyFormApp')

@app.route('/')
def form():
    return render_template(
    'form.html',
    title='Add a new restaurant')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    restaurant_name = request.form['restaurant_name']
    restaurant_address = request.form['restaurant_address']
    db.insert('restaurant', name=restaurant_name, address=restaurant_address)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
