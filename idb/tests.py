from django.test import TestCase
from django.http import HttpResponse
from urllib.request import urlopen, Request
from json import dumps, loads


# Create your tests here.



class APItests(TestCase) :
	url = "http://127.0.0.1:8000"
	#Figures

	def test_get_all_figures(self) :


		request = Request(self.url+"/api/figures/?format=json")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		expected_response = [{'kind': 'Olympian', 'name': 'Athena', 'id': 1, 'related_figures': ['/api/figures/2/'], 'related_stories': ['/api/stories/1/'], 'related_cultures': ['/api/cultures/1/', '/api/cultures/8/'], 'biography': 'In Greek religion and mythology, Athena or Athene (/əˈθiːnə/ or /əˈθiːniː/; Attic: Ἀθηνᾶ, Athēnā or Ἀθηναία, Athēnaia; Epic: Ἀθηναίη, Athēnaiē; Ionic: Ἀθήνη, Athēnē; Doric: Ἀθάνα, Athānā), also referred to as Pallas Athena/Athene (/ˈpæləs/; Παλλὰς Ἀθηνᾶ; Παλλὰς Ἀθήνη), is the goddess of wisdom, courage, inspiration, civilization, law and justice, just warfare, mathematics, strength, strategy, the arts, crafts, and skill. Minerva is the Roman goddess identified with Athena.\nAthena is portrayed as a shrewd companion of heroes and is the patron goddess of heroic endeavour. She is the virgin patroness of Athens. The Athenians founded the Parthenon on the Acropolis of her namesake city, Athens (Athena Parthenos), in her honour.\nAthena\'s veneration as the patron of Athens seems to have existed from the earliest times, and was so persistent that archaic myths about her were recast to adapt to cultural changes. In her role as a protector of the city (polis), many people throughout the Greek world worshiped Athena as Athena Polias (Ἀθηνᾶ Πολιάς "Athena of the city"). The city of Athens and the goddess Athena essentially bear the same name (Athena the Goddess, Athenai the city) while it is not known which of the two words is derived from the other.', 'resource_uri': '/api/figures/1/'}, {'kind': 'God', 'name': 'Odin', 'id': 3, 'related_figures': ['/api/figures/4/'], 'related_stories': ['/api/stories/3/'], 'related_cultures': ['/api/cultures/4/'], 'biography': 'Odin (/ˈoʊdɨn/; from Old Norse Óðinn, "The Furious One") is a major god in most if not all branches of Germanic mythology especially in the Norse mythology branch of Germanic mythology, the Allfather of the gods, and the ruler of Asgard. Homologous with the Old English "Wōden", the Old Saxon "Wôdan" and the Old High German "Wôtan", the name is descended from Proto-Germanic "*Wōdanaz" or "*Wōđanaz". "Odin" is generally accepted as the modern English form of the name, although, in some cases, older forms may be used or preferred. His name is related to ōðr, meaning "fury, excitation", besides "mind" or "poetry". His role, like that of many of the Norse gods, is complex. Odin is a principal member of the Æsir (the major group of the Norse pantheon) and is associated with war, battle, victory and death, but also wisdom, Shamanism, magic, poetry, prophecy, and the hunt. Odin has many sons, the most famous of whom is the thunder god Thor.', 'resource_uri': '/api/figures/3/'}, {'kind': 'Hero', 'name': 'Háma', 'id': 4, 'related_figures': ['/api/figures/3/'], 'related_stories': ['/api/stories/3/'], 'related_cultures': ['/api/cultures/4/'], 'biography': 'Háma (Old English: Hāma), Heimir (Old Norse), or Heime (German) was a legendary Germanic hero who often appears together with his friend Wudga. He appears in the Anglo-Saxon poems Beowulf and Widsith, in the Scandinavian Þiðrekssaga and in German epics such as Alpharts Tod.', 'resource_uri': '/api/figures/4/'}, {'kind': 'Goddess', 'name': 'Vishnu', 'id': 8, 'related_figures': ['/api/figures/7/'], 'related_stories': ['/api/stories/5/'], 'related_cultures': ['/api/cultures/5/'], 'biography': 'Vishnu is the Supreme God of Vaishnavism, one of the three main sects of Hinduism. Vishnu is also known as Narayana and Hari. Laksmi is the wife of Vishnu. The Vishnu Sahasranama declares Vishnu as Paramatman (supreme soul) and Parameshwara (supreme God). It describes Vishnu as the all-pervading essence of all beings, the master of—and beyond—the past, present and future, the creator and destroyer of all existences, one who supports, preserves, sustains and governs the universe and originates and develops all elements within. Though he is usually depicted as blue, some other depictions of Vishnu exist as green-bodied, and in the Kurma Purana he is described as colorless and with red eyes.\nIn Hindu sacred texts, Vishnu is usually described as having the divine blue color of water-filled clouds and as having four arms. He is depicted as holding a padma (lotus flower) in the lower left hand, a unique type of mace used in warfare known as a Kaumodaki gada in the lower right hand, a Panchajanya shankha (conch) in the upper left hand and a discus weapon Sudarshana Chakra in the upper right hand. Vishnu is also described in the Bhagavad Gita as having a \'Universal Form\' (Vishvaroopa or Viraata Purusha) Vishvarupa which is beyond the ordinary limits of human perception or imagination. It is said that he owns pancha ayudham (5 weapons): Sudarshanam, Panchajanyam, Komodaki, Nandakam, Shaarngam.[by whom?]\nVishnu\'s eternal and supreme abode beyond the material universe is called Vaikuntha, which is also known as Paramdhama, the realm of eternal bliss and happiness and the final or highest place for liberated souls who have attained Moksha. Vaikuntha is situated beyond the material universe and hence, cannot be perceived or measured by material science or logic. Vishnu\'s other abode within the material universe is Ksheera Sagara (the ocean of milk), where he reclines and rests on Ananta Shesha, (the king of the serpent deities, commonly shown with thousand heads). In almost all Hindu denominations, Vishnu is either worshipped directly or in the form of his ten avatars, the most famous of whom are Rama and Krishna. The Puranabharati, an ancient text, describes these as the dashavatara, or the ten avatars of Vishnu. Among the ten described, nine have occurred in the past and one will take place in the future as Lord Kalki, at the end of Kali Yuga, (the fourth and final stage in the cycle of yugas that the world goes through). These incarnations take place in all Yugas in cosmic scales; the avatars and their stories show that gods are indeed unimaginable, unthinkable and inconceivable. The Bhagavad Gita mentions their purpose as being to rejuvenate Dharma, to vanquish those negative forces of evil that threaten dharma, and also to display His divine nature in front of all souls.\nThe Trimurti (three forms) is a concept in Hinduism "in which the cosmic functions of creation, maintenance, and destruction are personified by the forms of Brahma the creator, Vishnu the maintainer or preserver, and Shiva the destroyer or transformer." These three deities have also been called "the Hindu triad" or the "Great Trinity", all having the same meaning of three in One. They are the different forms or manifestation of One person the Supreme Being or Narayana/Svayam Bhagavan.\nVishnu is also venerated as Mukunda, which means God who is the giver of mukti or moksha (liberation from the cycle of rebirths) to his devotees or the worthy ones who deserve salvation from the material world.\n\n', 'resource_uri': '/api/figures/8/'}, {'kind': 'Olympian', 'name': 'Zeus', 'id': 2, 'related_figures': ['/api/figures/1/', '/api/figures/10/'], 'related_stories': ['/api/stories/1/', '/api/stories/2/'], 'related_cultures': ['/api/cultures/1/', '/api/cultures/8/'], 'biography': 'Zeus (Ancient Greek: Ζεύς, Zeús; Modern Greek: Δίας, Días; English pronunciation /zjuːs/) is the "Father of Gods and men" (πατὴρ ἀνδρῶν τε θεῶν τε, patḕr andrōn te theōn te) who rules the Olympians of Mount Olympus as a father rules the family according to the ancient Greek religion. He is the god of sky and thunder in Greek mythology. Zeus is etymologically cognate with and, under Hellenic influence, became particularly closely identified with Roman Jupiter.\nZeus is the child of Cronus and Rhea, and the youngest of his siblings. In most traditions he is married to Hera, although, at the oracle of Dodona, his consort is Dione: according to the Iliad, he is the father of Aphrodite by Dione. He is known for his erotic escapades. These resulted in many godly and heroic offspring, including Athena, Apollo and Artemis, Hermes, Persephone (by Demeter), Dionysus, Perseus, Heracles, Helen of Troy, Minos, and the Muses (by Mnemosyne); by Hera, he is usually said to have fathered Ares, Hebe and Hephaestus.\nAs Walter Burkert points out in his book, Greek Religion, "Even the gods who are not his natural children address him as Father, and all the gods rise in his presence." For the Greeks, he was the King of the Gods, who oversaw the universe. As Pausanias observed, "That Zeus is king in heaven is a saying common to all men". In Hesiod\'s Theogony Zeus assigns the various gods their roles. In the Homeric Hymns he is referred to as the chieftain of the gods.\nHis symbols are the thunderbolt, eagle, bull, and oak. In addition to his Indo-European inheritance, the classical "cloud-gatherer" (Greek: Νεφεληγερέτα, Nephelēgereta) also derives certain iconographic traits from the cultures of the Ancient Near East, such as the scepter. Zeus is frequently depicted by Greek artists in one of two poses: standing, striding forward, with a thunderbolt leveled in his raised right hand, or seated in majesty.', 'resource_uri': '/api/figures/2/'}, {'kind': 'God', 'name': 'The Dagda', 'id': 5, 'related_figures': ['/api/figures/6/'], 'related_stories': ['/api/stories/4/'], 'related_cultures': ['/api/cultures/2/'], 'biography': 'The Dagda (Proto-Celtic: *Dagodeiwos, Old Irish: Dag Dia, Modern Irish: Daghdha) is an important god of Irish mythology. The Dagda is a father-figure (he is also known as Eochaid(h) Ollathair, or "All-father") and a protector of the tribe. In some texts his father is Elatha, in others his mother is Ethniu. Other texts say that his mother is Danu; while others yet place him as the father of Danu, perhaps due to her association with Brigit, daughter of the Dagda. The Dagda\'s siblings include the gods Ogma and Lir.', 'resource_uri': '/api/figures/5/'}, {'kind': 'Goddess', 'name': 'Ixchel', 'id': 10, 'related_figures': ['/api/figures/2/'], 'related_stories': [], 'related_cultures': ['/api/cultures/3/'], 'biography': 'Ixchel or Ix Chel (Mayan: [iʃˈt͡ʃel]) is the 16th-century name of the aged jaguar goddess of midwifery and medicine in ancient Maya culture. She corresponds, more or less, to Toci Yoalticitl "Our Grandmother the Nocturnal Physician", an Aztec earth goddess inhabiting the sweatbath, and is related to another Aztec goddess invoked at birth, viz. Cihuacoatl (or Ilamatecuhtli). In Taube\'s revised Schellhas-Zimmermann classification of codical deities, Ixchel corresponds to the goddess O.', 'resource_uri': '/api/figures/10/'}, {'kind': '', 'name': 'The Morrígan', 'id': 6, 'related_figures': ['/api/figures/5/'], 'related_stories': ['/api/stories/4/'], 'related_cultures': ['/api/cultures/2/'], 'biography': 'The Morrígan ("phantom queen") or Mórrígan ("great queen"), also written as Morrígu or in the plural as Morrígna, and spelt Morríghan or Mór-ríoghain in Modern Irish, is a figure from Irish mythology who appears to have been considered a goddess, although she is not explicitly referred to as such in the texts.\nThe Morrígan is a goddess of battle, strife, and sovereignty. She sometimes appears in the form of a crow, flying above the warriors, and in the Ulster cycle she also takes the forms of an eel, a wolf and a cow. She is generally considered a war deity comparable with the Germanic Valkyries, although her association with a cow may also suggest a role connected with wealth and the land.\nShe is often depicted as a trio of goddesses, all sisters, although membership of the triad varies; the most common combinations are Badb, Macha and Nemain, or Badb, Macha and Anand; Anand is also given as an alternate name for Morrigu. Other accounts name Fea, and others.', 'resource_uri': '/api/figures/6/'}, {'kind': 'Goddess', 'name': 'Shiva', 'id': 7, 'related_figures': ['/api/figures/8/'], 'related_stories': ['/api/stories/5/'], 'related_cultures': ['/api/cultures/5/'], 'biography': 'Shiva (Śiva; /ˈʃɪvə/  listen  meaning "The Auspicious One"), also known as Parameshwara (God), Mahadeva, Mahesh ("Great God") or Bholenath ("Simple Lord"), is a popular Hindu deity and is considered to be the Supreme God within Shaivism, one of the three most influential denominations in Hinduism. Shiva is regarded as one of the primary forms of God, such as one of the five primary forms of God in the Smarta tradition, and "the Destroyer" or "the Transformer" among the Trimurti, the Hindu Trinity of the primary aspects of the divine. Shiva is also regarded as the patron god of yoga and arts.\nShiva is usually worshiped in the aniconic form of Lingam. Shiva of the highest level is limitless, transcendent, unchanging and formless. However, Shiva also has many benevolent and fearsome forms. In benevolent aspects, he is depicted as an omniscient Yogi who lives an ascetic life on Mount Kailash, as well as a householder with wife Parvati and His two children, Ganesha and Kartikeya, or as the Cosmic Dancer. In fierce aspects, he is often depicted slaying demons. The most recognizable iconographical attributes of the God is a third eye on his forehead, a snake around his neck, the crescent moon adorning and the river Ganga flowing from his matted hair, the trishula as his weapon and the damaru as his instrument.\nShiva, as we know him today, shares features with the Vedic god Rudra. Historians have also suggested that worship of Shiva existed in pre-Vedic times, but not all historians agree on this.', 'resource_uri': '/api/figures/7/'}, {'kind': 'God', 'name': 'Osiris', 'id': 9, 'related_figures': [], 'related_stories': ['/api/stories/6/'], 'related_cultures': ['/api/cultures/6/'], 'biography': 'Osiris (/oʊˈsaɪərɨs/; Ancient Greek: Ὄσιρις, also Usiris; the Egyptian language name is variously transliterated Asar, Asari, Aser, Ausar, Ausir, Wesir, Usir, Usire or Ausare) is an Egyptian god, usually identified as the god of the afterlife, the underworld and the dead. He was classically depicted as a green-skinned man with a pharaoh\'s beard, partially mummy-wrapped at the legs, wearing a distinctive crown with two large ostrich feathers at either side, and holding a symbolic crook and flail.\nOsiris was at times considered the oldest son of the Earth god Geb, and the sky goddess Nut, as well as being brother and husband of Isis, with Horus being considered his posthumously begotten son. He was also associated with the epithet Khenti-Amentiu, which means "Foremost of the Westerners" — a reference to his kingship in the land of the dead. As ruler of the dead, Osiris was also sometimes called "king of the living", since the Ancient Egyptians considered the blessed dead "the living ones".\nOsiris is first attested in the middle of the Fifth dynasty of Egypt, although it is likely that he was worshipped much earlier; the term Khenti-Amentiu dates to at least the first dynasty, also as a pharaonic title. Most information available on the myths of Osiris is derived from allusions contained in the Pyramid Texts at the end of the Fifth Dynasty, later New Kingdom source documents such as the Shabaka Stone and the Contending of Horus and Seth, and much later, in narrative style from the writings of Greek authors including Plutarch and Diodorus Siculus.\nOsiris was considered not only a merciful judge of the dead in the afterlife, but also the underworld agency that granted all life, including sprouting vegetation and the fertile flooding of the Nile River. He was described as the "Lord of love", "He Who is Permanently Benign and Youthful" and the "Lord of Silence". The Kings of Egypt were associated with Osiris in death — as Osiris rose from the dead they would, in union with him, inherit eternal life through a process of imitative magic. By the New Kingdom all people, not just pharaohs, were believed to be associated with Osiris at death, if they incurred the costs of the assimilation rituals.\nThrough the hope of new life after death, Osiris began to be associated with the cycles observed in nature, in particular vegetation and the annual flooding of the Nile, through his links with Orion and Sirius at the start of the new year. Osiris was widely worshipped as Lord of the Dead until the suppression of the Egyptian religion during the Christian era.', 'resource_uri': '/api/figures/9/'}]

		self.assertTrue(expected_response == response_data["objects"])
	"""
	def test_post_figure(self) :
		values = dumps({"biography":"Long text description here.","kind":"God","name":"Loki","related_cultures":["/api/cultures/1/"],"related_figures":["/api/figures/2/"],"related_stories":["/api/stories/1/"]}).encode("utf-8")		
		headers = {"Content-Type": "application/json"}
		request = Request(self.url+"/api/figures/?format=json", data=values, headers=headers)
		#request.get_method = lambda: 'POST'
		response = urlopen(request)
		response_body = response.info()["Location"]
		self.assertEqual(response.getcode(), 201)
	"""

	def test_get_figure(self) :
		expected_response = {
		  "biography": "In Greek religion and mythology, Athena or Athene (/əˈθiːnə/ or /əˈθiːniː/; Attic: Ἀθηνᾶ, Athēnā or Ἀθηναία, Athēnaia; Epic: Ἀθηναίη, Athēnaiē; Ionic: Ἀθήνη, Athēnē; Doric: Ἀθάνα, Athānā), also referred to as Pallas Athena/Athene (/ˈpæləs/; Παλλὰς Ἀθηνᾶ; Παλλὰς Ἀθήνη), is the goddess of wisdom, courage, inspiration, civilization, law and justice, just warfare, mathematics, strength, strategy, the arts, crafts, and skill. Minerva is the Roman goddess identified with Athena.\nAthena is portrayed as a shrewd companion of heroes and is the patron goddess of heroic endeavour. She is the virgin patroness of Athens. The Athenians founded the Parthenon on the Acropolis of her namesake city, Athens (Athena Parthenos), in her honour.\nAthena's veneration as the patron of Athens seems to have existed from the earliest times, and was so persistent that archaic myths about her were recast to adapt to cultural changes. In her role as a protector of the city (polis), many people throughout the Greek world worshiped Athena as Athena Polias (Ἀθηνᾶ Πολιάς \"Athena of the city\"). The city of Athens and the goddess Athena essentially bear the same name (Athena the Goddess, Athenai the city) while it is not known which of the two words is derived from the other.", 
		  "id": 1, 
		  "kind": "Olympian", 
		  "name": "Athena", 
		  "related_cultures": [
		    "/api/cultures/1/", 
		    "/api/cultures/8/"
		  ], 
		  "related_figures": [
		    "/api/figures/2/"
		  ], 
		  "related_stories": [
		    "/api/stories/1/"
		  ], 
		  "resource_uri": "/api/figures/1/"
		}

		request = Request(self.url+"/api/figures/1/?format=json")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		self.assertTrue(expected_response == response_data)

	def test_post_and_delete_figure(self) :
		values = dumps({"biography":"Long text description here.","kind":"God","name":"Loki","related_cultures":["/api/cultures/1/"],"related_figures":["/api/figures/2/"],"related_stories":["/api/stories/1/"]}).encode("utf-8")		
		headers = {"Content-Type": "application/json"}
		request = Request(self.url+"/api/figures/?format=json", data=values, headers=headers)
		#request.get_method = lambda: 'POST'
		response = urlopen(request)
		response_body = response.info()["Location"]
		self.assertEqual(response.getcode(), 201)

		request = Request(response_body)
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()

		self.assertEqual(response.getcode(), 204)

	#Stories

	def test_get_all_stories(self) :


		request = Request(self.url+"/api/stories")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		#print(response_data)
		expected_response = [{'name': 'Trojan War', 'id': 1, 'related_figures': [], 'related_stories': ['/api/stories/2/'], 'summary': 'In Greek mythology, the Trojan War was waged against the city of Troy by the Achaeans (Greeks) after Paris of Troy took Helen from her husband Menelaus king of Sparta. The war is one of the most important events in Greek mythology and has been narrated through many works of Greek literature, most notably through Homer\'s Iliad. The Iliad relates a part of the last year of the siege of Troy; its sequel, the Odyssey describes Odysseus\'s journey home. Other parts of the war are described in a cycle of epic poems, which have survived through fragments. Episodes from the war provided material for Greek tragedy and other works of Greek literature, and for Roman poets including Virgil and Ovid.\nThe war originated from a quarrel between the goddesses Athena, Hera, and Aphrodite, after Eris, the goddess of strife and discord, gave them a golden apple, sometimes known as the Apple of Discord, marked "for the fairest". Zeus sent the goddesses to Paris, who judged that Aphrodite, as the "fairest", should receive the apple. In exchange, Aphrodite made Helen, the most beautiful of all women and wife of Menelaus, fall in love with Paris, who took her to Troy. Agamemnon, king of Mycenae and the brother of Helen\'s husband Menelaus, led an expedition of Achaean troops to Troy and besieged the city for ten years because of Paris\' insult. After the deaths of many heroes, including the Achaeans Achilles and Ajax, and the Trojans Hector and Paris, the city fell to the ruse of the Trojan Horse. The Achaeans slaughtered the Trojans (except for some of the women and children whom they kept or sold as slaves) and desecrated the temples, thus earning the gods\' wrath. Few of the Achaeans returned safely to their homes and many founded colonies in distant shores. The Romans later traced their origin to Aeneas, one of the Trojans, who was said to have led the surviving Trojans to modern-day Italy.\nThe ancient Greeks thought that the Trojan War was a historical event that had taken place in the 13th or 12th century BC, and believed that Troy was located in modern-day Turkey near the Dardanelles. As of the mid-19th century, both the war and the city were widely believed to be non-historical. In 1868, however, the German archaeologist Heinrich Schliemann met Frank Calvert, who convinced Schliemann that Troy was at Hissarlik and Schliemann took over Calvert\'s excavations on property belonging to Calvert; this claim is now accepted by most scholars. Whether there is any historical reality behind the Trojan War is an open question. Many scholars believe that there is a historical core to the tale, though this may simply mean that the Homeric stories are a fusion of various tales of sieges and expeditions by Mycenaean Greeks during the Bronze Age. Those who believe that the stories of the Trojan War are derived from a specific historical conflict usually date it to the 12th or 11th centuries BC, often preferring the dates given by Eratosthenes, 1194–1184 BC, which roughly corresponds with archaeological evidence of a catastrophic burning of Troy VII.', 'related_cultures': ['/api/cultures/1/'], 'resource_uri': '/api/stories/1/'}, {'name': 'Kamiumi', 'id': 9, 'related_figures': [], 'related_stories': ['/api/stories/10/'], 'summary': 'In Japanese mythology, the story of the birth of the gods (神産み, Kamiumi?) occurs after the creation of Japan (Kuniumi) and refers to the birth of the kami, descendants of Izanagi and Izanami.', 'related_cultures': ['/api/cultures/10/'], 'resource_uri': '/api/stories/9/'}, {'name': 'Labours of Hercules', 'id': 2, 'related_figures': [], 'related_stories': ['/api/stories/1/'], 'summary': 'The twelve labours of Hercules or dodekathlon (Greek: δωδέκαθλον, dodekathlon) are a series of episodes concerning a penance carried out by Heracles, the greatest of the Greek heroes, whose name was later romanised as Hercules. The episodes were later connected by a continuous narrative. The establishment of a fixed cycle of twelve labours was attributed by the Greeks to an epic poem, now lost, written by Peisander, dated about 600 BC.', 'related_cultures': ['/api/cultures/1/'], 'resource_uri': '/api/stories/2/'}, {'name': 'Ragnarök', 'id': 3, 'related_figures': [], 'related_stories': [], 'summary': 'In Norse mythology, Ragnarök is a series of future events, including a great battle foretold to ultimately result in the death of a number of major figures (including the gods Odin, Thor, Týr, Freyr, Heimdallr, and Loki), the occurrence of various natural disasters, and the subsequent submersion of the world in water. Afterward, the world will resurface anew and fertile, the surviving and returning gods will meet, and the world will be repopulated by two human survivors. Ragnarök is an important event in the Norse canon, and has been the subject of scholarly discourse and theory.\nThe event is attested primarily in the Poetic Edda, compiled in the 13th century from earlier traditional sources, and the Prose Edda, written in the 13th century by Snorri Sturluson. In the Prose Edda, and a single poem in the Poetic Edda, the event is referred to as Ragnarök or Ragnarøkkr (Old Norse "Fate of the Gods" and "Twilight of the Gods" respectively), a usage popularized by 19th-century composer Richard Wagner with the title of the last of his Der Ring des Nibelungen operas, Götterdämmerung (1876).', 'related_cultures': ['/api/cultures/4/'], 'resource_uri': '/api/stories/3/'}, {'name': 'Beltane', 'id': 4, 'related_figures': [], 'related_stories': [], 'summary': 'Beltane or Beltain /ˈbɛlteɪn/ (also Beltine or Beltaine) is the Gaelic May Day festival. Most commonly it is held on 30 April–1 May, or halfway between the spring equinox and the summer solstice. It was observed in Ireland, Scotland and the Isle of Man. In Irish it is Bealtaine ([ˈbʲal̪ˠt̪ˠənʲə]), in Scottish Gaelic Bealltainn ([ˈpjaul̪ˠt̪ˠɪɲ]) and in Manx Gaelic Boaltinn or Boaldyn. It is one of the four Gaelic seasonal festivals; along with Samhain, Imbolc and Lughnasadh.\nBeltane is mentioned in some of the earliest Irish literature and it is associated with important events in Irish mythology. It marked the beginning of summer and was when cattle were driven out to the summer pastures. Rituals were performed to protect the cattle, crops and people, and to encourage growth. Special bonfires were kindled, and their flames, smoke and ashes were deemed to have protective powers. The people and their cattle would walk around the bonfire, or between two bonfires, and sometimes leap over flames or embers. All household fires would be doused and then re-lit from the Beltane bonfire. Doors, windows, byres and the cattle themselves would be decorated with yellow May flowers, perhaps because they evoked fire. In parts of Ireland, people would make a May Bush; a thorn bush decorated with flowers, ribbons and bright shells. Holy wells were also visited, while Beltane dew was thought to bring beauty and maintain youthfulness. Many of these customs were part of May Day or Midsummer festivals in other parts of Great Britain and Europe.\nAs a festival, Beltane had largely died-out by the mid-20th century, although some of its customs continued and in some places it has been revived as a cultural event. Since the latter 20th century, Celtic neopagans and Wiccans have observed Beltane, or something based on Beltane, as a religious holiday. Neopagans in the Southern Hemisphere often celebrate Beltane at the other end of the year (~31 October–1 November).', 'related_cultures': ['/api/cultures/2/'], 'resource_uri': '/api/stories/4/'}, {'name': 'Ashvamedha', 'id': 5, 'related_figures': [], 'related_stories': [], 'summary': 'The Ashvamedha (Sanskrit: अश्वमेध aśvamedhá; "horse sacrifice") was one of the most important royal rituals of Vedic religion, described in detail in the Yajurveda (TS 7.1-5, VSM 22–25 and the pertaining commentary in the Shatapatha Brahmana ŚBM 13.1–5). The Rigveda does have descriptions of horse sacrifice, notably in hymns RV 1.162-163 (which are themselves known as aśvamedha), but does not allude to the full ritual according to the Yajurveda.\nAs per Brahma Vaivarta Purana (185.180), the Ashvamedha is one of five rites forbidden in the Kali Yuga, the present age.', 'related_cultures': ['/api/cultures/5/'], 'resource_uri': '/api/stories/5/'}, {'name': 'Flooding of the Nile', 'id': 6, 'related_figures': [], 'related_stories': [], 'summary': "The flooding of the Nile (Arabic: عيد وفاء النيل\u200e) has been an important natural cycle in Egypt since ancient times. It is celebrated by Egyptians as an annual holiday for two weeks starting August 15, known as Wafaa El-Nil. It is also celebrated in the Coptic Church by ceremonially throwing a martyr's relic into the river, hence the name, Esba` al-shahīd ('The Martyr's Finger'). Ancient Egyptians believed that the Nile flooded every year because of Isis's tears of sorrow for her dead husband, Osiris.", 'related_cultures': ['/api/cultures/6/'], 'resource_uri': '/api/stories/6/'}, {'name': 'Second Punic War', 'id': 7, 'related_figures': [], 'related_stories': [], 'summary': 'The Second Punic War, also referred to as The Hannibalic War, (by the Romans) The War Against Hannibal, or "The Carthaginian War", lasted from 218 to 201 BC and involved combatants in the western and eastern Mediterranean. This was the second major war between Carthage and the Roman Republic, with the crucial participation of Numidian-Berber armies and tribes on both sides. The two states had three major conflicts against each other over the course of their existence. They are called the "Punic Wars" because Rome\'s name for Carthaginians was Poeni, derived from Poenici (earlier form of Punici), a reference to the founding of Carthage by Phoenician settlers. \nThe war was to a considerable extent initiated by Rome, but is marked by Hannibal\'s surprising overland journey and his costly crossing of the Alps, followed by his reinforcement by Gallic allies and crushing victories over Roman armies in the battle of the Trebia and the giant ambush at Trasimene. In the following year (216), Hannibal\'s army defeated the Romans again, this time in southern Italy at Cannae. In consequence of these defeats, many Roman allies went over to Carthage, prolonging the war in Italy for over a decade. Against Hannibal\'s skill on the battlefield, the Romans deployed the Fabian strategy. Roman forces were more capable in siegecraft than the Carthaginians and recaptured all of the major cities that had joined the enemy, as well as defeating a Carthaginian attempt to reinforce Hannibal at the battle of the Metaurus. In the meantime, in Iberia, which served as the main source of manpower for the Carthaginian army, a second Roman expedition under Publius Cornelius Scipio Africanus Major took Carthago Nova by assault and ended Carthaginian rule over Iberia in the battle of Ilipa. The final showdown was the Battle of Zama in Africa between Scipio Africanus and Hannibal, resulting in the latter\'s defeat and the imposition of harsh peace conditions on Carthage, which ceased to be a major power and became a Roman client-state.\nA sideshow of this war was the indecisive First Macedonian War in the Eastern Mediterranean and the Ionian Sea.\nAll battles mentioned in the introduction are ranked among the most costly traditional battles of human history; in addition, there were a few successful ambushes of armies that also ended in their annihilation.', 'related_cultures': ['/api/cultures/8/'], 'resource_uri': '/api/stories/7/'}, {'name': 'Garden of Eden', 'id': 8, 'related_figures': [], 'related_stories': [], 'summary': 'The Garden of Eden (Hebrew גַּן עֵדֶן, Gan ʿEdhen) is the biblical "garden of God", described most notably in the Book of Genesis chapters 2 and 3, and also in the book of Ezekiel. The "garden of God", not called Eden, is mentioned in Genesis 14, and the "trees of the garden" are mentioned in Ezekiel 31. The Book of Zechariah and the Book of Psalms also refer to trees and water in relation to the temple without explicitly mentioning Eden.\nTraditionally, the favoured derivation of the name "Eden" was from the Akkadian edinnu, derived from a Sumerian word meaning "plain" or "steppe". Eden is now believed to be more closely related to an Aramaic root word meaning "fruitful, well-watered." The Hebrew term is translated "pleasure" in Sarah\'s secret saying in Genesis 18:12.\nThe Story of Eden echoes the Mesopotamian myth of a king, as a primordial man, who is placed in a divine garden to guard the tree of life. In the Hebrew Bible, Adam and Eve are depicted as walking around the Garden of Eden naked due to their innocence. Eden and its rivers may signify the real Jerusalem, the Temple of Solomon, or the Promised Land. It may also represent the divine garden on Zion, and the mountain of God, which was also Jerusalem. The imagery of the Garden, with its serpent and cherubs, has been compared to the images of the Solomonic Temple with its copper serpent, the nehushtan, and guardian cherubs.', 'related_cultures': ['/api/cultures/9/'], 'resource_uri': '/api/stories/8/'}, {'name': 'Kuniumi', 'id': 10, 'related_figures': [], 'related_stories': ['/api/stories/9/'], 'summary': 'In Japanese mythology, the creation of Japan (国産み, Kuniumi?, lit. "birth or formation of the country") is the traditional and legendary history of the emergence of the Japanese archipelago as narrated in the Kojiki and Nihon Shoki. According to this legend, after the creation of Heaven and Earth, the gods Izanagi and Izanami were given the task of forming a series of islands that would become what is now Japan. In Japanese mythology these islands make up the known world. The creation of Japan is followed by the creation of the gods (kamiumi).', 'related_cultures': ['/api/cultures/10/'], 'resource_uri': '/api/stories/10/'}]


		self.assertTrue(expected_response == response_data["objects"])
	"""
	def test_post_story(self) :

		values = dumps({
		    "name": "The Punishment of Atlas",
		    "related_cultures": [
		    	"/api/cultures/1/"
		    ],
		    "related_figures": [
		    	"/api/figures/1/"
		    ],
		    "related_stories": [
		    	"/api/stories/1/"
		    ],
		    "summary": "Long text description here."
		}).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request(self.url+"/api/stories", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 201)
		response_data = loads(response_body)
		self.assertTrue(expected_response == response_data)
	"""

	def test_get_story(self) :
		expected_response = {
		  "id": 1, 
		  "name": "Trojan War", 
		  "related_cultures": [
		    "/api/cultures/1/"
		  ], 
		  "related_figures": [], 
		  "related_stories": [
		    "/api/stories/2/"
		  ], 
		  "resource_uri": "/api/stories/1/", 
		  "summary": "In Greek mythology, the Trojan War was waged against the city of Troy by the Achaeans (Greeks) after Paris of Troy took Helen from her husband Menelaus king of Sparta. The war is one of the most important events in Greek mythology and has been narrated through many works of Greek literature, most notably through Homer's Iliad. The Iliad relates a part of the last year of the siege of Troy; its sequel, the Odyssey describes Odysseus's journey home. Other parts of the war are described in a cycle of epic poems, which have survived through fragments. Episodes from the war provided material for Greek tragedy and other works of Greek literature, and for Roman poets including Virgil and Ovid.\nThe war originated from a quarrel between the goddesses Athena, Hera, and Aphrodite, after Eris, the goddess of strife and discord, gave them a golden apple, sometimes known as the Apple of Discord, marked \"for the fairest\". Zeus sent the goddesses to Paris, who judged that Aphrodite, as the \"fairest\", should receive the apple. In exchange, Aphrodite made Helen, the most beautiful of all women and wife of Menelaus, fall in love with Paris, who took her to Troy. Agamemnon, king of Mycenae and the brother of Helen's husband Menelaus, led an expedition of Achaean troops to Troy and besieged the city for ten years because of Paris' insult. After the deaths of many heroes, including the Achaeans Achilles and Ajax, and the Trojans Hector and Paris, the city fell to the ruse of the Trojan Horse. The Achaeans slaughtered the Trojans (except for some of the women and children whom they kept or sold as slaves) and desecrated the temples, thus earning the gods' wrath. Few of the Achaeans returned safely to their homes and many founded colonies in distant shores. The Romans later traced their origin to Aeneas, one of the Trojans, who was said to have led the surviving Trojans to modern-day Italy.\nThe ancient Greeks thought that the Trojan War was a historical event that had taken place in the 13th or 12th century BC, and believed that Troy was located in modern-day Turkey near the Dardanelles. As of the mid-19th century, both the war and the city were widely believed to be non-historical. In 1868, however, the German archaeologist Heinrich Schliemann met Frank Calvert, who convinced Schliemann that Troy was at Hissarlik and Schliemann took over Calvert's excavations on property belonging to Calvert; this claim is now accepted by most scholars. Whether there is any historical reality behind the Trojan War is an open question. Many scholars believe that there is a historical core to the tale, though this may simply mean that the Homeric stories are a fusion of various tales of sieges and expeditions by Mycenaean Greeks during the Bronze Age. Those who believe that the stories of the Trojan War are derived from a specific historical conflict usually date it to the 12th or 11th centuries BC, often preferring the dates given by Eratosthenes, 1194–1184 BC, which roughly corresponds with archaeological evidence of a catastrophic burning of Troy VII."
		}


		request = Request(self.url+"/api/stories/1")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		#print(response_body)
		response_data = loads(response_body)

		self.assertTrue(expected_response == response_data)

	def test_post_and_delete_story(self) :
		values = dumps({
		    "name": "The Punishment of Atlas",
		    "related_cultures": [
		    	"/api/cultures/1/"
		    ],
		    "related_figures": [
		    	"/api/figures/1/"
		    ],
		    "related_stories": [
		    	"/api/stories/1/"
		    ],
		    "summary": "Long text description here."
		}).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request(self.url+"/api/stories", data=values, headers=headers)
		response = urlopen(request)
		self.assertEqual(response.getCode(), 201)

		request = Request(respone.info()["Location"])
		request.get_method = lambda: 'DELETE'
		response = urlopen(request)
		response_body = response.read()

		self.assertEqual(response.getcode(), 204)

	#Cultures

	def test_get_all_cultures(self) :


		request = Request("http://cs373idb.apiary-mock.com/api/cultures")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)
		expected_response = [{
		    "id": 1,
		    "title":"Greek",
		    "region":"Greece",
		    "language":"Greek",
		    "history":"Long text description here."
		}, {
		    "id": 2,
		    "title":"Roman",
		    "region":"Mediterranean",
		    "language":"Latin",
		    "history":"Long text description here."
		}, {
		    "id": 3,
		    "title":"Nordic",
		    "region":"Scandinavia",
		    "language":"Old Norse",
		    "history":"Long text description here."
		}]

		self.assertTrue(expected_response == response_data)

	def test_post_culture(self) :

		values = dumps({
		    "title":"Greek",
		    "region":"Greece",
		    "language":"Greek",
		    "history":"Long text description here.",
		    "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/a/ad/Parthenon_from_west.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/19/William_Faden._Composite_Mediterranean._1785.I.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/8/87/ArchaicGr.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/7/7c/Beginning_Odyssey.svg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/9/96/EarlyAthenianCoin.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/4/4a/Law_Code_Gortyn_Louvre_Ma703.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/a/a4/Socrates_Louvre.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/2/22/Greek-Persian_duel.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg"}],
		    "videos":[{"link":"http://www.youtube.com/embed/WptSXfvY-vs"},
		              {"link":"http://www.youtube.com/embed/vHMu2gVzspA"}],
		    "related_figures":[{"id":1, "name":"Atlas"}, {"id":2, "name":"Athena"}],
		    "related_stories":[],
		    "related_cultures":[{"id":2, "name":"Roman"}],
		    "external_links":[{"name":"Wikipedia: Greeks", "link":"http://en.wikipedia.org/wiki/Greeks"},
		                      {"name":"Wikipedia: Ancient Greece", "link":"http://en.wikipedia.org/wiki/Ancient_Greece"},
		                      {"name":"ancientgreece.com", "link":"http://www.ancientgreece.com/s/Main_Page/"},
		                      {"name":"BBC: Ancient Greeks", "link":"http://www.bbc.co.uk/schools/primaryhistory/ancient_greeks/"},
		                      {"name":"History Channel: Ancient Greeks", "link":"http://www.history.com/topics/ancient-history/ancient-greece"}]
		}).encode("utf-8")
		headers = {"Content-Type": "application/json"}
		request = Request("http://cs373idb.apiary-mock.com/api/cultures", data=values, headers=headers)
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 201)
		response_data = loads(response_body)
		expected_response = {
		    "id": 1
		}

		self.assertTrue(expected_response == response_data)

	def test_get_culture(self) :
		expected_response = {
		    "id": 1,
		    "title":"Greek",
		    "region":"Greece",
		    "language":"Greek",
		    "history":"Long text description here.",
		    "images":[{"link":"http://upload.wikimedia.org/wikipedia/commons/a/ad/Parthenon_from_west.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/19/William_Faden._Composite_Mediterranean._1785.I.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/8/87/ArchaicGr.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/7/7c/Beginning_Odyssey.svg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/9/96/EarlyAthenianCoin.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/4/4a/Law_Code_Gortyn_Louvre_Ma703.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/a/a4/Socrates_Louvre.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/2/22/Greek-Persian_duel.jpg"},
		              {"link":"http://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg"}],
		    "videos":[{"link":"http://www.youtube.com/embed/WptSXfvY-vs"},
		              {"link":"http://www.youtube.com/embed/vHMu2gVzspA"}],
		    "related_figures":[{"id":1, "name":"Atlas"}, {"id":2, "name":"Athena"}],
		    "related_stories":[],
		    "related_cultures":[{"id":2, "name":"Roman"}],
		    "external_links":[{"name":"Wikipedia: Greeks", "link":"http://en.wikipedia.org/wiki/Greeks"},
		                      {"name":"Wikipedia: Ancient Greece", "link":"http://en.wikipedia.org/wiki/Ancient_Greece"},
		                      {"name":"ancientgreece.com", "link":"http://www.ancientgreece.com/s/Main_Page/"},
		                      {"name":"BBC: Ancient Greeks", "link":"http://www.bbc.co.uk/schools/primaryhistory/ancient_greeks/"},
		                      {"name":"History Channel: Ancient Greeks", "link":"http://www.history.com/topics/ancient-history/ancient-greece"}]
		}

		request = Request("http://cs373idb.apiary-mock.com/api/cultures/{id}")
		response = urlopen(request)
		response_body = response.read().decode("utf-8")
		self.assertEqual(response.getcode(), 200)
		response_data = loads(response_body)

		self.assertTrue(expected_response == response_data)

	def test_delete_culture(self) :
		request = Request("http://cs373idb.apiary-mock.com/api/cultures/{id}")
		request.get_method = lambda: 'DELETE'

		response = urlopen(request)
		response_body = response.read()

		self.assertEqual(response.getcode(), 204)




print("Done.")