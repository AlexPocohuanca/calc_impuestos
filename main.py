from website import create_app
import os
#app = create_app()

# port = int(os.getenv('PORT'))

#if __name__ == '__main__':
#    try:
#        app.run(debug=True) #, port = port)
#    finally:
#        pass


from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
        
