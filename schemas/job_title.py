from ma import ma
from models.employee import JobTitleModel


class JobTitleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = JobTitleModel
