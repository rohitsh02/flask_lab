"""
## Jinja2 template engine
    - Here you are actually integrating HTML with some data source so that you will be able to get
    this value from there itself. 

    {% ... %}: Used for control flow statements like loops (for, while), conditions (if, elif, else), and other template logic.
    {{ ... }}: Used for rendering expressions and printing output dynamically within HTML templates.
    {# ... #}: Used for adding comments within templates, which are ignored during rendering.

    In essence, {% ... %} is for logic, {{ ... }} is for output, and {# ... #} is for comments in Jinja2 templates.

Use Cases of Jinja2:
Web Development: Jinja2 is extensively used in web development frameworks like Flask and Django for generating dynamic HTML content,
rendering templates, and building user interfaces.

Email Templates: Jinja2 can be used to generate dynamic email templates, allowing developers to personalize email
content based on user data or application events.

Reports and Documents: Jinja2 can generate dynamic reports and documents in various formats (e.g., HTML, PDF, CSV) by
populating templates with data fetched from databases or APIs.

Configuration Files: Jinja2 can be utilized to generate configuration files dynamically, enabling parameterization and
customization based on deployment environments or user preferences.
"""

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"
    exp = {'score': score, "result":res}
    return render_template('result.html', result=exp)

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
