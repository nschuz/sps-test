import json
from flask import abort, jsonify, request , make_response
from flask_restplus import Namespace, Resource
from v1.model.models import Todo
from mongoengine import DoesNotExist

todos = Namespace('v1/todos', description='Todos namespace')


@todos.route('/')
class TodosApi(Resource):
    def get(self):
        '''List all Todos'''
        todos = Todo.objects.all()
        return json.loads(todos.to_json()), 200
    
    def post(self):
        """Create a new todo"""
        #data = request.get_json() 
        # # status code
        json_data = request.get_json(force=True)
        title = json_data["title"]
        content = json_data["content"]
        response = Todo.objects.insert(Todo(title=title,content=content))
        print(response)
        return make_response(jsonify({'data': json_data}), 201)

@todos.route('/<id>')
@todos.response(404, 'Todo not found')
@todos.param('id', 'The task identifier')
class TodoApi(Resource):
    def get(self, id):
        '''Fetch a given Todo'''
        try:
            todo = Todo.objects.get(id=id)
            return json.loads(todo.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(404)
            
        
