from flask_restful import Resource, reqparse
from models.employee import EmployeeCheckInModel
from schemas.employee_check_in import EmployeeCheckInSchema
from sqlalchemy import exc

employee_check_in_schema = EmployeeCheckInSchema()
employee_check_in_list_schema = EmployeeCheckInSchema(many=True)


class EmployeeCheckIn(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('category',
                        type=str,
                        required=False,
                        help="optional"
                        )

    def get(self, category):
        check_in = EmployeeCheckInModel.find_by_name(category)
        if check_in:
            return employee_check_in_schema.dump(check_in), 200
        return {'message': 'Category not found'}, 404

    def post(self, category):
        if EmployeeCheckInModel.find_by_name(category):
            return {'message': "A Cateogry with name '{}' already exists.".format(category)}, 400

        # get input data

        check_in = EmployeeCheckInModel(category)
        try:
            check_in.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred creating the store."}, 500

        return employee_check_in_schema.dump(check_in), 200

    def delete(self, category):
        check_in = EmployeeCheckInModel.find_by_name(category)
        if check_in:
            check_in.delete_from_db()
        else:
            return {'message': 'category not found'}, 404
        return {'message': 'Category deleted',
                'Employee Check In': employee_check_in_schema.dump(check_in)}

    def put(self, category):
        data = EmployeeCheckIn.parser.parse_args()

        check_in = EmployeeCheckInModel.find_by_name(category)
        if check_in:
            if data['category'] != None and check_in.category != data['category']:
                check_in.category = data['category']
            else:
                return {"message": "category already exists"}
        else:
            check_in = EmployeeCheckInModel(category)
        check_in.save_to_db()
        return employee_check_in_schema.dump(check_in), 201


class Employee_Check_In_List(Resource):
    def get(self):
        return {"Category": employee_check_in_list_schema.dump(EmployeeCheckInModel.query.all())}, 200
