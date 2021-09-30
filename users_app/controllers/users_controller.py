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
def goToCreate():
    return render_template( "create.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.addDataForm(request.form)
    return redirect('/users')

#//////////////////////////////////////// EDIT PART ///////////////////////////////////////////
#We're trying to get into a new page called edit
@app.route('/users/edit/<id>')
def goAndEdit(id):
    updatedUsersInTable = User.get_one(id)
    print(updatedUsersInTable)
    return render_template("edit.html", users1 = updatedUsersInTable, id = id)

#Here we're trying to redirect to the next page
@app.route('/users/show/<id>')
def showUsersData(id):
    updatedUsersInTable = User.get_one(id)
    print("EditUserData: ", updatedUsersInTable)
    return render_template("show.html", users1 = updatedUsersInTable, id = id)

#We're trying to got a form here
@app.route('/users/edit2', methods=['POST'])
def gotAndEditForm():
    User.editUserData(request.form)
    print("EditUserData: ", request.form)
    return render_template("show.html")

#Here we create the form for update the data from an user
@app.route('/users/edit/<id>')
def editUserData(id):
    currentUsersInTable = User.get_all_users()
    print("EditUserData: ", currentUsersInTable)
    return render_template("edit.html", users1 = currentUsersInTable, id = id)
