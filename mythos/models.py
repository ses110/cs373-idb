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
    notable_stories     = models.ForeignKey('Story')

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
    culture_items = None

    @staticmethod
    def init_culture_items():
        P1_Models.culture_items = list()
        P1_Models.culture_items.append(Culture(id=1, name="Greeks"))
        P1_Models.culture_items.append(Culture(id=2, name="Nordic"))
        P1_Models.culture_items.append(Culture(id=3, name="Roman"))

    @staticmethod
    def init_cultures():
        P1_Models.cultures = dict()

        P1_Models.cultures[1] = {
            'title':"Greeks",
            'region':"Greece",
            'language':"Greek",
            'history':"""The Greeks are an ethnic group native to Greece, Cyprus, Anatolia and other regions. They also form a significant diaspora, with Greek communities established
around the world. Greek colonies and communities have been historically established in most corners of the Mediterranean, but Greeks have always been centered around the Aegean Sea, 
where the Greek language has been spoken since the Bronze Age. Until the early 20th century, Greeks were uniformly distributed between the Greek peninsula, the western coast of 
Asia Minor, Pontus, Egypt, Cyprus and Constantinople; many of these regions coincided to a large extent with the borders of the Byzantine Empire of the late 11th century and the 
Eastern Mediterranean areas of the ancient Greek colonization. Greeks have greatly influenced and contributed to culture, arts, exploration, literature, philosophy, politics, 
architecture, music, mathematics, science, technology, cuisine, and sports, both historically and contemporary.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/6/61/Leonidas_I_of_Sparta.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/6/66/Pericles_Townley_BM_549.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/7/7d/Head_Platon_Glyptothek_Munich_548.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/e/e7/Domenico-Fetti_Archimedes_1620.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/a/ae/Aristotle_Altemps_Inv8575.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/a/a4/Socrates_Louvre.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/0/01/El_greco.JPG"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/7/7d/Head_Platon_Glyptothek_Munich_548.jpg")],
            'videos':[Media(link="http://www.youtube.com/embed/WptSXfvY-vs"),
                      Media(link="http://www.youtube.com/embed/vHMu2gVzspA")],
            'related_figures':[Figure(id=1, name="Zeus"), Figure(id=2, name="Hercules"), Figure(id=3, name="Athena")],
            'related_stories':[Story(id=1, name="lorem ipsum"), Story(id=2, name="lorem ipsum"), Story(id=3, name="lorem ipsum")],
            'related_cultures':[Culture(id=1, name="Roman")],
            'external_links':[Media(name="Wikipedia: Greeks", link="http://en.wikipedia.org/wiki/Greeks"),
                              Media(name="ancientgreece.com", link="http://www.ancientgreece.com/s/Main_Page/"),
                              Media(name="BBC: Ancient Greeks", link="http://www.bbc.co.uk/schools/primaryhistory/ancient_greeks/"),
                              Media(name="History Channel: Ancient Greeks", link="http://www.history.com/topics/ancient-history/ancient-greece")]
        }

def p1_cultures():
    if not P1_Models.culture_items:
        P1_Models.init_culture_items()
    return P1_Models.culture_items

def p1_culture(id):
    if not P1_Models.cultures:
        P1_Models.init_cultures()
    return P1_Models.cultures[int(id)]

def p1_figure(id):
    pass

def p1_story(id):
    pass
