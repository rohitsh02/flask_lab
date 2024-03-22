from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    message = ""
    if score >= 50:
        result = "Pass"
        message = "Congratulations! You have passed. Keep up the good work and strive for excellence in the future!"
    else:
        result = "Fail"
        message = "You have done well, but it seems you fell short this time. Don't lose heart! Keep working hard and you'll surely succeed."

    return render_template('result.html', result={'score': score, "result":result, 'message': message})

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

### Result checker submit HTML page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    res = ""
    return redirect(url_for('success', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
