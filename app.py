from flask import Flask, render_template,request
import sentiment_mod as s
import nltk
nltk.download('punkt')


app = Flask(__name__)

@app.route('/')
def default():
    return render_template('home.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/insight.html')
def insight():
    return render_template('insight.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/test.html',methods=['POST'])
def predict():


    if request.method == 'POST':
        data = request.form['review']

      
    
        dtlc = data.lower()
        rev , conf =(s.sentiment(dtlc))
        p_conf = conf * 100
               
        
    return render_template('test.html', prediction_text = "the review :: " + data + " :: is a " + rev + " review!, with " + str(p_conf) + " percent confidence")


 

if __name__ == '__main__':
    app.run(debug=True)


    
