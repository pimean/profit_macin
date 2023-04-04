from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from time import wait

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


#Finance Tools Route and Children
@app.route('/finance-tools')
def finacetools():
    return render_template('finance-tools.html', active_page='finance-tools')

@app.route('/profit-margin-calculator', methods=['GET', 'POST'])
def profitmargincalculator():
    if request.method == 'POST':
        cost = float(request.form['cost'])
        revenue = float(request.form['revenue'])
        gross_margin = round((revenue - cost) / revenue * 100, 2)
        profit = round(revenue - cost, 2)
        return render_template('profit-margin-calculator.html', active_page='business-tools', gross_margin=gross_margin, profit=profit, cost=cost, revenue=revenue)

    else:
        return render_template('profit-margin-calculator.html', active_page='business-tools')


#Finance Tools Route and Children
@app.route('/business-tools')
def businesstools():
    return render_template('business-tools.html', active_page='business-tools')

@app.route('/tool-collections')
def toolcollections():
    return render_template('tool-collections.html', active_page='tool-collections')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/privacy-policy')
def privacypolicy():
    return render_template('privacy-policy.html', active_page='privacy-policy')

@app.route('/terms')
def terms():
    return render_template('terms.html', active_page='terms')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html', active_page='disclaimer')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
