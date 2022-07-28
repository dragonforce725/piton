from flask import Flask
from flask_restful import Api

from resources.LivroResource import LivroResource, LivrosResource

app = Flask(__name__)
api = Api(app)

api.add_resource(LivrosResource,'/livros')
api.add_resource(LivroResource, '/livro/<int:livro_id>')

if __name__  == '__main__':
    app.run(debug=True)