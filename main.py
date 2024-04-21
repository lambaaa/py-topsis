from flask import Flask, render_template, request
from waitress import serve
from topsis import Topsis
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/sonuc')
def get_hesap():
    city = request.args.get('city')
    ##ekrandan al verileri

    evaluation_matrix = np.array([
    [1,2,3,4],
    [4,3,2,1],
    [3,3,3,3],
    ])
    weights = [5, 5, 9, 0]
    criterias = np.array([True, True, True, True])
    t = Topsis(evaluation_matrix, weights, criterias)
    t.calc()
    
    return render_template(
        "sonuc.html",
        status = "best_distance\t"+str(t.best_distance),
        temp = "worst_distance\t"+str(t.worst_distance)
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
