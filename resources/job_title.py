from flask_restful import Resource, reqparse
from models.employee import JobTitleModel
from schemas.job_title import JobTitleSchema

job_title_schema = JobTitleSchema()
job_title_list_schema = JobTitleSchema(many=True)


class JobTitle(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('title',
                        type=str,
                        required=False,
                        help="optional"
                        )

    def get(self, title):
        job_title = JobTitleModel.find_by_name(title)
        if job_title:
            return job_title_schema.dump(job_title), 200
        return {'message': 'title not found'}, 404

    def post(self, title):
        if JobTitleModel.find_by_name(title):
            return {'message': "A Cateogry with name '{}' already exists.".format(title)}, 400

        # get input data

        job_title = JobTitleModel(title)
        try:
            job_title.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occurred creating the store."}, 500

        return job_title_schema.dump(job_title), 200

    def delete(self, title):
        job_title = JobTitleModel.find_by_name(title)
        if job_title:
            job_title.delete_from_db()
        else:
            return {'message': 'title not found'}, 404
        return {'message': 'title deleted',
                'title': job_title_schema.dump(job_title)}

    def put(self, title):
        data = JobTitle.parser.parse_args()

        job_title = JobTitleModel.find_by_name(title)
        if job_title:
            if data['title'] != None and not JobTitleModel.find_by_name(data['title']):
                job_title.title = data['title']
            else:
                return {'message': f'title already exists'}
        else:
            job_title = JobTitleModel(title)

        job_title.save_to_db()

        return job_title_schema.dump(job_title), 201


class JobTitleList(Resource):
    def get(self):
        return {"Job Title": job_title_list_schema.dump(JobTitleModel.query.all())}, 200
