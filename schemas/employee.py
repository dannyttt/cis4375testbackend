from ma import ma
from models.employee import EmployeeLeaveModel
from models.employee import EmployeeQuitModel


class EmployeeQuitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeQuitModel


class EmployeeLeaveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeLeaveModel
