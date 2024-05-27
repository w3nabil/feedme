from pack import server
from pack import db

if __name__ == '__main__':
    app = server()
    app.run(host='0.0.0.0', port=5000 ,debug=True)