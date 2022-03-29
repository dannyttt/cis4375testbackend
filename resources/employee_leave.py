from flask_restful import Resource, reqparse
from models.employee import EmployeeLeaveModel
from schemas.employee import EmployeeLeaveSchema

employee_leave_schema = EmployeeLeaveSchema()
employee_leave_list_schema = EmployeeLeaveSchema(many=True)


class EmployeeLeave(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('category',
                        type=str,
                        required=False,
                        help="optional"
                        )

    def get(self, category):
        employee_leave = EmployeeLeaveModel.find_by_name(category)
        if employee_leave:
            return employee_leave_schema.dump(employee_leave), 200
        return {'message': 'Category not found'}, 404

    def post(self, category):
        if EmployeeLeaveModel.find_by_name(category):
            return {'message': "A Cateogry with name '{}' already exists.".format(category)}, 400

        # get input data

        employee_leave = EmployeeLeaveModel(category)
        try:
            employee_leave.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred creating the store."}, 500

        return employee_leave_schema.dump(employee_leave), 200

    def delete(self, category):
        employee_leve = EmployeeLeaveModel.find_by_name(category)
        if employee_leve:
            employee_leve.delete_from_db()
        else:
            return {'message': 'category not found'}, 404
        return {'message': 'Category deleted',
                'Employee Leave': employee_leave_schema.dump(employee_leve)}

    def put(self, category):
        data = EmployeeLeave.parser.parse_args()

        employee_quit = EmployeeLeaveModel.find_by_name(category)
        if employee_quit:
            if data['category'] != None and not EmployeeLeaveModel.find_by_name(data['category']):
                employee_quit.category = data['category']
            else:
                return {'message': f'category already exists'}
        else:
            employee_quit = EmployeeLeaveModel(category)

        employee_quit.save_to_db()

        return employee_leave_schema.dump(employee_quit), 201


class EmployeeLeaveList(Resource):
    def get(self):
        return {"Employee-quits": employee_leave_list_schema.dump(EmployeeLeaveModel.query.all())}, 200
