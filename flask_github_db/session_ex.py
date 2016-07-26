from flask import Flask, session, request, render_template, redirect

import pg

db = pg.DB(dbname='github_db')

app = Flask('MyApp')

@app.route('/signin')
def signin():
    return render_template('get_name.html')

@app.route('/signin_submit', methods=['POST'])
def signin_submit():
    name = request.form['name']
    session['name'] = name
    return redirect('/signin')


app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'

if __name__ == '__main__':
    app.run(debug=True)
