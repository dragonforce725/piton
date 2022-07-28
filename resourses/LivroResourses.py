from flask_restful import Resource

bd_fake = [
    {'id': 1, 'nome': 'as aventuras de pipi', 'preço': 20.90},
    {'id': 2, 'nome': 'as aventuras de pipi 1', 'preço': 20.90},
    {'id': 3, 'nome': 'as aventuras de pipi 2', 'preço': 20.90},
    {'id': 4, 'nome': 'as aventuras de pipi 3', 'preço': 20.90}
]

class LivrosResource(Resource):
    def get(self):
        return { 'status', "sucess", 'data': [bd_fake]}

class LivroResource(Resource):
    def get(self, livro_id):
        for livro in bd_fake:
            if livro.get('id') == livro_id:
                return{
                    'status': 'success',
                    "data": [livro]
                }
        return {
            'status': 'error',
            'data': [{'mensagem': 'livro não encontrado!'}]
        }, 404

    def post(self):
        pass
    def put(self):
        pass
