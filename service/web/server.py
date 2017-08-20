from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == 'wario.txt':
            file.save(file.filename)
            return redirect(request.url)
        else:
            flash('Not wario.txt')
            return redirect(request.url)

    return render_template('upload_responses.html')

@app.route('/backup')
def return_backup():
    return send_file('wario.txt')

if __name__ == '__main__':
    app.run()