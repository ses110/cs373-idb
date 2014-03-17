from django.db import models

class Relations(models.Model):
   pass 

class Figure(Models.Model):
    '''
    Figure Model

    @type figure_id: models.CharField(200, primary_key = True)
    @cvar figure_id: A figure's primary key to uniquely the instance
    
    '''
    figure_id = models.CharField(max_length=200, primary_key=True)
    name      = models.CharField(max_length=200)
    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: Figure
        @param self: Current Figure instance

        @rtype: string
        @return: The id associated with this Figure instance  
        """
        return self.figure_id

class Event(Models.Model):
    event_id = models.CharField(max_length=200, primary_key=True)
    name      = models.CharField(max_length=200)
    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: Event
        @param self: Current Event instance

        @rtype: string
        @return: The id associated with this Event instance
        """
        return self.event_id

class Faction(Models.Model):
    faction_id = models.CharField(max_length=200, primary_key=True)
    name      = models.CharField(max_length=200)

    def getID(self):
        """
        Fetch primary key ID from current instance

        @type self: Faction
        @param self: Current Faction instance

        @rtype: string
        @return: The id associated with this Faction instance
        """
        return self.faction_id
