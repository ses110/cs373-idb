from haystack import indexes
from mythos.models import *

class FigureIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    kind = indexes.CharField(model_attr='kind')
    bio = indexes.CharField(model_attr='biography')

    name_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Figure

class StoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    summary = indexes.CharField(model_attr='summary')

    name_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Story

class CultureIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    history = indexes.CharField(model_attr='history')
    language = indexes.CharField(model_attr='language')

    name_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Culture
