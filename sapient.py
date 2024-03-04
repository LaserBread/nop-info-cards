######## SPECIES ######## NOP-INFO-CARDS ######## LASER BREAD #################
# Defines the information of a species in NoP.
###############################################################################

class species:
    def __init__(self, *args):
        if(len(args) == 9):
            self.fromseries(*args)
        else:
            
            self.name = "unknown" # Name of the species
            self.id = None
            self.ht = "???" # Average height of the species in feet
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
            self.color_A_side = 0x000000
            self.color_B_side = 0x000000
    
    
    def fromseries(self,name,htft,blood,homeworld,diet,cure,alter,desc,flavor):
        self.name = name
        self.ht = htft
        self.blood = blood
        self.homeworld = homeworld
        self.diet = diet
        self.cure = cure
        self.alter = alter
        self.desc = desc
        self.flavor = flavor
        self.affiliations = []
        self.from_fanfic = False
        self.fic_name = None
        self.fic_author = None
        self.id = None
        self.color_A_side = 0x000000
        self.color_B_side = 0x000000

    # Add an affiliation listing 
    def add_affil(self, in_name, in_desc):
        if(len(self.affiliations) > 6):
            raise Exception("Too many affiliation entries!")
        self.affiliations.append(dict(name = in_name, desc = in_desc))

    # Get the name of the affiliation
    def get_affil_name(self, index):
        return(self.affiliations[index]["name"])
    
    # Get the description of the affiliation
    def get_affil_desc(self, index):
        return(self.affiliations[index]["desc"])
    
    # Delete an affiliation listing
    def rm_affil(self,index):
        return(self.affiliations.pop(index))
    
    # Add info for a fanmade species
    def add_fic(self,in_name,in_author):
        self.from_fanfic = True
        self.fic_author = in_author
        self.fic_name = in_name

    # Clear the fanfic status from the species
    def rm_fic(self):
        self.from_fanfic = False
        self.fic_author = None
        self.fic_name = None

    # Does the species have an ID given to them by the Federation?
    def has_id(self):
        return(self.id != None)
    
    def num_badges(self):
        badges = 0
        if(self.cure):
            badges += 1
        if(self.alter):
            badges += 1
        return(badges)
    
    def set_color_A(self, in_color):
        if(in_color[0] == '#'):
            self.color_A_side = int(in_color[1:], base=16)
        else:
            self.color_B_side = int(in_color, base=16)
    
    def set_color_B(self, in_color):
        if(in_color.char[0] == '#'):
            self.color_B_side = int(in_color[1:], base=16)
        else:
            self.color_B_side = int(in_color, base=16)
    
    
