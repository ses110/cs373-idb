from django.db import models

class Relations(models.Model):
   pass 

class Figures(Models.Model):
    '''
    figure Model

    @type figure_id: models.CharField(200, primary_key = True)
    @cvar figure_id: A figure's primary key to uniquely identify the instance
    
    '''
    figure_id = models.CharField(max_length=200, primary_key=True)
    name    = models.CharField(max_length=200)
    origin  = models.CharField(max_length=200)
    strengths = models.CharField(max_length=200)
    weaknesses = models.CharField(max_length=200)
    short_bio = models.CharField(max_length=2000)
    father = models.ForeignKey(Figures)
    mother = models.ForeignKey(Figures)
    culture = models.OneToOneField(Cultures)

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: figure
        @param self: Current figure instance

        @rtype: string
        @return: The id associated with this figure instance  
        """
        return self.figure_id

class Story(Models.Model):
    story_id = models.CharField(max_length=200, primary_key=True)
    name     = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    culture  = models.ForeignKey(Cultures)
    summary  = models.CharField(max_length=10000)
    start_date = models.DateTimeField("Beginning date of story")
    end_date = models.DateTimeField("Ending date of story")

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: story
        @param self: Current story instance

        @rtype: string
        @return: The id associated with this story instance
        """
        return self.story_id

class Cultures(Models.Model):
    culture_id = models.CharField(max_length=200, primary_key=True)
    name   = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    timespan_startdate = models.DateTimeField("Beginning timespan of culture")
    timespan_enddate = models.DateTimeField("Ending timespan of culture")

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: culture
        @param self: Current culture instance

        @rtype: string
        @return: The id associated with this culture instance
        """
        return self.culture_id
