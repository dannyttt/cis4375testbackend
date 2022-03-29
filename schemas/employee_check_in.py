from ma import ma
from models.employee import EmployeeCheckInModel


class EmployeeCheckInSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeCheckInModel
