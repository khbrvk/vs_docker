from main import db
from flask_admin.contrib.sqla import ModelView


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    breed = db.Column(db.String(32))
    age = db.Column(db.Integer)
    description = db.Column(db.String(256))

    def __repr__(self):
        return f'Cat {self.name}'


class UserAdmin(ModelView):
    column_searchable_list = ('name', 'breed', 'age', 'description')
    column_filters = ('name', 'breed', 'age', 'description')
    column_default_sort = [('name', True), ('breed', True)]
    can_set_page_size = True
    can_edit = True
    can_view_details = True
    page_size = 2


