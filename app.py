from flask import Flask 


app = Flask(__name__)
TESTING = True
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return 'sub. subscribe'



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()