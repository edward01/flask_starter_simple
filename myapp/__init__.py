# import os
# from flask import Flask, render_template


# def create_app():
#     app = Flask(__name__)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     @app.route('/ping')
#     def pingpong():
#         return 'pong!'

#     @app.route('/')
#     def index():
#         return render_template('index.html')

#     return app
