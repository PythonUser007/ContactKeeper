from flask import Flask, render_template, request
import DatabaseHandler as DbH
import datetime as dt

phonebook_app = Flask(__name__)
db_instance = DbH.Db_Functions()

@phonebook_app.route("/")
def homepage():
    current_year = dt.datetime.now().year
    return render_template("index.html", Year=current_year)


@phonebook_app.route("/", methods=["POST"])
def gather_details():
    Title = request.form["radio"]
    Name = Title + " " + request.form["name"]
    Email = request.form["email"]
    Phone = request.form["phone"]
    data_touple = [(Name, Email, Phone)]
    db_instance.insert_record(data_touple)
    return render_template("index.html")


@phonebook_app.route("/Fetch")
def find_contact():
    current_year = dt.datetime.now().year
    return render_template("fetch.html", Year=current_year, State=1)


@phonebook_app.route("/Fetch", methods=["POST"])
def retrieve():
    current_year = dt.datetime.now().year
    search_string = request.form["name"]
    output = db_instance.fetch_record(search_string)
    print("The fetched details are : \n")
    print(output)
    return render_template("fetch.html", Year=current_year, final_data=output, State=2)


if __name__ == "__main__":
    phonebook_app.run(debug=True)
