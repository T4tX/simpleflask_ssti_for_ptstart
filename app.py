from flask import Flask,render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to the home page!</h1>"

@app.errorhandler(404)
def page_not_found(e):
    error_page = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>404: Page not found</title>
</head>
<body>
    <div class="App_wrapper">
        <div class="form_box">
            <h1>404 Error Page</h1>
            <section class="error-container">
            </section>
	    <h1>
		    _PATH_ not found!
	    </h1>
            <div class="link-container">
		    <a target="_blank" href="/" class="more-link">Back to homepage</a>
            </div>
        </div>
    </div>
</body>
</html>

'''
    error_page = error_page.replace('_PATH_', request.path)
    return render_template_string(error_page), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)