from flask import Flask, render_template, request, redirect, session
from users_app import app
from users_app.controllers import users_controller

if __name__ == "__main__":
    app.run( debug = True )
