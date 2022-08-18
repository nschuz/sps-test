import json
from flask import abort, jsonify, request , make_response
from flask_restplus import Namespace, Resource
from v1.model.models import Todo
from mongoengine import DoesNotExist

main =   Namespace('d/', description="Root namespace")
todos = Namespace('v1/todos', description='Todos namespace')


@main.route('/helth-check')
class Health(Resource):
    def get(self):
        '''List all Todos'''
        
        respose = {
            "services":{
                "api-flask":"online",
                "db-mongo":"online"
            }
        }
        
        try:
            Todo(title="testx007", description="testx007").save()
            saved = True
        except Exception as e:
            saved = False
            raise e
        finally:
            if saved:
                Todo.objects.get(title="testx007").delete()
                return json.loads(respose), 200
        response = response["services"]["db-mongo"]="down"
        return json.loads(respose), 200    

@todos.response(400, 'bad request')
@todos.route('/')
class TodosApi(Resource):
    def get(self):
        '''List all Todos'''
        todos = Todo.objects.all()
        return json.loads(todos.to_json()), 200
    
    def post(self):
        """Create a new todo"""

        json_data = request.get_json(force=True)
        title = json_data.get('title', None)
        content = json_data.get('content', None)
        
        if  title and content:    
            Todo.objects.insert(Todo(**json_data))
            return make_response(jsonify({'data': json_data}), 201)
        else:
            return make_response(jsonify({'message': 'title and content must be required.'}), 400)
        

@todos.route('/<id>', '/<title>')
@todos.response(404, 'Todo not found')
@todos.param('id', 'The task identifier')
@todos.param('title' , 'The title identifier')
class TodoApiManager(Resource):
    def get(self, id=None, title=None):
        '''Fetch a given Todo by id or by title'''
        try:
            if id:
                todo = Todo.objects.get(id=id)
            elif title:
                todo = Todo.objects.get(title=title)
            
            return json.loads(todo.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(404)
            
        
    def put(self, id=None , title=None):
        """Create a new todo"""

        json_data = request.get_json(force=True)
        #title = json_data.get('title', None)
        #content = json_data.get('content', None)
        try:
            if id:
                todo = Todo.objects.get(id=id)
                
            elif title:
                todo = Todo.objects.get(title=title)
            
            return json.loads(todo.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(404)