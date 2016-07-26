from flask import Flask, session, request, render_template, redirect

import pg

db = pg.DB(dbname='github_db')

app = Flask('MyApp')


@app.route('/')
def home():
    if 'name' in session:
        return render_template('hello.html', name=session['name'])
    else:
        return render_template('get_name.html')

@app.route('/submit_name', methods=['POST'])
def submit_name():
    query = db.query("select coder.name from coder where name = $1", request.form['name'])
    dictionaried_result = query.dictresult()
    print dictionaried_result
    if len(dictionaried_result) > 0:
        session['name'] = request.form['name']
    return redirect('/')

@app.route('/clear_name')
def clear_name():
    del session['name']
    return redirect('/')

app.debug = True
app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'

if __name__ == '__main__':
    app.run(debug=True)
