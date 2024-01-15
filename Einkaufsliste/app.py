from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
app = Flask (__name__)
bootstrap = Bootstrap(app)

@app.route("/lol")
def index():
    user="Leo"
    return render_template('liste.html', Einkaufsliste = Lebensmittel) 

Lebensmittel = [
    {'name': 'Gönergy', 'anzahl': '6'}, 

    {'name': 'Pulle Vitavate', 'anzahl': '1'}, 

    {'name': 'Loco Juice', 'anzahl': '4'} 

] 

if __name__ == '__main__':
    app.run(debug=True)