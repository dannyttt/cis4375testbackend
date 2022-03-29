from flask import Flask
from flask_restful import Api


# from flask_sqlalchemy import SQLAlchemy
from db import db
from ma import ma


from resources.store import Store, StoreList
from resources.employee_quit import EmployeeQuit, EmployeeQuitList
from resources.employee_leave import EmployeeLeave, EmployeeLeaveList
from resources.job_title import JobTitleList, JobTitle
from resources.employee_check_in import EmployeeCheckIn, Employee_Check_In_List
from resources.employee_check_out import EmployeeCheckOut, Employee_Check_Out_List


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    print('tables created')


# store api endpoints
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# Employee
# Empployee quit
api.add_resource(EmployeeQuit, '/employee-quit/<string:category>')
api.add_resource(EmployeeQuitList, '/employee-quits')
# employee leave
api.add_resource(EmployeeLeave, '/employee-leave/<string:category>')
api.add_resource(EmployeeLeaveList, '/employee-leaves')
# job title
api.add_resource(JobTitle, '/job-title/<string:title>')
api.add_resource(JobTitleList, '/job-titles')
# employee check in
api.add_resource(EmployeeCheckIn, '/employee-check-in/<string:category>')
api.add_resource(Employee_Check_In_List, '/employee-check-ins')
# employee check out
api.add_resource(EmployeeCheckOut, '/employee-check-out/<string:category>')
api.add_resource(Employee_Check_Out_List, '/employee-check-outs')
# employee log in

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
