from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'
