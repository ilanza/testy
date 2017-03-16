from flask import Flask, render_template, request
# import werkzeug


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Please go to /uploader'

@app.route('/uploader')
def upload_file():
   return app.send_static_file('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      # f.save(werkzeug.secure_filename(f.filename))
      f.save('/Users/ilanzaitoun/PycharmProjects3/flask_uploader/'+f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)

