from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    '''
    Media Model that represents media (such as image, a video, etc.) associated with a figure, a culture, or a story

    @type name: models.Charfield(200)
    @cvar name: Name of the media
    @type kind: models.Charfield(200)
    @cvar kind: The kind/category of the media instance
    @type link: models.Charfield(200)
    @cvar link: URL to the media
    @type figure: models.ForeignKey('Figure')
    @cvar figure: Foreign key associating this media to a figure
    @type culture: models.ForeignKey('Culture')
    @cvar culture: Foreign key associating this media to a culture
    @type story: models.ForeignKey('Story')
    @cvar story: Foreign key associating this media to a story
    '''
    name                = models.CharField(max_length=200)
    kind                = models.CharField(max_length=200)
    link                = models.CharField(max_length=200)
    figure              = models.ForeignKey('Figure', blank=True, null=True)
    culture             = models.ForeignKey('Culture', blank=True, null=True)
    story               = models.ForeignKey('Story', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Figure(models.Model):
    '''
    figure Model represents an instance of a figure in mythology

    @type name: models.CharField(200)
    @cvar name: Name of the figure
    @type kind: models.CharField(200)
    @cvar kind: Kind of the figure
    @type biography: models.CharField(10000)
    @cvar biography: Short description/bio of the figure
    @type related_figures: models.ManyToManyField('self')
    @cvar related_figures: Many to many assocation associating other related figures to this figure instance
    @type related_cultures: models.ManyToManyField('Culture')
    @cvar related_cultures: Many to many assocation associating related cultures to this figure instance
    @type related_stories: models.ManyToManyField('Story')
    @cvar related_stories: Many to many assocation associating related stories that this figure instance is in
    '''
    name                = models.CharField(max_length=200)
    kind                = models.CharField(max_length=200)
    biography           = models.CharField(max_length=10000)
    related_figures     = models.ManyToManyField('self')
    related_cultures    = models.ManyToManyField('Culture')
    related_stories     = models.ManyToManyField('Story')

    def __unicode__(self):
        return self.name

class Story(models.Model):
    '''
    Story model represents an instance of a mythological event/story
    
    @type name: models.CharField(200)
    @cvar name: Name of Story instance
    @type summary: models.CharField(10000)
    @cvar summary: Short description/summary of the story
    @type related_figures: models.ManyToManyField('Figure')
    @cvar related_figures: Many to many assocation linking to any related figures associated with this story
    @type related_cultures: models.ManyToManyField('Culture')
    @cvar related_cultures: Many to many assocation linking to any related cultures that may be associated with this story
    @type related_stories: models.ManyToManyField('self')
    @cvar related_stories: Many to many assocation linking to any other stories that may be related to this story instance
    '''
    name                = models.CharField(max_length=200)
    summary             = models.CharField(max_length=10000)
    related_stories     = models.ManyToManyField('self')
    related_cultures    = models.ManyToManyField('Culture')

    def __unicode__(self):
        return self.name


class Culture(models.Model):
    '''
    Culture model represents an instance of a culture (e.g. Greek, Scandinavian, Roman...)

    @type name: models.CharField(200)
    @cvar name: Name of the culture
    @type region: models.CharField(200)
    @cvar region:  Region location of the Culture
    @type history: models.CharField(10000)
    @cvar history: Summary of the history of this Culture instance
    @type language: models.CharField(200)
    @cvar language: Most common language spoken in this culture
    @type related_figures: models.ManyToManyField('Figure')
    @cvar related_figures: Many to many assocation associating Figures related to this Culture
    @type related_cultures: models.ManyToManyField('self')
    @cvar related_cultures: Many to many assocation associating Cultures similar to this Culture
    @type related_stories: models.ManyToManyField('Story')
    @cvar related_stories:  Many to many assocation associating notable mythological stories belonging within this Culture
    '''
    name                = models.CharField(max_length=200)
    region              = models.CharField(max_length=200)
    history             = models.CharField(max_length=10000)
    language            = models.CharField(max_length=200)
    related_cultures    = models.ManyToManyField('self')

    def __unicode__(self):
        return self.name
