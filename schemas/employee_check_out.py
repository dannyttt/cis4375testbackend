from ma import ma
from models.employee import EmployeeCheckOutModel


class EmployeeCheckOutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeCheckOutModel
