from flask import Flask, render_template, request, redirect, url_for
from forms import QueryForm
import openai
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'spectakuralkeyfiles'
openai.api_key = os.getenv("OPENAI_API_KEY")

# results = []

@app.route('/', methods = ['GET','POST'])
@app.route('/home', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    form = QueryForm()
    # global results
    if form.is_submitted():
        query = request.form["query"]
        # response = "Hello this is a response"
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = query,
            max_tokens = 100,
            temperature = 0.6,
        )
        # results.append((query, response))        
        return redirect(url_for("index", response = response.choices[0].text, query = query))
        # return redirect(url_for("index",results = results))
    response = request.args.get("response")
    query = request.args.get("query")
    return render_template("index.html", form = form, response = response, query = query)
    # return render_template("index.html", form = form, result = results)


if __name__ == "__main__":
    app.run()