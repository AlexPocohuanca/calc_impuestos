from website import create_app
import os
from os import environ
app = create_app()

print('main!')
#port = int(os.getenv('PORT'))

if __name__ == '__main__':
    print('app running')
    #try:
    #app.run(debug=True, use_reloader=False) #, port = port)
    app.run(debug=False, port=environ.get("PORT", 5000))#, processes=2)
    #finally:
    print('I shat myself')
        #pass


        
