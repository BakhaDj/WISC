from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = "vjbdkjvbdfkjbvd"


@app.route('/', methods=['POST', 'GET'])
def main_view():
    if request.method == 'GET':
        return render_template('site.html')
    
    if request.method == 'POST':
        print(request.form)
        name = request.form ['IMYA']
        if 'will_come' in request.form.keys():
            will_come = 'Придёт'
        else: 
            will_come = 'Не придёт' 
        with sqlite3.connect('dbs') as connection:
            cursor = connection.cursor()
            stmt = f'''INSERT INTO users (username, will_come) VALUES ("{name}", "{will_come}") '''
            print(stmt)
            cursor.execute(stmt)
            connection.commit()
        return redirect('/success')

@app.route('/success')
def success_view():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.7', port=80)