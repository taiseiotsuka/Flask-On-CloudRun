import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

class FireBase:
  def __init__(self):
    if (not len(firebase_admin._apps)):
      cred = credentials.ApplicationDefault()
      firebase_admin.initialize_app(cred, { 'projectId': os.getenv('GOOGLE_PROJECT_ID') })
    self.client = firestore.client()

  def get_collect(self, name):
    return self.client.collection(name)