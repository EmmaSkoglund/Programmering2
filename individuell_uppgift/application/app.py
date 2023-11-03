"""
• År
• Månad
• Dag
• prisklass (se API nedan)

• val max en dag frammåt, och som längs
2022-11-01 bakåt
• felmeddelande ska ges om icke angivet datum åvan
• en egen endpoint visa de aktuellq el priserna
med hjälp av pandas
• klockslag skall finnas med hh:mm
• om icke existerande endpoint anges ska 404 ges och
med hjälp av en kanpp kunna återvända tillbaka.

• test case för funktioner

länk : https://www.elprisetjustnu.se/elpris-api
"""

from flask import Flask, render_template, request
import ssl, json, urllib

app = Flask(__name__)


@app.route("/")
def index():

    month_mapping = {
    "01": "Januari",
    "02": "Februari",
    "03": "Mars",
    "04": "April",
    "05": "Maj",
    "06": "Juni",
    "07": "Juli",
    "08": "Augusti",
    "09": "September",
    "10": "Oktober",
    "11": "November",
    "12": "December" 
    }
    
    
    return render_template("index.html", month_mapping=month_mapping)



@app.route("/api", methods=["GET", "POST"])
def api_post():

    if request.method == "POST":
        try:
            year = request.form["year"]
            month = request.form["month"]
            day = request.form["day"]
            region = request.form["region"]
        except KeyError:
            return "Please fill out all required fields."  # Returnera ett felmeddelande till användaren om något saknas

        context = ssl._create_unverified_context()

        if year and month and day and region:
            data_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{region}.json"
            try:
                json_data = urllib.request.urlopen(data_url, context=context).read()
                data = json.loads(json_data)
                return render_template('index.html', data=data)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    return "Data not found. Please check your input."
                else:
                    return f"An error occurred: {str(e)}"
        else:
            return "Please select valid options."
    return render_template('index.html')  # Om det är en GET-förfrågan, rendera bara sidan utan att försöka hämta data


    
    