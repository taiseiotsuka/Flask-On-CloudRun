from flask import Blueprint

example = Blueprint('example', __name__)

@example.route('/example/hello')
def hello():
  return 'Hello World!!'

@example.route('/example/user/<int:id>')
def user(id):
  print(id)
  return 'UserId: %d' % id