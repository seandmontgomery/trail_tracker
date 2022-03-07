import os
from website import create_app
from flask_cors import CORS, cross_origin

app = create_app()
CORS(app)

if __name__ == '__main__':
    if os.environ.get('IS_HEROKU'):
        app.run_server(port=33507)
    else:
        app.run(debug=True)