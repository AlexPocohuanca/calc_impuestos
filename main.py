from website import create_app
import os
app = create_app()

print('main!')
#port = int(os.getenv('PORT'))

if __name__ == '__main__':
    print('app.run')
    #try:
    app.run(debug=True, use_reloader=False) #, port = port)
    #finally:
    print('I shat myself')
        #pass


        
