from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/output'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def apply_filter(image_path, filter_name, **kwargs):
    img = cv2.imread(image_path)

    if img is None:
        return None

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if filter_name == 'grayscale':
        result = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    elif filter_name == 'binary':
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, result = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)

    elif filter_name == 'hsv':
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        result = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    elif filter_name == 'blur':
        amount = kwargs.get('amount', 5)

        if amount < 1:
            amount = 1

        if amount > 21:
            amount = 21

        if amount % 2 == 0:
            amount += 1

        result = cv2.GaussianBlur(img, (amount, amount), 0)

    elif filter_name == 'brightness':
        factor = kwargs.get('factor', 1.0)

        if factor < 0.5:
            factor = 0.5

        if factor > 2.0:
            factor = 2.0

        result = cv2.convertScaleAbs(img, alpha=factor, beta=0)

    elif filter_name == 'edges':
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        result = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    elif filter_name == 'sharpen':
        kernel = np.array([
            [-1, -1, -1],
            [-1,  9, -1],
            [-1, -1, -1]
        ])

        result = cv2.filter2D(img, -1, kernel)

    elif filter_name == 'dilation':
        kernel_size = kwargs.get('kernel_size', 5)
        iterations = kwargs.get('iterations', 1)

        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        result = cv2.dilate(
            img,
            kernel,
            iterations=iterations
        )

    elif filter_name == 'erosion':
        kernel_size = kwargs.get('kernel_size', 5)
        iterations = kwargs.get('iterations', 1)

        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        result = cv2.erode(
            img,
            kernel,
            iterations=iterations
        )

    elif filter_name == 'opening':
        kernel_size = kwargs.get('kernel_size', 5)
        iterations = kwargs.get('iterations', 1)

        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        result = cv2.morphologyEx(
            img,
            cv2.MORPH_OPEN,
            kernel,
            iterations=iterations
        )

    elif filter_name == 'closing':
        kernel_size = kwargs.get('kernel_size', 5)
        iterations = kwargs.get('iterations', 1)

        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        result = cv2.morphologyEx(
            img,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=iterations
        )

    else:
        result = img

    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)

    output_filename = f"{name}_{filter_name}{ext}"
    output_path = os.path.join(
        app.config['OUTPUT_FOLDER'],
        output_filename
    )

    result_pil = Image.fromarray(result)
    result_pil.save(output_path)

    return output_filename


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        if 'file' not in request.files:
            return render_template(
                'index.html',
                error='No file uploaded'
            )

        file = request.files['file']

        if file.filename == '':
            return render_template(
                'index.html',
                error='No file selected'
            )

        if not allowed_file(file.filename):
            return render_template(
                'index.html',
                error='Invalid file type'
            )

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        file.save(filepath)

        allowed_filters = {
            'grayscale',
            'binary',
            'hsv',
            'blur',
            'brightness',
            'edges',
            'sharpen',
            'dilation',
            'erosion',
            'opening',
            'closing'
        }

        filter_name = request.form.get(
            'filter',
            'grayscale'
        )

        if filter_name not in allowed_filters:
            return render_template(
                'index.html',
                error='Invalid filter selected'
            )

        params = {}

        if filter_name == 'blur':

            amount = int(
                request.form.get(
                    'blur_amount',
                    5
                )
            )

            if amount < 1:
                amount = 1

            if amount > 21:
                amount = 21

            if amount % 2 == 0:
                amount += 1

            params['amount'] = amount

        elif filter_name == 'brightness':

            factor = float(
                request.form.get(
                    'brightness_factor',
                    1.0
                )
            )

            if factor < 0.5:
                factor = 0.5

            if factor > 2.0:
                factor = 2.0

            params['factor'] = factor

        elif filter_name in {
            'dilation',
            'erosion',
            'opening',
            'closing'
        }:

            kernel_size = int(
                request.form.get(
                    'kernel_size',
                    5
                )
            )

            iterations = int(
                request.form.get(
                    'iterations',
                    1
                )
            )

            if kernel_size not in [3, 5, 7]:
                kernel_size = 5

            if iterations < 1:
                iterations = 1

            if iterations > 5:
                iterations = 5

            params['kernel_size'] = kernel_size
            params['iterations'] = iterations

        output_filename = apply_filter(
            filepath,
            filter_name,
            **params
        )

        if output_filename is None:
            return render_template(
                'index.html',
                error='Unable to process the image'
            )

        return render_template(
            'index.html',
            original=filename,
            processed=output_filename,
            filter_applied=filter_name
        )

    return render_template('index.html')


@app.route('/download/<filename>')
def download(filename):

    file_path = os.path.join(
        app.config['OUTPUT_FOLDER'],
        filename
    )

    return send_file(
        file_path,
        as_attachment=True
    )


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )