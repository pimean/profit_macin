from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import schema, json

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


#Category Pages
@app.route('/finance-tools')
def financetools():
    return render_template('/categories/finance-tools.html', active_page='finance-tools')

@app.route('/business-tools')
def businesstools():
    return render_template('/categories/business-tools.html', active_page='business-tools')

@app.route('/tool-collections')
def toolcollections():
    return render_template('/categories/tool-collections.html', active_page='tool-collections')


#General Pages
@app.route('/about')
def about():
    return render_template('/pages/about.html', active_page='about')

@app.route('/contact')
def contact():
    return render_template('/pages/contact.html', active_page='contact')

@app.route('/privacy-policy')
def privacypolicy():
    return render_template('/pages/privacy-policy.html', active_page='privacy-policy')

@app.route('/terms')
def terms():
    return render_template('/pages/terms.html', active_page='terms')

@app.route('/disclaimer')
def disclaimer():
    return render_template('/pages/disclaimer.html', active_page='disclaimer')


#Business Tools Pages
@app.route('/breakeven-point-calculator')
def breakeven_point_calculator():
    return render_template('/business-tools/breakeven-point-calculator.html', active_page='business-tools')

@app.route('/currency-converter')
def currency_converter():
    return render_template('/business-tools/currency-converter.html', active_page='business-tools')

@app.route('/discount-calculator')
def discount_calculator():
    return render_template('/business-tools/discount-calculator.html', active_page='business-tools')

@app.route('/domain-name-availability-checker')
def domain_name_availability_checker():
    return render_template('/business-tools/domain-name-availability-checker.html', active_page='business-tools')

@app.route('/investment-return-calculator')
def investment_return_calculator():
    return render_template('/business-tools/investment-return-calculator.html', active_page='business-tools')

@app.route('/profit-margin-calculator', methods=['GET', 'POST'])
def profit_margin_calculator():
    # Define schema object
    schema_markup = schema.schema_markup_business_tools_profit_margin_calculator
    # Convert the schema object to a JSON-LD string
    json_ld = json.dumps(schema_markup, indent=4)
    if request.method == 'POST':
        cost = float(request.form['cost'])
        revenue = float(request.form['revenue'])
        gross_margin = round((revenue - cost) / revenue * 100, 2)
        profit = round(revenue - cost, 2)
        return render_template('/business-tools/profit-margin-calculator.html', active_page='business-tools', gross_margin=gross_margin, profit=profit, cost=cost, revenue=revenue, json_ld = json_ld)

    else:
        return render_template('/business-tools/profit-margin-calculator.html', active_page='business-tools', json_ld = json_ld)
    
@app.route('/roi-calculator')
def roi_calculator():
    return render_template('/business-tools/roi-calculator.html', active_page='business-tools')

@app.route('/sales-tax-calculator')
def sales_tax_calculator():
    return render_template('/business-tools/sales-tax-calculator.html', active_page='business-tools')

@app.route('/tip-calculator')
def tip_calculator():
    return render_template('/business-tools/tip-calculator.html', active_page='business-tools')


#Finance Tools Pages
@app.route('/auto-insurance-calculator')
def auto_insurance_calculator():
    return render_template('/finance-tools/auto-insurance-calculator.html', active_page='finance-tools')

@app.route('/net-worth-calculator')
def net_worth_calculator():
    return render_template('/finance-tools/net-worth-calculator.html', active_page='finance-tools')

@app.route('/car-loan-calculator')
def car_loan_calculator():
    return render_template('/finance-tools/car-loan-calculator.html', active_page='finance-tools')

@app.route('/compound-interest-calculator')
def compound_interest_calculator():
    return render_template('/finance-tools/compound-interest-calculator.html', active_page='finance-tools')

@app.route('/cost-of-living-calculator')
def cost_of_living_calculator():
    return render_template('/finance-tools/cost-of-living-calculator.html', active_page='finance-tools')

@app.route('/credit-card-interest-calculator')
def credit_card_interest_calculator():
    return render_template('/finance-tools/credit-card-interest-calculator.html', active_page='finance-tools')

@app.route('/debt-payoff-calculator')
def debt_payoff_calculator():
    return render_template('/finance-tools/debt-payoff-calculator.html', active_page='finance-tools')

@app.route('/home-equity-loan-calculator')
def home_equity_loan_calculator():
    return render_template('/finance-tools/home-equity-loan-calculator.html', active_page='finance-tools')

@app.route('/homeowners-insurance-calculator')
def homeowners_insurance_calculator():
    return render_template('/finance-tools/homeowners-insurance-calculator.html', active_page='finance-tools')

@app.route('/hourly-wage-calculator')
def hourly_wage_calculator():
    return render_template('/finance-tools/hourly-wage-calculator.html', active_page='finance-tools')

@app.route('/investment-calculator')
def investment_calculator():
    return render_template('/finance-tools/investment-calculator.html', active_page='finance-tools')

@app.route('/loan-calculator')
def loan_calculator():
    return render_template('/finance-tools/loan-calculator.html', active_page='finance-tools')

@app.route('/mortgage-calculator')
def mortgage_calculator():
    return render_template('/finance-tools/mortgage-calculator.html', active_page='finance-tools')

@app.route('/payroll-calculator')
def payroll_calculator():
    return render_template('/finance-tools/payroll-calculator.html', active_page='finance-tools')

@app.route('/retirement-savings-calculator')
def retirement_savings_calculator():
    return render_template('/finance-tools/retirement-savings-calculator.html', active_page='finance-tools')

@app.route('/salary-calculator')
def salary_calculator():
    return render_template('/finance-tools/salary-calculator.html', active_page='finance-tools')

@app.route('/stock-profit-calculator')
def stock_profit_calculator():
    return render_template('/finance-tools/stock-profit-calculator.html', active_page='finance-tools')


#Other Tools Pages
@app.route('/qr-code-generator')
def qr_code_generator():
    return render_template('/other-tools/qr-code-generator.html', active_page='tool-collections')


if __name__ == '__main__':
    app.run(debug=True)
