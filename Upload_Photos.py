from flask import Flask, render_template, url_for, g, request, redirect, send_from_directory
import os
from werkzeug.utils import secure_filename

DEBUG = True
MAX_CONTENT_LENGTH = 1024 * 1024
UPLOAD_FOLDER = r'.\static\images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config.from_object(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/Upload_Photo', methods=['GET', 'POST'])
def Upload_Photo():
    images = os.listdir(os.path.join(app.static_folder, "images"))
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("Form.html", images=images)


@app.route('/Upload_Photo')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True)
