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
    culture_items = None
    figure_items = None
    story_items = None

    @staticmethod
    def init_culture_items():
        P1_Models.culture_items = list()
        P1_Models.culture_items.append(Culture(id=1, name="Greek"))
        P1_Models.culture_items.append(Culture(id=2, name="Roman"))
        P1_Models.culture_items.append(Culture(id=3, name="Norse"))

    @staticmethod
    def init_cultures():
        P1_Models.cultures = dict()

        P1_Models.cultures[1] = {
            'title':"Greek",
            'region':"Greece",
            'language':"Greek",
            'history':"""The Greeks are an ethnic group native to Greece, Cyprus, Anatolia and other regions. They also form a significant diaspora, with Greek communities established
around the world. Greek colonies and communities have been historically established in most corners of the Mediterranean, but Greeks have always been centered around the Aegean Sea, 
where the Greek language has been spoken since the Bronze Age. The Greeks were uniformly distributed between the Greek peninsula, the western coast of 
Asia Minor, Pontus, Egypt, Cyprus and Constantinople; many of these regions coincided to a large extent with the borders of the Byzantine Empire of the late 11th century and the 
Eastern Mediterranean areas of the ancient Greek colonization. Greeks have greatly influenced and contributed to culture, arts, exploration, literature, philosophy, politics, 
architecture, music, mathematics, science, technology, cuisine, and sports, both historically and contemporary.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/a/ad/Parthenon_from_west.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/1/19/William_Faden._Composite_Mediterranean._1785.I.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/8/87/ArchaicGr.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/7/7c/Beginning_Odyssey.svg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/9/96/EarlyAthenianCoin.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/4/4a/Law_Code_Gortyn_Louvre_Ma703.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/a/a4/Socrates_Louvre.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/2/22/Greek-Persian_duel.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg")],
            'videos':[Media(link="http://www.youtube.com/embed/WptSXfvY-vs"),
                      Media(link="http://www.youtube.com/embed/vHMu2gVzspA")],
            'related_figures':[Figure(id=1, name="Atlas"), Figure(id=2, name="Athena")],
            'related_stories':[],
            'related_cultures':[Culture(id=2, name="Roman")],
            'external_links':[Media(name="Wikipedia: Greeks", link="http://en.wikipedia.org/wiki/Greeks"),
                              Media(name="Wikipedia: Ancient Greece", link="http://en.wikipedia.org/wiki/Ancient_Greece"),
                              Media(name="ancientgreece.com", link="http://www.ancientgreece.com/s/Main_Page/"),
                              Media(name="BBC: Ancient Greeks", link="http://www.bbc.co.uk/schools/primaryhistory/ancient_greeks/"),
                              Media(name="History Channel: Ancient Greeks", link="http://www.history.com/topics/ancient-history/ancient-greece")]
        }

        P1_Models.cultures[2] = {
            'title':"Roman",
            'region':"Mediterranean",
            'language':"Latin",
            'history':"""Ancient Rome was an Italic civilization that began on the Italian Peninsula as early as the 8th century BC. Located along the Mediterranean Sea and centered 
on the city of Rome, it expanded to become one of the largest empires in the ancient world[1] with an estimated 50 to 90 million inhabitants (roughly 20% of the world's population) 
and covering 6.5 million square kilometers (2.5 million sq mi) during its height between the first and second centuries AD. In its approximately 12 centuries of existence, Roman civilization 
shifted from a monarchy to a classical republic to an increasingly autocratic empire. Through conquest and assimilation, it came to dominate Southern Europe, Western Europe, Asia Minor, North Africa, 
parts of Northern Europe, and parts of Eastern Europe. Rome was preponderant throughout the Mediterranean region and was one of the most powerful entities of the ancient world. It is often grouped into 
"Classical Antiquity" together with ancient Greece, and their similar cultures and societies are known as the Greco-Roman world. The Romans are still remembered today, including names such as Julius Caesar, 
Cicero, and Augustus. Ancient Roman society contributed greatly to government, law, politics, engineering, art, literature, architecture, technology, warfare, religion, language, society and more in the 
Western world. A civilization highly developed for its time, Rome professionalized and greatly expanded its military and created a system of government called res publica, the inspiration for modern 
republics such as the United States and France. It achieved impressive technological and architectural feats, such as the construction of an extensive system of aqueducts and roads, as well as large monuments, palaces, and public facilities.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/e/ea/Roman_Republic_Empire_map.gif"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/8/8e/Capitoline_Brutus_Musei_Capitolini_MC1183.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/b/b5/Italy_400bC_en.svg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/1/15/Giulio-cesare-enhanced_1-800x1450.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/9/95/Castro_Battle_of_Actium.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/e/eb/Statue-Augustus.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/e/e6/Septimius_Severus_Glyptothek_Munich_357.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/2/2d/Invasions_of_the_Roman_Empire_1.png")],
            'videos':[Media(link="http://www.youtube.com/embed/g-MFgjO88KY"),
                      Media(link="http://www.youtube.com/embed/uR-dCYZ8LIo")],
            'related_figures':[Figure(id=1, name="Atlas"), Figure(id=2, name="Athena")],
            'related_stories':[],
            'related_cultures':[Culture(id=1, name="Greeks"), Culture(id=3, name="Norse")],
            'external_links':[Media(name="Wikipedia: Roman Mythology", link="http://en.wikipedia.org/wiki/Roman_mythology"),
                              Media(name="Wikipedia: Ancient Rome", link="http://en.wikipedia.org/wiki/Ancient_Rome"),
                              Media(name="OpenCourseWare: History of Ancient Rome", link="http://ocw.nd.edu/classics/history-of-ancient-rome"),
                              Media(name="Livius.org", link="http://www.livius.org/rome.html")]
        }

        P1_Models.cultures[3] = {
            'title':"Nordic",
            'region':"Scandinavia",
            'language':"Old Norse",
            'history':"""Vikings (from Old Norse víkingr) were the people of the Norse culture, during the Viking Age. 
They were a seafaring people of north Germanic descent, based in Scandinavia, who raided, traded, explored, and settled in wide areas of Europe, Asia, and the North Atlantic islands, 
from the late 8th to the mid-11th centuries. The Vikings employed wooden longships with wide, shallow-draft hulls, allowing navigation in rough seas or in shallow river waters. 
The ships could be landed on beaches, and their light weight enabled them to be hauled over portages. These versatile ships allowed the Vikings to settle and travel as far east 
as Constantinople and the Volga River in Russia, as far west as Iceland, Greenland, and Newfoundland, and as far south as Nekor. This period of Viking expansion, known as the Viking Age,
constitutes an important element of the medieval history of Scandinavia, Great Britain, Ireland, Russia, and the rest of Europe.
Popular conceptions of the Vikings often differ from the complex picture that emerges from archaeology and written sources. A romanticised picture of Vikings as noble savages began to take 
root in the 18th century, and this developed and became widely propagated during the 19th-century Viking revival.[2] The received views of the Vikings as violent brutes or intrepid adventurers 
owe much to the modern Viking myth that had taken shape by the early 20th century. Current popular representations are typically highly clichéd, presenting the Vikings as familiar caricatures.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/c/cb/Wikinger.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/5/53/Gokstadskipet1.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/5/51/The_Wolves_Pursuing_Sol_and_Mani.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/5/51/Ardre_Odin_Sleipnir.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/e/e2/Walhall_by_Emil_Doepler.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/6/60/Hundingsbane.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/b/b3/Manuscript_Odinn.jpg")],
            'videos':[Media(link="http://www.youtube.com/embed/_qYvtDaVEYM"),
                      Media(link="http://www.youtube.com/embed/IsX7i5BCHso")],
            'related_figures':[Figure(id=3, name="Loki")],
            'related_stories':[],
            'related_cultures':[Culture(id=2, name="Roman")],
            'external_links':[Media(name="Wikipedia: Nordic Mythology", link="http://en.wikipedia.org/wiki/Nordic_mythology"),
                              Media(name="Wikipedia: Norsemen", link="http://en.wikipedia.org/wiki/Norsemen"),
                              Media(name="Hurstwic", link="http://www.hurstwic.org/history/text/history.htm")]
        }

    @staticmethod
    def init_figure_items():
        P1_Models.figure_items = list()
        P1_Models.figure_items.append(Figure(id=1, name="Atlas"))
        P1_Models.figure_items.append(Figure(id=2, name="Athena"))
        P1_Models.figure_items.append(Figure(id=3, name="Loki"))

    @staticmethod
    def init_figures():
        P1_Models.figures = dict()

        P1_Models.figures[1] = {
            'title':"Atlas",
            'kind':"Titan",
            'biography':"""In Greek mythology, Atlas was the primordial Titan who held up the celestial sphere. 
He is also the titan of astronomy and navigation. Although associated with various places, he became commonly identified with the Atlas Mountains in northwest Africa (Modern-day Morocco and Algeria). 
Atlas and his brother Menoetius sided with the Titans in their war against the Olympians, the Titanomachy. When the Titans were defeated, many of them (including Menoetius) were confined to Tartarus, 
but Zeus condemned Atlas to stand at the western edge of Gaia (the Earth) and hold up Uranus on his shoulders, to prevent the two from resuming their primordial embrace. Thus, he was Atlas Telamon, 
"enduring Atlas," and became a doublet of Coeus, the embodiment of the celestial axis around which the heavens revolve.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/en/7/75/Atlas_New_York.JPG"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/5/52/Atlas_Santiago_Toural_GFDL.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/0/0d/Atlas_sculpture_on_collins_street_melbourne.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/6/62/GandharanAtlas.JPG")],
            'videos':[Media(link="http://www.youtube.com/embed/5hhPRUpF6YY")],
            'related_figures':[Figure(id=1, name="Atlas")],
            'related_stories':[Story(id=2, name="The Punishment of Atlas")],
            'related_cultures':[Culture(id=1, name="Greek"), Culture(id=2, name="Roman")],
            'external_links':[Media(name="Wikipedia: Atlas", link="http://en.wikipedia.org/wiki/Atlas_(mythology)"),
                              Media(name="Tufts: A Dictionary of Greek and Roman biography and mythology", link="http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0104%3Aalphabetic+letter%3DA%3Aentry+group%3D53%3Aentry%3Datlas-bio-1")]
        }

        P1_Models.figures[2] = {
            'title':"Athena",
            'kind':"Olympian",
            'biography':"""In Greek religion and mythology, Athena or Athene, also referred to as Pallas Athena/Athene, 
is the goddess of wisdom, courage, inspiration, civilization, law and justice, just warfare, mathematics, strength, strategy, the arts, crafts, and skill. 
Minerva is the Roman goddess identified with Athena. Athena is also a shrewd companion of heroes and is the goddess of heroic endeavour. She is the virgin patroness of Athens. 
The Athenians founded the Parthenon on the Acropolis of her namesake city, Athens (Athena Parthenos), in her honour. Athena's veneration as the patron of Athens seems to have existed 
from the earliest times, and was so persistent that archaic myths about her were recast to adapt to cultural changes. In her role as a protector of the city (polis), many people throughout the Greek world worshiped Athena as Athena Polias. 
The city of Athens and the goddess Athena essentially bear the same name (Athena the Goddess, Athenai the city) while it is not known which of the two words is derived from the other.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/2/22/Mattei_Athena_Louvre_Ma530_n2.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/d/db/Athena_Parthenos_Altemps_Inv8622.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/2/2a/Gandharan_Athena.jpg")],
            'videos':[Media(link="http://www.youtube.com/embed/AOL0oAAO9LA")],
            'related_figures':[Figure(id=1, name="Atlas")],
            'related_stories':[Story(id=1, name="Birth of Athena")],
            'related_cultures':[Culture(id=1, name="Greek"), Culture(id=2, name="Roman")],
            'external_links':[Media(name="Wikipedia: Athena", link="http://en.wikipedia.org/wiki/Athena"),
                              Media(name="Cult of Athena", link="http://www.theoi.com/Cult/AthenaCult.html")]
        }

        P1_Models.figures[3] = {
            'title':"Loki",
            'kind':"God",
            'biography':"""In Norse mythology, Loki, Loptr, or Hveðrungr is a god. Loki is the son of Fárbauti and Laufey, and the brother of Helblindi and Byleistr. 
By the jotunn Angrboða, Loki is the father of Hel, the wolf Fenrir, and the world serpent Jormungandr. By his wife Sigyn, Loki is the father of Narfi and/or Nari. 
By the stallion Svaoilfari, Loki is the mother—giving birth in the form of a mare—to the eight-legged horse Sleipnir. In addition, Loki is referred to as the father of Vali in the Prose Edda.
Loki's relation with the gods varies by source. Loki sometimes assists the gods and sometimes causes problems for them. Loki is a shape shifter and in separate incidents he appears in the form of a salmon, 
mare, seal, a fly, and possibly an elderly woman. Loki's positive relations with the gods end with his role in engineering the death of the god Baldr. Loki is eventually bound by the gods with the entrails of one of his sons.
In both the Poetic Edda and the Prose Edda, the goddess Skaði is responsible for placing a serpent above him while he is bound. The serpent drips venom from above him that Sigyn collects into a bowl; however, 
she must empty the bowl when it is full, and the venom that drips in the meantime causes Loki to writhe in pain, thereby causing earthquakes. With the onset of Ragnarök, Loki is foretold to slip free from his bonds and to fight against the gods among the forces of the jotnar, 
at which time he will encounter the god Heimdallr and the two will slay each other. Loki is attested in the Poetic Edda, compiled in the 13th century from earlier traditional sources; the Prose Edda and Heimskringla, written in the 13th century by Snorri Sturluson; 
the Norwegian Rune Poems, in the poetry of skalds, and in Scandinavian folklore. Loki may be depicted on the Snaptun Stone, the Kirkby Stephen Stone, and the Gosforth Cross. Loki's origins and role in Norse mythology, which some scholars have described as that of a trickster god, 
have been much debated by scholars.""",
            'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/4/40/Processed_SAM_loki.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/a/ac/Loki_taunts_Bragi.jpg"),
                      Media(link="http://upload.wikimedia.org/wikipedia/commons/c/cb/Louis_Huard_-_The_Punishment_of_Loki.jpg")],
            'videos':[Media(link="http://www.youtube.com/embed/o43-oAL2ogY")],
            'related_figures':[],
            'related_stories':[],
            'related_cultures':[Culture(id=3, name="Norse")],
            'external_links':[Media(name="Wikipedia: Loki", link="http://en.wikipedia.org/wiki/Loki"),
                              Media(name="Pantheon.Org", link="http://www.pantheon.org/articles/l/loki.html")]
        }

    @staticmethod
    def init_story_items():
      P1_Models.story_items = list()
      P1_Models.story_items.append(Story(id=1, name="Birth of Athena"))
      P1_Models.story_items.append(Story(id=2, name="The Punishment of Atlas"))
      P1_Models.story_items.append(Story(id=3, name="Reginsmál"))

    @staticmethod
    def init_stories():
      P1_Models.stories = dict()

      P1_Models.stories[1] = {
        'title':"The Birth of Athena",
        'summary':"""The story of Athena's birth comes in several versions. In the one most commonly cited, Zeus lay with Metis, the goddess of crafty thought and wisdom, 
but he immediately feared the consequences. It had been prophesied that Metis would bear children more powerful than the sire, even Zeus himself. In order to forestall these dire 
consequences, after lying with Metis, Zeus "put her away inside his own belly;" he "swallowed her down all of a sudden." He was too late: Metis had already conceived.
Eventually Zeus experienced an enormous headache; Prometheus, Hephaestus, Hermes, Ares, or Palaemon (depending on the sources examined) cleaved Zeus's head with the double-headed 
Minoan axe, the labrys. Athena leaped from Zeus's head, fully grown and armed, with a shout— "and pealed to the broad sky her clarion cry of war. And Ouranos trembled to hear, 
and Mother Gaia..." (Pindar, Seventh Olympian Ode).\nThe major competing tradition regarding Athena's parentage involves some of her more mysterious epithets: Pallas, as in the 
ancient-Greek Παλλάς Ἀθήνη (also Pallantias) and Tritogeneia (also Trito, Tritonis, Tritoneia, Tritogenes). A distant archaic separate entity named Pallas is invoked as Athena's father, 
sister, foster sister, companion, or opponent in battle. Pallas is often a nymph, a daughter of Triton (a sea god), and a childhood friend of Athena.
In every case, Athena kills Pallas, accidentally, and thereby gains the name for herself. In one telling, they practice the arts of war together until 
one day they have a falling out. As Pallas is about to strike Athena, Zeus intervenes. With Pallas stunned by a blow from Zeus, Athena takes advantage and 
kills her. Distraught over what she has done, Athena takes the name Pallas for herself.
When Pallas is Athena's father the events, including her birth, are located near a body of water named Triton or Tritonis. When Pallas is Athena's sister or 
foster-sister, Athena's father or foster-father is Triton, the son and herald of Poseidon. But Athena may be called the daughter of Poseidon and a nymph named Tritonis,
without involving Pallas. Likewise, Pallas may be Athena's father or opponent, without involving Triton.""",
        'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/4/42/Amphora_birth_Athena_Louvre_F32.jpg")],
        'videos':[],
        'related_figures':[Figure(id=2, name="Athena")],
        'related_stories':[],
        'related_cultures':[Culture(id=1, name="Greek"), Culture(id=2, name="Roman")],
        'external_links':[Media(name="Wikipedia: Athena", link="http://en.wikipedia.org/wiki/Athena"),
                          Media(name="Birth of Athena", link="http://www.greekmythology.com/Myths/The_Myths/Birth_of_Athena/birth_of_athena.html")]
    }

      P1_Models.stories[2] = {
          'title':"The Punishment of Atlas",
          'summary':"""Atlas and his brother Menoetius sided with the Titans in their war against the Olympians, the Titanomachy. When the Titans were defeated, 
many of them (including Menoetius) were confined to Tartarus, but Zeus condemned Atlas to stand at the western edge of Gaia (the Earth) and hold up Uranus on his shoulders, 
to prevent the two from resuming their primordial embrace. Thus, he was Atlas Telamon, "enduring Atlas," and became a doublet of Coeus, the embodiment of the celestial axis 
around which the heavens revolve.""",
          'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/8/8c/MAN_Atlante_fronte_1040572.JPG")],
          'videos':[],
          'related_figures':[Figure(id=1, name="Atlas"), Figure(id=2, name="Athena")],
          'related_stories':[],
          'related_cultures':[Culture(id=1, name="Greek"), Culture(id=2, name="Roman")],
          'external_links':[Media(name="Wikipedia: Atlas", link="http://en.wikipedia.org/wiki/Atlas_(mythology)"),
                            Media(name="Ancient History", link="http://ancienthistory.about.com/od/atlastitanmyth/f/081409WorldonShouders.htm")]
      }

      P1_Models.stories[3] = {
          'title':"Reginsmál",
          'summary':"""Loki appears in both prose and the first six stanzas of the poem Reginsmál. 
The prose introduction to Reginsmál details that, while the hero Sigurd was being fostered by Regin, son of Hreidmar, 
Regin tells him that once the gods Odin, Hœnir, and Loki went to Andvara-falls, which contained many fish. Regin, a dwarf, 
 two brothers; Andvari, who gained food by spending time in the Andvara-falls in the form of a pike, and Ótr, who would often go to the Andvara-falls in the form of an otter.
While the three gods are at the falls, Ótr (in the form of an otter) catches a salmon and eats it on a river bank, his eyes shut, when Loki hits and kills him with a stone. 
The gods think that this is great, and flay the skin from the otter to make a bag. That night, the three gods stay with Hreidmar (the father of Regin, Andvari, 
  and the now-dead Ótr) and show him their catches, including the skin of the otter. Upon seeing the skin, Regin and Hreidmar "seized them and made them ransom their lives" in exchange for filling the 
otterskin bag the gods had made with gold and covering the exterior of the bag with red gold.
Loki is sent to retrieve the gold, and Loki goes to the goddess Rán, borrows her net, and then goes back to the Andvara-falls. 
At the falls, Loki spreads his net before Andvari (who is in the form of a pike), which Andvari jumps into. The stanzas of the poem then begin: 
Loki mocks Andvari, and tells him that he can save his head by telling Loki where his gold is. Andvari gives some background information about himself, 
including that he was cursed by a "norn of misfortune" in his "early days". Loki responds by asking Andvari "what requital" does mankind get if 
"they wound each other with words". Andvari responds that lying men receive a "terrible requital": having to wade in the river Vadgelmir, and that their suffering will be long.
Loki looks over the gold that Andvari possesses, and after Andvari hands over all of his gold, Andvari holds on to but a single ring; the ring Andvarinaut, which Loki also takes. 
Andvari, now in the form of a dwarf, goes into a rock, and tells Loki that the gold will result in the death of two brothers, will cause strife between eight princes, and will be useless to everyone.
Loki returns, and the three gods give Hreidmar the money from the gold hoard and flatten out the otter skin, stretch out its legs, and heap gold atop it, covering it. Hreidmar looks it over, and notices a single hair that has not been covered. 
Hreidmar demands that it be covered as well. Odin puts forth the ring Andvarinaut, covering the single hair.
Loki states that they have now handed over the gold, and that gold is cursed as Andvari is, and that it will be the death of Hreidmar and Regin both. 
Hreidmar responds that if he had known this before, he would have taken their lives, yet that he believes those are not yet born whom the curse is intended for, and that he doesn't believe him. Further, with the hoard, he will have red gold for the rest of his life. 
Hreidmar tells them to leave, and the poem continues without further mention of Loki.""",
          'images':[Media(link="http://upload.wikimedia.org/wikipedia/commons/8/8c/MAN_Atlante_fronte_1040572.JPG")],
          'videos':[],
          'related_figures':[Figure(id=3, name="Loki")],
          'related_stories':[],
          'related_cultures':[Culture(id=1, name="Norse")],
          'external_links':[Media(name="Wikipedia: Loki", link="http://en.wikipedia.org/wiki/Loki"),
                            Media(name="Wikipedia: Reginsmál", link="http://en.wikipedia.org/wiki/Reginsm%C3%A1l")]
      }


def p1_cultures():
    if not P1_Models.culture_items:
        P1_Models.init_culture_items()
    return P1_Models.culture_items

def p1_culture(id):
    if not P1_Models.cultures:
        P1_Models.init_cultures()
    return P1_Models.cultures[int(id)]

def p1_figures():
    if not P1_Models.figure_items:
        P1_Models.init_figure_items()
    return P1_Models.figure_items

def p1_figure(id):
    if not P1_Models.figures:
        P1_Models.init_figures()
    return P1_Models.figures[int(id)]

def p1_stories():
    if not P1_Models.story_items:
        P1_Models.init_story_items()
    return P1_Models.story_items

def p1_story(id):
    if not P1_Models.stories:
        P1_Models.init_stories()
    return P1_Models.stories[int(id)]
