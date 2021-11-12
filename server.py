# first server using flask
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        massage = data['massage']
        file = database.write(f'\n {email}, {subject}, {massage}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as databasecsv:
        email = data['email']
        subject = data['subject']
        massage = data['massage']
        csv_writer = csv.writer(
            databasecsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, massage])


@app.route('/summit_form', methods=['POST', 'GET'])
def summit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyounote.html')
        except:
            return 'did not saved to database'
    else:
        return 'some thing went wrong. Try again!'
