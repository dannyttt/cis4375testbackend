from db import db


class EmployeeQuitModel(db.Model):
    __tablename__ = 'employee_quit'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))

    def __init__(self, category):
        self.category = category

    @classmethod
    def find_by_name(cls, category):
        return cls.query.filter_by(category=category).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class EmployeeLeaveModel(db.Model):
    __tablename__ = 'employee_leave'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))

    def __init__(self, category):
        self.category = category

    @classmethod
    def find_by_name(cls, category):
        return cls.query.filter_by(category=category).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class JobTitleModel(db.Model):
    __tablename__ = 'job_title'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    def __init__(self, title):
        self.title = title

    @classmethod
    def find_by_name(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class EmployeeCheckInModel(db.Model):
    __tablename__ = 'employee_check_in'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))

    def __init__(self, category):
        self.category = category

    @classmethod
    def find_by_name(cls, category):
        return cls.query.filter_by(category=category).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class EmployeeCheckOutModel(db.Model):
    __tablename__ = 'employee_check_out'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))

    def __init__(self, category):
        self.category = category

    @classmethod
    def find_by_name(cls, category):
        return cls.query.filter_by(category=category).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class EmployeeModel(db.Model):
    __tablename__ = 'employee'

    emp_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))
    # job_date
    # quit_date
    # comment
    # fk employee_quit_id
    # fk job_title_id
    # fk store_id
    # how to connect foreign keys
    # need to figure out how to find by id or name

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def find_by_name(cls, category):
        return cls.query.filter_by(category=category).first()
    # need to know more sqlachemy query types

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
