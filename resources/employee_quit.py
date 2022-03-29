from flask_restful import Resource, reqparse
from models.employee import EmployeeQuitModel
from schemas.employee import EmployeeQuitSchema

employee_quit_schema = EmployeeQuitSchema()
employee_quit_list_schema = EmployeeQuitSchema(many=True)


class EmployeeQuit(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('category',
                        type=str,
                        required=False,
                        help="optional"
                        )

    def get(self, category):
        employee_quit = EmployeeQuitModel.find_by_name(category)
        if employee_quit:
            return employee_quit_schema.dump(employee_quit), 200
        return {'message': 'Category not found'}, 404

    def post(self, category):
        if EmployeeQuitModel.find_by_name(category):
            return {'message': "A Cateogry with name '{}' already exists.".format(category)}, 400

        # get input data

        employee_quit = EmployeeQuitModel(category)
        try:
            employee_quit.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred creating the store."}, 500

        return employee_quit_schema.dump(employee_quit), 200

    def delete(self, category):
        employee_quit = EmployeeQuitModel.find_by_name(category)
        if employee_quit:
            employee_quit.delete_from_db()
        else:
            return {'message': 'category not found'}, 404
        return {'message': 'Category deleted',
                'Category': employee_quit_schema.dump(employee_quit)}

    def put(self, category):
        data = EmployeeQuit.parser.parse_args()

        employee_quit = EmployeeQuitModel.find_by_name(category)
        if employee_quit:
            if data['category'] != None and not EmployeeQuitModel.find_by_name(data['category']):
                employee_quit.category = data['category']
            else:
                return {'message': f'category already exists'}
        else:
            employee_quit = EmployeeQuitModel(category)

        employee_quit.save_to_db()

        return employee_quit_schema.dump(employee_quit), 201


class EmployeeQuitList(Resource):
    def get(self):
        return {"Employee-quits": employee_quit_list_schema.dump(EmployeeQuitModel.query.all())}, 200
