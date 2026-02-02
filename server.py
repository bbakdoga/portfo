from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    return 'something went wrong. Try again'


def write_tofile(data):
    with open('database.txt', mode="a") as fp:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = fp.write(f'\n{name}, {email}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode="a") as fp:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(fp, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])
