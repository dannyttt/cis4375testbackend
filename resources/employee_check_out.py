from flask_restful import Resource, reqparse
from models.employee import EmployeeCheckOutModel
from schemas.employee_check_out import EmployeeCheckOutSchema
from sqlalchemy import exc

employee_check_out_schema = EmployeeCheckOutSchema()
employee_check_out_list_schema = EmployeeCheckOutSchema(many=True)


class EmployeeCheckOut(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('category',
                        type=str,
                        required=False,
                        help="optional"
                        )

    def get(self, category):
        check_out = EmployeeCheckOutModel.find_by_name(category)
        if check_out:
            return employee_check_out_schema.dump(check_out), 200
        return {'message': 'Category not found'}, 404

    def post(self, category):
        if EmployeeCheckOutModel.find_by_name(category):
            return {'message': "A Cateogry with name '{}' already exists.".format(category)}, 400

        # get input data

        check_out = EmployeeCheckOutModel(category)
        try:
            check_out.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred creating the store."}, 500

        return employee_check_out_schema.dump(check_out), 200

    def delete(self, category):
        check_out = EmployeeCheckOutModel.find_by_name(category)
        if check_out:
            check_out.delete_from_db()
        else:
            return {'message': 'category not found'}, 404
        return {'message': 'Category deleted',
                'Employee Check In': employee_check_out_schema.dump(check_out)}

    def put(self, category):
        data = EmployeeCheckOut.parser.parse_args()

        check_out = EmployeeCheckOutModel.find_by_name(category)
        if check_out:
            if data['category'] != None and check_out.category != data['category']:
                check_out.category = data['category']
            else:
                return {"message": "category already exists"}
        else:
            check_out = EmployeeCheckOutModel(category)
        check_out.save_to_db()
        return employee_check_out_schema.dump(check_out), 201


class Employee_Check_Out_List(Resource):
    def get(self):
        return {"Category": employee_check_out_list_schema.dump(EmployeeCheckOutModel.query.all())}, 200
