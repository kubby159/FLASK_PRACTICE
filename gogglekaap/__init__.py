from urllib import response
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_flask():
        app.logger.info('RUN HELLOWORLD!')
        return "<p>Hello, Flask!</p>"
    '''Method'''
    from flask import request
   
    @app.route('/test/method/<id>', methods=['GET','POST','PUT','DELETE'])
    def method_test(id):
        return jsonify({
            "requests.method": request.method,
            "requests.form": request.form,
            "request.json": request.json
            

          
           
        })
    #Routing practice
    from flask import jsonify,redirect,url_for
    from markupsafe import escape
    @app.route('/test/name/<name>')
    def name(name):
        return f'Name is {name} , {escape(type(name))}'
    @app.route('/test/id/<int:id>')
    def id(id):
        return f'id:{ id }'


    # 경로를 받아줌
    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath
    
    @app.route('/test/json')
    def json():
        return jsonify({"HELLO":"WORLD"});

    @app.route('/test/redirect/<path:subpath>')
    def redirect_url(subpath):
        return redirect(subpath)


    @app.route('/test/urlfor/<path:subpath>')
    def urlfor(subpath):
        return redirect(url_for('path',subpath=subpath))


    '''Reuqest hook'''
    from flask import g, current_app
    @app.before_first_request
    def before_first_request():
        app.logger.info('BEFORE_FIRST_REUQEST')
    @app.before_request
    def before_request():
        g.test=True
        app.logger.info('BEFORE_REQUEST')

    @app.after_request
    def after_request(response):
        app.logger.info(f'g.test:{g.test}')
        # app.logger.info(f'current_app: {current_app.config}')
        app.logger.info('AFTER_REQUEST')
        return response

    # Request 가 완전히 마친 뒤.
    @app.teardown_request
    def teardown_request(exception):
        app.logger.info('TEARDOWN_REQUEST')
        return exception

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        app.logger.info("TEARDOWN_CONTEXT")

    if __name__ == '__main__':
        app.run(host='localhost',port='5001')

    return app