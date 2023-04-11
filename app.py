from flask import Flask, request, render_template, send_from_directory, redirect
from flask_bootstrap import Bootstrap
from schema import *

app = Flask(__name__)
Bootstrap(app)

@app.before_request
def redirect_nonwww():
    """Redirect non-www requests to www."""
    if request.url.startswith('https://profitmacin.com'):
        url = request.url.replace('https://profitmacin.com', 'https://www.profitmacin.com', 1)
        return redirect(url, code=301)


@app.route('/')
def index():
    return render_template('index.html')


#Category Pages
@app.route('/finance-tools')
def financetools():
    return render_template('/categories/finance-tools.html', active_page='finance-tools', schema_markup = schema_markup_finance_tools_page, breadcrumb = get_breadcrumb(schema_markup_finance_tools_page))

@app.route('/business-tools')
def businesstools():
    return render_template('/categories/business-tools.html', active_page='business-tools', schema_markup = schema_markup_business_tools_page, breadcrumb = get_breadcrumb(schema_markup_business_tools_page) )

@app.route('/tool-collections')
def toolcollections():
    return render_template('/categories/tool-collections.html', active_page='tool-collections', schema_markup = schema_markup_tool_collections_page, breadcrumb = get_breadcrumb(schema_markup_tool_collections_page) )


#General Pages
@app.route('/about')
def about():
    return render_template('/pages/about.html', active_page='about', schema_markup = schema_markup_about_page, breadcrumb = get_breadcrumb(schema_markup_about_page) )

@app.route('/contact')
def contact():
    return render_template('/pages/contact.html', active_page='contact', schema_markup = schema_markup_contact_page, breadcrumb = get_breadcrumb(schema_markup_contact_page))

@app.route('/disclaimer')
def disclaimer():
    return render_template('/pages/disclaimer.html', active_page='disclaimer', schema_markup = schema_markup_disclaimer_page, breadcrumb = get_breadcrumb(schema_markup_disclaimer_page) )

@app.route('/privacy-policy')
def privacypolicy():
    return render_template('/pages/privacy-policy.html', active_page='privacy-policy', schema_markup = schema_markup_privacy_policy_page, breadcrumb = get_breadcrumb(schema_markup_privacy_policy_page) )

@app.route('/terms')
def terms():
    return render_template('/pages/terms.html', active_page='terms', schema_markup = schema_markup_terms_of_use_page, breadcrumb = get_breadcrumb(schema_markup_terms_of_use_page) )


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

    if request.method == 'POST':
        cost = float(request.form['cost'])
        revenue = float(request.form['revenue'])
        gross_margin = round((revenue - cost) / revenue * 100, 2)
        profit = round(revenue - cost, 2)
        return render_template('/business-tools/profit-margin-calculator.html', active_page='business-tools', gross_margin=gross_margin, profit=profit, cost=cost, revenue=revenue, schema_markup = schema_markup_business_tools_profit_margin_calculator, breadcrumb = get_breadcrumb(schema_markup_business_tools_profit_margin_calculator) )

    else:
        return render_template('/business-tools/profit-margin-calculator.html', active_page='business-tools', schema_markup = schema_markup_business_tools_profit_margin_calculator, breadcrumb = get_breadcrumb(schema_markup_business_tools_profit_margin_calculator) )
    
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


def get_breadcrumb(schema):
    """Extracts breadcrumb values and URLs from a schema markup"""
    
    # Get the breadcrumb list from the schema markup
    breadcrumb_list = schema.get('breadcrumb', {}).get('itemListElement', [])
    
    # Extract the name and URL for each breadcrumb item
    breadcrumbs = []
    for item in breadcrumb_list:
        name = item.get('name', '')
        url = item.get('item', '')
        breadcrumbs.append((name, url))
    
    # Combine the name and URL for each breadcrumb item into a string
    breadcrumb_string = '<ol class="breadcrumb">'
    for i, (name, url) in enumerate(breadcrumbs):
        if i == len(breadcrumbs) - 1:
            breadcrumb_string += f'<li class="breadcrumb-item active" aria-current="page">{name}</li>'
        else:
            breadcrumb_string += f'<li class="breadcrumb-item"><a href="{url}" class="text-secondary">{name}</a></li>'
    breadcrumb_string += '</ol>'
    
    return breadcrumb_string

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')


if __name__ == '__main__':
    app.run(debug=True)
