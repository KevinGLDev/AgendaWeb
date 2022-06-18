from flasksite import create_app


app=create_app()

#run from terminal and set EMAIL_USER and EMAIL_PASS in the terminal using nano .bash_profile for mac
if __name__ == '__main__':
    app.run(debug=True)