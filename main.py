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
    ##weights = np.array(request.array.get('wg'))
    ##choices = request.args.get('choices')
    choices = np.array([
        'Hammadde A :',
        'Hammadde B :',
        'Hammadde C :',
        'Hammadde D :',
        'Hammadde E :',
        'Hammadde F :',
        ])
    evaluation_matrix = np.array([
    [49,8,5,9],
    [45,7,7,8],
    [55,9,5,7],
    [48,6,6,8],
    [52,8,5,6],
    [51,8,7,7],
    ])
    weights = np.array([0.2, 0.3, 0.2, 0.1])
    ##weights = [5, 5, 9, 0]
    ##weights = [123.12, 18.92, 14.14, 18.52]
    criterias = np.array([False, True, False, True])
    t = Topsis(evaluation_matrix, weights, criterias)
    t.calc()
    
    return render_template(
        "sonuc.html",
        ##status = "best_distance\t"+str(t.best_distance),
        ##temp = "worst_distance\t"+str(t.worst_distance),
        step1 = 
            str(choices[0])+str(np.round(t.evaluation_matrix[0],3))+"\n"+
            str(choices[1])+str(np.round(t.evaluation_matrix[1],3))+"\n"+
            str(choices[2])+str(np.round(t.evaluation_matrix[2],3))+"\n"+
            str(choices[3])+str(np.round(t.evaluation_matrix[3],3))+"\n"+
            str(choices[4])+str(np.round(t.evaluation_matrix[4],3))+"\n"+
            str(choices[5])+str(np.round(t.evaluation_matrix[5],3))+"\n",

        step2 = 
            str(choices[0])+str(np.round(t.normalized_decision[0],3))+"\n"+
            str(choices[1])+str(np.round(t.normalized_decision[1],3))+"\n"+
            str(choices[2])+str(np.round(t.normalized_decision[2],3))+"\n"+
            str(choices[3])+str(np.round(t.normalized_decision[3],3))+"\n"+
            str(choices[4])+str(np.round(t.normalized_decision[4],3))+"\n"+
            str(choices[5])+str(np.round(t.normalized_decision[5],3))+"\n",

        step3 = 
            str(choices[0])+str(np.round(t.weighted_normalized[0],3))+"\n"+
            str(choices[1])+str(np.round(t.weighted_normalized[1],3))+"\n"+
            str(choices[2])+str(np.round(t.weighted_normalized[2],3))+"\n"+
            str(choices[3])+str(np.round(t.weighted_normalized[3],3))+"\n"+
            str(choices[4])+str(np.round(t.weighted_normalized[4],3))+"\n"+
            str(choices[5])+str(np.round(t.weighted_normalized[5],3))+"\n",

        step4worst = "\t"+str(t.worst_alternatives),
        step4best = "\t"+str(t.best_alternatives),

        step5worstdist = "\t"+str(t.worst_distance),
        step5bestdist = "\t"+str(t.best_distance),

        step6worstsim = "\t"+str(t.worst_similarity),
        step6bestsim = "\t"+str(t.best_similarity)
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
