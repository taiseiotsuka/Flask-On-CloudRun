from routes import app
from dotenv import load_dotenv
import os

if os.getenv('FLASK_DEBUG'):
  load_dotenv('instance/config/dev.cfg')
else:
  load_dotenv('instance/config/prod.cfg')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)