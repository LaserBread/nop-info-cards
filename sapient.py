'''====== SPECIES ======== NOP-INFO-CARDS ======== LASER BREAD ================
    Defines the information of a species in NoP.

    Some context you may want to know if you haven't read NoP (do it).

IDs:
    When the Federation probes a species' nautre during the uplifting process,
    it assigns them a letter and number.  Some species in NoP and its fanfics
    were never encountered by the feds (or were the founders), and thus don't
    have an id

    The number is the order in which
    species were uplifted          
                        \-------> 245 - G <--\
                                  (Human)     Appears to be a measure on
                                              how rebelious the species is.
                                              A: 100% Grade A docility!
                                              B: Mostly harmless
                                              C: Probably not a huge deal
                                              D: This may be a problem
                                              E: These bitches be predators
                                              F: Oh speh, oh brahk!
                                              G: Kneecap removal time
    
The Cure:
    The cure was how the federation forced its species to become vegan, by
    modifying their DNA to make them deathly allergic to meat.  Not the best
    use-case of genetic modifying technology.  All I'm saying is if you can
    make me allergic to meat, it's not a far-off possibility you could fix
    my pollen allergies.  Please.  I beg of you, farsul.
============================================================================'''

'''=+=+=+=+ CLASS: SPECIES +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+'''
#Defines everything a species needs for an info card to be constructed.
class species:
    
    '''======== INIT ====================================================='''
    def __init__(self):
        self.name = "unknown" # Name of the species
        self.id = None # ID given to the species by the Federation
        self.stances = [] # Dict of the species' stance and height.
        self.blood = "???" # Color of the species' blood
        self.homeworld = "???"  # Planet the species originates from
        self.diet = "???" # What the species eats
        self.cure = False # Did the species recieve The Cure on mass scale?
        self.alter = False # Was the species' DNA altered (other than cure)
        self.desc = None # descirption of the species
        self.flavor = None # Snarky quip ragarding them
        self.affiliations = [] # List of all affiliations the species has
        self.from_fanfic = False # Is the species from an NoP fanfic?
        self.fic_name = None # What is the fic's name (None if canon)
        self.fic_author = None # What is the fic author's name (none if canon)
        self.color_A_side = 0x000000 # The color for the A side
        self.color_B_side = 0x000000 # The color for the B side
    '''====================================================================='''


    '''======== ADD AN AFFILIATION ========================================='''
    # Add an affiliation listing for the species (up to 6)
    def add_affil(self, in_name, in_desc):

        #-------- CHECK AFFILIATION LIMIT ------------------------------------#
        if(len(self.affiliations) >= 6):
            raise Exception("Too many affiliation entries!")
        #---------------------------------------------------------------------#

        #Add the name and a little blurb about their time in the affiliation
        self.affiliations.append(dict(name = in_name, desc = in_desc))
    '''====================================================================='''


    '''======== GET AFFILIATION NAME ======================================='''
    # Get the name of the affiliation at the specified index.
    def get_affil_name(self, index):
        return(self.affiliations[index]["name"])
    '''====================================================================='''
    

    '''======== GET AFFILIATION DESCRIPTION ================================'''
    # Get the description of the affiliation at the specified index
    def get_affil_desc(self, index):
        return(self.affiliations[index]["desc"])
    '''====================================================================='''


    '''======== REMOVE AN AFFILIATION ======================================'''
    # Delete an affiliation listing at the specified index.  No purpose
    # here, but futureproofing for future use-cases
    def rm_affil(self,index):
        return(self.affiliations.pop(index))
    '''====================================================================='''


    '''======== ADD FANFIC INFORMATION ====================================='''
    # Add info for a fanmade species
    def add_fic(self,in_name,in_author):
        self.from_fanfic = True
        self.fic_author = in_author
        self.fic_name = in_name
    '''====================================================================='''


    '''======== GET AFFILIATION NAME ======================================='''
    # Clear the fanfic status from the species
    def rm_fic(self):
        self.from_fanfic = False
        self.fic_author = None
        self.fic_name = None
    '''====================================================================='''


    '''======== GET FED ID ================================================='''
    # Does the species have an ID given to them by the Federation?
    def has_id(self):
        return(self.id != None)
    '''====================================================================='''

    
    '''======== GET NUMBER OF BADGES ======================================='''
    # Status of the cure and other genetic tomfuckery are shown as badges next
    # to the species' portrait.  This returns the number of those badges.
    def num_badges(self):
        badges = 0
        if(self.cure):
            badges += 1
        if(self.alter):
            badges += 1
        return(badges)
    '''====================================================================='''

    
    '''======== SET A-SIDE COLOR ==========================================='''
    # Set the a-side color from a hex color code.
    def set_color_A(self, in_color):
        # if there's an octothrope, remove it
        if(in_color[0] == '#'):
            self.color_A_side = int(in_color[1:], base=16)
        else:
            self.color_B_side = int(in_color, base=16)
    '''====================================================================='''

    
    '''======== SET B-SIDE COLOR ==========================================='''
    # Set the b-side color from a hex color code.
    def set_color_B(self, in_color):
        # if there's an octothrope, remove it
        if(in_color[0] == '#'):
            self.color_B_side = int(in_color[1:], base=16)
        else:
            self.color_B_side = int(in_color, base=16)
    '''====================================================================='''

    
    '''======== ADD STANCE AND HEIGHT ======================================'''
    # The galaxy is diverse.  Some species are quadrupedal.  Some are bipedal.
    # Some are literally ant taurs.  Again, diverse.  Most notably is that
    # some species can go bipedal and quadrupedal.  This means that up to two
    # stances can be added, alongside their associated heights.
    def add_stance(self, in_stance, in_height):

        #-------- CHECK NUMBER OF STANCES ------------------------------------#
        if(self.num_stances() >= 2):
            raise Exception("There can only be up to two stances!")
        #---------------------------------------------------------------------#
        
        self.stances.append(dict(stance = in_stance, height = in_height))
    '''====================================================================='''


    '''======== GET STANCE ================================================='''
    # Get a stance at the specified index.
    def get_stance(self,int):
        return(self.stances[int])
    '''====================================================================='''


    '''======== GET STANCES ================================================'''
    # Get the number of stances.
    def num_stances(self):
        return(len(self.stances))
    '''====================================================================='''


    '''======== FANCY HEIGHT ==============================================='''
    # Shows height in the format of " x ft / y m ".  Converts to oh-god-why
    # impereal, and rounds that and the measurement system God intended to the
    # nearest tenth.
    def fancy_height(self, in_stance):
        output =  str(round(self.stances[in_stance]['height'] * 3.28084), 1)
        output += " ft / "
        output += str(round(self.stances[in_stance]['height']),1) + " m"
        return(output)
    '''====================================================================='''

'''=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='''