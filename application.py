from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/application-form")
def show_application():
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def show_response():
	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	job = request.form.get("role")
	return render_template("response-page.html", fname=first_name , lname=last_name , jobtitle=job)

if __name__ == "__main__":
    app.run(debug=True)