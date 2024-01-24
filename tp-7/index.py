#!/usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)

# File path to store username and password
data_file_path = "user_data.txt"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # Verify user credentials
        if verify_credentials(username, password):
            return f"<h1>Welcome, {username}!</h1>"
        else:
            return "<h1>Invalid credentials. Please try again.</h1>"

    return render_template('index.html')

def verify_credentials(username, password):
    with open(data_file_path, 'r') as data_file:
        for line in data_file:
            stored_username, stored_password = parse_credentials(line)
            if username == stored_username and password == stored_password:
                return True
    return False

def parse_credentials(line):
    # Extract username and password from the line in the data file
    # This is a simple parsing, and in a real-world scenario, you'd need a more robust approach
    parts = line.strip().split(', ')
    stored_username = parts[0].split(': ')[1]
    stored_password = parts[1].split(': ')[1]
    return stored_username, stored_password

if __name__ == '__main__':
    app.run(debug=True)
