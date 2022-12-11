from flask import Flask, flash, request, redirect, url_for, render_template, jsonify,Response,after_this_request
from werkzeug.utils import secure_filename
import os
from utils.face_comparison import verify_face


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/face_match', methods=['POST'])
def face_match():
    result ={}
    source_file = request.files['source_file']
    destination_file = request.files['destination_file']
    if (source_file.filename == '' or destination_file.filename == ''):
        result['statusCode'] = 200
        result['message'] = 'No image selected for uploading'
        return result
    if (source_file and allowed_file(source_file.filename)) or (destination_file and allowed_file(destination_file.filename)):
        for filename in os.listdir('static/uploads/'):
            os.remove('static/uploads/' + filename)
        source_filename = secure_filename(source_file.filename)
        destination_filename = secure_filename(destination_file.filename)

        source_file.save(os.path.join(app.config['UPLOAD_FOLDER'], source_filename))
        destination_file.save(os.path.join(app.config['UPLOAD_FOLDER'], destination_filename))

        result = verify_face('static/uploads/'+source_filename,'static/uploads/'+destination_filename)
        result['statusCode'] = 200
        result['message']='success'
        return result
    else:
        result['statusCode'] = 200
        result['message'] = 'Allowed image types are -> png, jpg, jpeg'
        return result


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5007)