from v1.resources.todos import todos, main


def initialize_routes(api):
    api.add_namespace(main)
    api.add_namespace(todos)