from flask import render_template, request, redirect
from users_app import app
from users_app.models.User import User

@app.route( "/" )
def displayLogin():
    return redirect ('/users')

@app.route( "/users" )
def displayAllUsers():
    currentUsersInTable = User.get_all_users()
    print(currentUsersInTable)
    return render_template( "read.html", users1 = currentUsersInTable)

@app.route('/users/new')
def new():
    return render_template( "create.html")

@app.route('/users/new', methods=['POST'])
def create():
    print(request.form)
    User.addDataForm(request.form)
    return redirect('/users')
