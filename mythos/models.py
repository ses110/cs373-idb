from django.db import models

class Relations(models.Model):
   pass 

class Hero(Models.Model):
    '''
    Hero Model

    @type hero_id: models.CharField(200, primary_key = True)
    @cvar hero_id: A hero's primary key to uniquely the instance
    
    '''
    hero_id = models.CharField(max_length=200, primary_key=True)
    name    = models.CharField(max_length=200)
    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: Hero
        @param self: Current Hero instance

        @rtype: string
        @return: The id associated with this Hero instance  
        """
        return self.hero_id

class Event(Models.Model):
    event_id = models.CharField(max_length=200, primary_key=True)
    name     = models.CharField(max_length=200)
    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: Event
        @param self: Current Event instance

        @rtype: string
        @return: The id associated with this Event instance
        """
        return self.event_id

class God(Models.Model):
    god_id = models.CharField(max_length=200, primary_key=True)
    name   = models.CharField(max_length=200)

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: God
        @param self: Current God instance

        @rtype: string
        @return: The id associated with this God instance
        """
        return self.god_id
