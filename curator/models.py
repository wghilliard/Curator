from mongoengine import Document, ReferenceField, StringField, IntField, ListField, ObjectIdField, DictField


# GENERAL DATABASE MODEL CLASSES
class Tag(Document):
    meta = {'collection': 'tags'}
    category = StringField()
    value = StringField()


class Filter(Document):
    meta = {'collection': 'filters'}
    name = StringField()
    screen = DictField()
    entry = ObjectIdField()
    # tags = ListField(ReferenceField(Tag, default=None))


class Run(Document):
    meta = {'collection': 'runs'}
    name = StringField(max_length=80)
    events = ListField(ObjectIdField())
    subRuns = ListField(ObjectIdField(default=None))


class Entry(Document):
    meta = {'collection': 'entries'}
    name = StringField()
    run = StringField()
    histograms = ListField(ObjectIdField(default=None))
    type = StringField()


class Histogram(Document):
    meta = {'collection': 'histograms'}
    filename = StringField()
    run = StringField()
    entry = StringField()
    tags = ListField(ReferenceField(Tag, default=None))
    fullPath = StringField()
    caption = StringField()
    tags = DictField()


class Config(Document):
    meta = {'collection': 'config'}
    ref_run = StringField()
    ref_entry = StringField()
    password = StringField()
    step = IntField()
    added = DictField()


# CURATOR SPECIFIC CLASS
# class SortKey(Document):
#     meta = {'collection': 'sort_keys'}
#     category = StringField()
#     value = StringField()

class Caption(Document):
    meta = {'collection': 'captions'}
    search_tring = StringField()
    text = StringField()
