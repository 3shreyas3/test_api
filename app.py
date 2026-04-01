from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('album.html')


@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/comments')
def comments():
    return render_template('comments.html')
if __name__ == '__main__':
    app.run(debug=True)
