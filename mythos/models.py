from django.db import models

class Media(models.Model):
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=200)
    kind                = models.CharField(max_length=200)
    link                = models.CharField(max_length=200)
    figure              = models.ForeignKey('Figure', blank=True, null=True)
    culture             = models.ForeignKey('Culture', blank=True, null=True)
    story               = models.ForeignKey('Story', blank=True, null=True)

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: figure
        @param self: Current figure instance

        @rtype: string
        @return: The id associated with this figure instance  
        """
        return self.id

class Figure(models.Model):
    '''
    figure Model

    @type figure_id: models.CharField(200, primary_key = True)
    @cvar figure_id: A figure's primary key to uniquely identify the instance
    
    '''
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=200)
    kind                = models.CharField(max_length=200)
    biography           = models.CharField(max_length=10000)
    related_figures     = models.ForeignKey('self')
    related_cultures    = models.ForeignKey('Culture')
    related_stories     = models.ForeignKey('Story')

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
    summary             = models.CharField(max_length=10000)
    related_figures     = models.ForeignKey('Figure')
    related_cultures    = models.ForeignKey('Culture')
    related_stories     = models.ForeignKey('self')

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
    id                  = models.IntegerField(primary_key=True)
    name                = models.CharField(max_length=200)
    region              = models.CharField(max_length=200)
    history             = models.CharField(max_length=10000)
    language            = models.CharField(max_length=200)
    related_figures     = models.ForeignKey('Figure')
    related_cultures    = models.ForeignKey('self')
    related_stories     = models.ForeignKey('Story')

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: culture
        @param self: Current culture instance

        @rtype: string
        @return: The id associated with this culture instance
        """
        return self.id



class P1_Models(object):
    cultures = None
    figures = None
    stories = None

    @staticmethod
    def init_cultures():
        P1_Models.cultures = dict()

        c1 = Culture(id=1,
            name="Greeks", 
            region="Greece", 
            history="""The Greeks are an ethnic group native to Greece, Cyprus, Anatolia and other regions. They also form a significant diaspora, with Greek communities established
around the world. Greek colonies and communities have been historically established in most corners of the Mediterranean, but Greeks have always been centered around the Aegean Sea, 
where the Greek language has been spoken since the Bronze Age. Until the early 20th century, Greeks were uniformly distributed between the Greek peninsula, the western coast of 
Asia Minor, Pontus, Egypt, Cyprus and Constantinople; many of these regions coincided to a large extent with the borders of the Byzantine Empire of the late 11th century and the 
Eastern Mediterranean areas of the ancient Greek colonization. Greeks have greatly influenced and contributed to culture, arts, exploration, literature, philosophy, politics, 
architecture, music, mathematics, science, technology, cuisine, and sports, both historically and contemporary.""",
            language="Greek")
        c1_m0 = Media(id=0, culture=c1, name="img_Greeks", kind="img", link="http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg")
        c1_m1 = Media(id=1, culture=c1, name="youtube:Greeks", kind="vid", link="http://www.youtube.com/watch?v=WptSXfvY-vs")
        c1_m2 = Media(id=2, culture=c1, name="wikipedia:Greeks", kind="link", link="http://en.wikipedia.org/wiki/Greeks")
        c1.media = [c1_m0, c1_m1, c1_m2]
        P1_Models.cultures[c1.getID()] = c1

def p1_cultures():
    if not P1_Models.cultures:
        P1_Models.init_cultures()
    return P1_Models.cultures.values()

def p1_culture(id):
    if not P1_Models.cultures:
        P1_Models.init_cultures()
    return P1_Models.cultures[int(id)]

def p1_figure(id):
    pass

def p1_story(id):
    pass
