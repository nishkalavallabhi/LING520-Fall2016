from bottle import get, post, request, route, template, run

@route('/')
@route('/upload')
def uploadfile():
    html_code = '''<form action="/upload" method="post" enctype="multipart/form-data">
  Select a text file: <input type="file" name="upload" />
  <input type="submit" value="Upload file" />
</form>'''
    return html_code

@post('/upload')
def afterupload():
    uploaded_file = request.files.get('upload')
    if uploaded_file.filename.endswith(".txt"):
        uploaded_file.save("uploadedfile.txt", "w")
        return "You uploaded the right kind of file and it is successfully saved on the server"
    else:
        return "Wrong extension. Only .txt allowed"

run()