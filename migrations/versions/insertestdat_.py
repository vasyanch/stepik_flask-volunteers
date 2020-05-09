import json

from volunteers.app import db
from volunteers.models import Volunteer, Street, District


def insert_test_data():
    all_objects = []
    with open('test_data/volunteers.json', encoding='utf8') as volunteers_file:
        volunteers_data = json.load(volunteers_file)
        volunteers = [
            Volunteer(id=int(id_), name=vol['name'], userpic=vol['userpic'], phone=vol['phone'])
            for id_, vol in volunteers_data.items()
        ]
    all_objects.extend(volunteers)

    with open('test_data/streets.json', encoding='utf8') as streets_file:
        streets_data = json.load(streets_file)
        streets = [
            Street(id=int(id_), title=st['title'], volunteers=list(filter(lambda x: x.id in st['volunteer'], volunteers)))
            for id_, st in streets_data.items()
        ]
    all_objects.extend(streets)

    with open('test_data/districts.json', encoding='utf8') as districts_file:
        districts_data = json.load(districts_file)
        districts = [
            District(id=int(id_), title=ds['title'], streets=list(filter(lambda x: x.id in ds['streets'], streets)))
            for id_, ds in districts_data.items()
        ]
    all_objects.extend(districts)

    db.session.add_all(all_objects)
    db.session.commit()


revision = 'insertestdat'
down_revision = '19e1224f3cf1'
branch_labels = None
depends_on = None


def upgrade():
    insert_test_data()


def downgrade():
    pass
