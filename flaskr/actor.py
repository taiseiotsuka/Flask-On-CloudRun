from flask import Blueprint
from flask.views import MethodView
from flask import request
from library.firebase import FireBase
import json

alias = 'actor'
actor = Blueprint(alias, __name__)

class Actor(MethodView, FireBase):

    def get(self, actor_id):
      doc = self.get_collect(alias).document(actor_id).get()
      return doc.to_dict()

    def post(self, actor_id):
      self.get_collect(alias).document(actor_id).set(json.loads(request.get_data()))
      return "Success"

actor_view = Actor.as_view(alias)
actor.add_url_rule('/%s/<actor_id>' % alias, view_func=actor_view)
