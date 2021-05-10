from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api=Api(app)
myEmployee = {
    "Palita" : {"EmployeeName":"Palita","Salary":20000},
    "Peter" : {"EmployeeName":"Peter","Salary":30000,}
}


#Resource
class Employee(Resource):
    def get(self,name):
        return myEmployee[name]

    def post(self,name):
        return {"data": "Return Resource = "+name}
#call
api.add_resource(Employee,"/employeeinformation/<string:name>")





if __name__ == "__main__":
    app.run(debug=True)
