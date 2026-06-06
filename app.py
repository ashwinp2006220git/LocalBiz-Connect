from flask import Flask, render_template, request, redirect, url_for

from db import (
    create_tables,
    insert_sample_data,
    get_all_enquiries,
    add_enquiry,
    delete_enquiry,
    get_dashboard_counts
)

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

create_tables()
insert_sample_data()


# Home
@app.route("/")
def home():
    return render_template("index.html")


# About
@app.route("/about")
def about():
    return render_template("aboutus.html")


# Services
@app.route("/services")
def services():
    return render_template("services.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    counts = get_dashboard_counts()
    enquiries = get_all_enquiries()

    return render_template(
        "dashboard.html",
        counts=counts,
        enquiries=enquiries
    )


# Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone") or "Not Provided"
        service = request.form.get("service")
        message = request.form.get("message")

        add_enquiry(name, email, phone, service, message)

        return redirect(url_for("thank_you"))

    return render_template("contactus.html")


# Thank You
@app.route("/thank-you")
def thank_you():
    return render_template("thankyou.html")


# Admin
@app.route("/admin")
def admin():
    enquiries = get_all_enquiries()
    return render_template("admin.html", enquiries=enquiries)


# Delete enquiry
@app.route("/delete/<int:enquiry_id>")
def delete(enquiry_id):
    delete_enquiry(enquiry_id)
    return redirect(url_for("admin"))


# Student Profile
@app.route("/student")
def student_profile():
    return render_template("studentprofile.html")


if __name__ == "__main__":
    app.run(debug=True)