from flask import Flask,render_template,request,redirect
from db import init_db,add_expense,get_expenses

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    data = get_expenses()
    total = sum([d[2] for d in data])
    return render_template('index.html',data=data,total=total)

@app.route('/add',methods=['POST'])
def add():
    item = request.form['item']
    amount = float(request.form['amount'])
    date = request.form['date']
    add_expense(item,amount,date)
    return redirect('/')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
