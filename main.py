from website import create_app
import os
app = create_app()

print('main!')
#port = int(os.getenv('PORT'))

if __name__ == '__main__':
    #try:
        app.run(debug=True) #, port = port)
    #finally:
        print('caca')
        #pass


        
