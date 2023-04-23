from flask import Flask, render_template, request, redirect, send_file, jsonify, Response
from flask_cors import CORS
#from flask_socketio import SocketIO, emit
import os
import subprocess
import json
import time
from cfgexplorer import cfg_explore

app = Flask(__name__)

# configuration
UPLOAD_FOLDER = os.path.abspath('upload')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FLASK_ENV'] = "development"
file_dir = app.config['UPLOAD_FOLDER']
CORS(app, resources=r'/*')
DEBUG = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getJson', methods=['GET', 'POST'])
def getJson():
    pass


@app.route('/getCFG',methods=['get','POST'])
#@cross_origin(origin="localhost:8080")
def getCFG():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # delete cfg_output.cfg if exist
        if os.path.exists("cfg_output.svg"):
            os.remove("cfg_output.svg")
        if os.path.exists("../frontend/public/cfg_output.svg"): 
            os.remove("../frontend/public/cfg_output.svg")
        cfg_explore(file_dir + '/' + filename,launch=False,output='./cfg_output.svg')
        print("waiting")
        '''
        time for cfg_output.cfg generation,synchronous problem
        '''
        while not os.path.exists("cfg_output.svg"):
            time.sleep(1)
            print("waiting waiting")
        # subprocess.run(['python', 'cfg_display.py', file_dir + '/' + filename])
        print("file  finish")
        if os.path.exists("cfg_output.svg"):
            # ugly way to console the response
            subprocess.run(['mv','cfg_output.svg','../frontend/public'])
            #return send_file("cfg_output.svg")
            return "cfg_output.svg"
        else:
            print("cfg_output.svg not exist\n")
        
        


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
            out_dir = "output"
            filename = file.filename
            '''
            # using file to store text and return text
            subprocess.call(["python","process.py",target])
            report_file = target.replace("upload","output")+"/report.txt"
            result = open(report_file,"r").read()
            '''

            # using json
            target = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(target)
            #result = subprocess.run(['python', 'process.py', file_dir + '/' + filename], capture_output=True, text=True)
            result = subprocess.check_output(['python', 'process.py', target])
            result = result.decode().split('\n')
            resultJson = []
            for i in result:
                resultJson.append({"result":i})
            print("resultJson:",resultJson)
            with open(out_dir + '/' + filename + ".json","w") as fp:
                json.dump(resultJson,fp)
                fp.close()
            return jsonify({'result': result.split('\n')})
                

        return redirect('/')    
    else:

        return redirect('/')  
    

if __name__ == '__main__':
    app.run(debug=True)






