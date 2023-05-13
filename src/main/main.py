from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # Get the news articles from the API.
    articles = client.get_articles()

    # Render the template with the news articles.
    return render_template("index.html", articles=articles)

@app.route("/article/<id>")
def article(id):
    # Get the article from the API.
    article = client.get_article(id)

    # Render the template with the article.
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(debug=True)
