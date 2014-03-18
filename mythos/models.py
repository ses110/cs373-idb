from django.db import models

class Relations(models.Model):
   pass 

class Figure(models.Model):
    '''
    figure Model

    @type figure_id: models.CharField(200, primary_key = True)
    @cvar figure_id: A figure's primary key to uniquely identify the instance
    
    '''
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=200)
    kind                = models.CharField(max_length=200) #possibly change to models.choices
    description         = models.CharField(max_length=2000)
    images              = models.CharField(max_length=200)
    videos              = models.CharField(max_length=200)
    related_figures     = models.ForeignKey('Figure')
    related_cultures    = models.ForeignKey('Culture')
    related_stories     = models.ForeignKey('Story')
    external_links      = models.CharField(max_length=200)

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: figure
        @param self: Current figure instance

        @rtype: string
        @return: The id associated with this figure instance  
        """
        return self.id

class Story(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=200)
    
    description         = models.CharField(max_length=10000)
    images              = models.CharField(max_length=200)
    videos              = models.CharField(max_length=200)
    related_figures     = models.ForeignKey('Figure')
    related_cultures    = models.ForeignKey('Culture')
    related_stories     = models.ForeignKey('Story')
    external_links      = models.CharField(max_length=200)

  
    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: story
        @param self: Current story instance

        @rtype: string
        @return: The id associated with this story instance
        """
        return self.id

class Culture(models.Model):
    id                  = models.CharField(max_length=200, primary_key=True)
    name                = models.CharField(max_length=200)
    region              = models.CharField(max_length=200)
    history             = models.CharField(max_length=10000)
    language            = models.CharField(max_length=200)
    images              = models.CharField(max_length=200)
    videos              = models.CharField(max_length=200)
    related_figures     = models.ForeignKey('Figure')
    related_cultures    = models.ForeignKey('Culture')
    related_stories     = models.ForeignKey('Story')
    external_links      = models.CharField(max_length=200)


    # timespan_startdate = models.DateTimeField("Beginning timespan of culture")
    # timespan_enddate = models.DateTimeField("Ending timespan of culture")

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: culture
        @param self: Current culture instance

        @rtype: string
        @return: The id associated with this culture instance
        """
        return self.id
