from flask import Flask, render_template, redirect, url_for, session, request
import json

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'  # Clé secrète pour les sessions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcul', methods=['GET', 'POST'])
def calcul():
    if request.method == 'POST':
        # Récupérer les données du graphe depuis le formulaire
        points = request.form.get('points')
        lines = request.form.get('lines')

        # Stocker les données dans la session
        session['points'] = points
        session['lines'] = lines

        # Rediriger vers la page de calcul
        return redirect(url_for('calcul'))

    # Récupérer les données du graphe depuis la session
    points = session.get('points', '[]')
    lines = session.get('lines', '[]')

    # Convertir les données JSON en objets Python
    points = json.loads(points)
    lines = json.loads(lines)

    # Passer les données au template
    return render_template('calcul.html', points=points, lines=lines)

if __name__ == '__main__':
    app.run(debug=True)