from flask import Flask 


application = Flask(__name__)
TESTING = True
UPLOAD_FOLDER = 'static/upload'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@application.route('/')
def hello_world():
    return 'sub. subscribe'



def main():
    application.run(debug=True)

if __name__ == '__main__':
    main()