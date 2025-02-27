'''======= SPECIES ======== NOP-INFO-CARDS ======== LASER BREAD ===============
    Defines the information of a species in NoP.

    Some context you may want to know if you haven't read NoP (do it).

IDs:
    When the Federation probes a species' nautre during the uplifting process,
    it assigns them a letter and number.  Some species in NoP and its fanfics
    were never encountered by the feds (or were the founders), and thus don't
    have an id

    The number is the order in which
    species were uplifted          
                        \\-------> 245 - G <--\\ 
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

#=+=+=+=+=+ CLASS: SPECIES +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
#Defines everything a species needs for an info card to be constructed.
class species:
    
    #========= INIT =========================================================#
    def __init__(self):
        '''
        Define a species class
        '''
        self.name = "unknown"                           # Name of the species
        self.id = None            # ID given to the species by the Federation
        self.stances = []            # Dict of the species' stance and height
        self.blood = "???"                      # Color of the species' blood
        self.homeworld = "???"           # Planet the species originates from
        self.diet = "???"                             # What the species eats
        self.cure = False   # Did the species recieve The Cure on mass scale?
        self.alter = False  # Was the species' DNA altered (other than cure)?
        self.desc = None                         # descirption of the species
        self.flavor = None                       # Snarky quip ragarding them
        self.affiliations = []     # List of all affiliations the species has
        self.from_fanfic = False         # Is the species from an NoP fanfic?
        self.fic_name = None         # What is the fic's name (None if canon)
        self.fic_author = None# What is the fic author's name (none if canon)
        self.color_A_side = 0x000000               # The color for the A side
        self.color_B_side = 0x000000               # The color for the B side
    #=========================================================================#


    #--======== ADD AN AFFILIATION ===========================================#
    def add_affil(self, in_name: str, in_desc: str):
        '''
        Add an affiliation/faction listing for the species (up to 6)

        Args:
            in_name: The name of the affiliation
            in_desc: A brief description of the faction

        Raises:
            Exception: There can only be 6 affiliations
        '''
        #-------- CHECK AFFILIATION LIMIT ------------------------------------#
        if(len(self.affiliations) >= 6):
            raise Exception("Too many affiliation entries!")
        #---------------------------------------------------------------------#

        #Add the name and a little blurb about their time in the affiliation
        self.affiliations.append(dict(name = in_name, desc = in_desc))
    #=========================================================================#


    #========= GET AFFILIATION NAME ==========================================#
    def get_affil_name(self, index: int) -> str:
        '''
        Get the name of the affiliation at the specified index.

        Args:
            index: index to get

        Returns:
            str: Name of affiliation at index 

        Raises:
            IndexError
        '''
        return(self.affiliations[index]["name"])
    #=========================================================================#
    

    #=========== GET AFFILIATION DESCRIPTION =================================#
    def get_affil_desc(self, index: int) -> str:
        '''
        Get the description of the affiliation at the specified index.

        Args:
            index: Index to get

        Returns:
            str: Description of affiliation at index 

        Raises:
            IndexError
        '''
        return(self.affiliations[index]["desc"])
    #=========================================================================#


    #=========== REMOVE AN AFFILIATION =======================================#
    def rm_affil(self,index: int) -> dict:
        '''
        Delete an affiliation listing at the specified index.  No purpose
        here, but futureproofing for future use-cases

        Args:
            index: Index to get

        Returns:
            dict: Name and description of the removed affiliation

        Raises:
            IndexError
        '''
        return(self.affiliations.pop(index))
    #=========================================================================#


    #=========== ADD FANFIC INFORMATION ======================================#
    def add_fic(self,in_fic: str,in_author: str):
        '''
        Add info for a fanmade species.

        Args:
            in_fic: The title of the fanfic
            in_author: The name of the author (does not automatically add
                Reddit's 'u/' tag)
        '''
        self.from_fanfic = True
        self.fic_author = in_author
        self.fic_name = in_fic
    #=========================================================================#


    #========== REMOVE FANFIC NAME ===========================================#
    def rm_fic(self):
        '''
        Clear the fanfic status from the species.
        '''
        self.from_fanfic = False
        self.fic_author = None
        self.fic_name = None
    #=========================================================================#


    #=========== HAS FED ID ==================================================#
    def has_id(self) -> bool:
        '''
        Does the species have an ID given to them by the Federation?

        Returns:
            bool: Whether or not the species has an id.
        '''
        return(self.id != None)
    #=========================================================================#

    
    #=========== GET NUMBER OF BADGES ========================================#
    def num_badges(self) -> int:
        '''
        Status of the cure and other genetic tomfuckery are shown as badges 
        next to the species' portrait.  This returns the number of those
        badges.
        
        Returns:
            Number of Badges
        '''
        badges = 0
        if(self.cure):
            badges += 1
        if(self.alter):
            badges += 1
        return(badges)
    #=========================================================================#

    
    #=========== SET A-SIDE COLOR ============================================#
    def set_color_A(self, in_color):
        '''
        Set the a-side color from a hex color code.
        '''
        # if there's an octothrope, remove it
        if(in_color[0] == '#'):
            self.color_A_side = in_color
        else:
            self.color_A_side = '#' + in_color
    #=========================================================================#

    
    #=========== SET B-SIDE COLOR ============================================#
    def set_color_B(self, in_color):
        '''
        Set the b-side color from a hex color code
        '''
        # if there's an octothrope, remove it
        if(in_color[0] == '#'):
            self.color_B_side = in_color
        else:
            self.color_B_side = '#' + in_color
    #=========================================================================#

    
    #=========== ADD STANCE AND HEIGHT =======================================#
    def add_stance(self, in_stance: str, in_height_m: float):
        '''
        The galaxy is diverse. Some species are quadrupedal. Some are bipedal.
        Some are literally ant taurs. Again, diverse. Most notably is that
        some species can go bipedal and quadrupedal. This means that up to two
        stances can be added, alongside their associated heights.

        Args:
            in_stance: The name of the stance (eg, bipedal, quadrupedal)
            in_height: The species' typical height in meters while in this 
                stance. (Hint: quadrupeds are measured from shoulder down).

        Raises:
            Exception if there are more than two stances
        '''
        #-------- CHECK NUMBER OF STANCES ------------------------------------#
        if(self.num_stances() >= 2):
            raise Exception("There can only be up to two stances!")
        #---------------------------------------------------------------------#
        
        self.stances.append(dict(stance = in_stance, height = in_height_m))
    #=========================================================================#


    #=========== GET STANCE ===================================================#
    def get_stance(self,index: int) -> dict:
        '''
        Get a stance at the specified index.

        Args:
            index: Index of the stance to retrieve

        Returns:
            dict: Name and height of the stance
        '''
        return(self.stances[index])
    #=========================================================================#


    #=========== GET STANCES ==================================================#
    def num_stances(self) -> int:
        '''
        Get the number of stances.

        Returns:
            int: number of stances
        '''
        return(len(self.stances))
    #=========================================================================#


    #=========== FANCY HEIGHT =================================================#
    def fancy_height(self, index: int) -> str:
        '''
        Shows height in a fancy way.  Converts to oh-god-why
        imperial, and rounds that and the measurement system God intended to the
        nearest tenth.

        Args:
            index: Which stance will be printed
        
        Returns:
            str: Height in format " x ft / y m "
        '''
        output = str(round(self.stances[index]['height'] * 3.28084, 1))
        output += " ft / "
        output += str(round(self.stances[index]['height'], 1)) + " m"
        return(output)
    #=========================================================================#

#====+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+===#