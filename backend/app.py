from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from flask_cors import CORS
#from flask_socketio import SocketIO, emit
import os
import subprocess

app = Flask(__name__)
'''
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
'''

UPLOAD_FOLDER = os.path.abspath('upload')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
file_dir = app.config['UPLOAD_FOLDER']
CORS(app, resources=r'/*')
# configuration
DEBUG = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # 渲染文件
    return render_template('upload.html')

@app.route('/cfg',methods=['POST'])
#@cross_origin(origin="localhost:8080")
def cfg():
    pass


@app.route('/upload_file',methods=['POST'])
#@cross_origin(origin="localhost:8080")
def upload_file():
    """
        文件上传
    """
    
    if request.method == 'POST':
        if 'file' not in request.files:
            print("debug1",request.url)
            return redirect('/')
        
        # input标签中的name的属性值
        file = request.files['file']
        if file.filename == '':
            print("debug2",request.url)
            return redirect('/')

        # 拼接地址，上传地址，f.filename：直接获取文件名
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = subprocess.run(['python', 'process.py', file_dir + '/' + filename], capture_output=True, text=True)
            print("result:",result)
            return render_template('index.html', result=result.stdout)
        
        print("debug3",request.url)
        return redirect('/')    
    else:
        return render_template('upload.html')
    
    
'''
    # 调用 process.py 处理二进制文件并获取 stdout
    process = subprocess.Popen(["python", "process.py", binary_path], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    print("output:",output)

    # 返回 stdout
    return Response(output, mimetype="text/plain")
'''

if __name__ == '__main__':
    app.run(debug=True)






