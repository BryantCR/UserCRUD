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

@app.route('/user/edit/<id>')
id2 = int(id)
def goAndEdit(id):
    return render_template("edit.html")

@app.route('/user/show/<id>')
id2 = int(id)
def showUserData(id):
    return render_template("show.html")
