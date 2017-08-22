import os.path
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import send_file
app = Flask(__name__)

WARIO_RESPONSE_FILE_PATH = 'wario.txt'
@app.route('/')
def hello_world():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == WARIO_RESPONSE_FILE_PATH:
            file.save(file.filename)
            return redirect(request.url)
        else:
            return redirect(request.url)

    return render_template('upload_responses.html')

@app.route('/backup')
def return_backup():
    if not os.path.isfile(WARIO_RESPONSE_FILE_PATH):
        return redirect('/')
    return send_file(WARIO_RESPONSE_FILE_PATH)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
