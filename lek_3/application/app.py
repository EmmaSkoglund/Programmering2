from flask import Flask, render_template, request, make_response

app = Flask(__name__)

country = [
    "Sverige",
    "Norge",
    "Danmark",
    "Frankrike",
    "England",
    "Tyskland",
    "Italien",
    "Grekland"
]


@app.route("/")
def start_sida():
    selected_country = request.cookies.get("selected_country")

    if selected_country in country:
        country.remove(selected_country)
        country.insert(0, selected_country)

    return render_template('index.html', countries=country, selected_country=selected_country)


@app.route("/se", methods=['POST'])
def sverige():
    selected_country = request.form.get("country")

    responsed = make_response(render_template("inde"))
    if selected_country == "Sverige":
        return render_template("layout.html", selected_country=selected_country)
    else:
        return render_template("index.html")

