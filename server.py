from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')


# @app.route('/')
# def index():
#     friends = mysql.query_db("SELECT * FROM friends")
#     print friends
#     return render_template('index.html')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template


# @app.route('/friends', methods=['POST'])
# def create():
#     # add a friend to the database!
#     return redirect('/')

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'age': request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')





app.run(debug=True)
