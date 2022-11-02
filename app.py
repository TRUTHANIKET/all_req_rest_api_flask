from flask import Flask ,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse,Resource,Api,abort

app=Flask(__name__)

flatujsonvalue={
    1:{"Name":"aniket","password":"23131313"},
     2:{"Name":"Ram","password":"efaf"}
}
tak_post_api=reqparse.RequestParser()
tak_post_api.add_argument("Name",type=str,help="name is required",required=True)
tak_post_api.add_argument("password",type=str,help="pass is required",required=True)


tak_put_api=reqparse.RequestParser()
tak_put_api.add_argument("Name",type=str)
tak_put_api.add_argument("password",type=str)


#totoal return value
class TodoList(Resource):
    def get(self):
        return flatujsonvalue


#single /post request as well
class Todo(Resource):
    def get(self,todo_id):
        return flatujsonvalue[todo_id]



    def post(self,todo_id):
        arg=tak_post_api.parse_args()
        if todo_id in flatujsonvalue :
            abort(409  ,message='''why the hell are u adding it again''')
        
        flatujsonvalue[todo_id] = { "Name" : arg["Name"],"password" : arg["password"]}
        return jsonify("200 Server Ok your account has been successfully added")

    def delete(self,todo_id):
        del flatujsonvalue[todo_id]
        return jsonify("your acc has been successfully deleted")
    
    def put(self,todo_id):
        argput=tak_put_api.parse_args()
        if todo_id not in flatujsonvalue:
            abort(409,message="cannot delete the value")
        if argput['Name']:
            flatujsonvalue[todo_id] ['Name']=argput['Name']
        if argput['password']:
            flatujsonvalue[todo_id] ['password']=argput['password']

        return  flatujsonvalue[todo_id] 
        
       




api=Api(app)
api.add_resource(Todo,'/todo/<int:todo_id>')
api.add_resource(TodoList,'/todo')

@app.route("/")
def index():
    return "hello world"


if __name__=="__main__":
    app.run(debug=True)
