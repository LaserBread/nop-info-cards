'''===== SPREADSHEET PARSER ======== NoP INFO CARDS ======== LASER BREAD ======
   This script handles the parsing and reading of the spreadsheet that gets
   returned to the user.

   DEPENDENCIES:
        pandas library
        sapient.py from this file
============================================================================'''

import pandas as pd # Yes, this is how people use this library, it's not me making a stupid reference.

from sapient import species
import numbers

'''====== IS A NUMBER ======================================================'''
# Returns true if this is a number, false otherwise
def isNum(num):
    return(isinstance(num, numbers.Real))
'''========================================================================='''


'''====== POSSESSIVE FORMAT ================================================'''
# Formats input of a species' name to be possessive, and capitalizes it.
def nForm(name, capitalize):
    output = name

    #capitalize the name if true
    if(capitalize):
        output = output.title()

    #check if the s is already at the end, and if not, add 's.
    if(not(output[len(output)-1] == 's')):
        output += "'s"
    else:
        output += "'"
    
    return(output)
'''========================================================================='''


'''=+=+=+ CLASS: DATA TABLE +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='''
# This object handles retrieving species from a specifically formatted table.
# Here's the columns it.  Note that all columns must be present.  Requirement
# is only for what things can be left blank in entries.
'''
In a sheet called 'Basic Information, Affiliations':
    NAME                       TYPE            REQUIREMENT
    stance 1                   string          required
    height 1 (m)               number          required
    stance 2                   string          optional
    height 2 (m)               number          required if stance 2 is filled
    blood color                string          optional [set to unknown if blank]
    homeworld                  string          optional [set to unknown if blank]
    diet                       string          optional [set to unknown if blank]
    is cured                   boolean         required
    is genetically altered     boolean         required
    affiliation 1 head         string          optional 
    affiliation 1 description  string          optional
    affiliation 2 head         string          optional 
    affiliation 2 description  string          optional
    affiliation 3 head         string          optional 
    affiliation 3 description  string          optional
    affiliation 4 head         string          optional 
    affiliation 4 description  string          optional
    affiliation 5 head         string          optional 
    affiliation 5 description  string          optional
    affiliation 6 head         string          optional 
    affiliation 6 description  string          optional
    federation id              string          optional
In a sheet called 'Author, Description, and Colors':
    NAME                       TYPE            REQUIREMENT
    description                string          optional
    flavor text                string          optional
    a-side color               hex color code  optional [set black if invalid]
    b-side color               hex color code  optional [set black if invalid]
    fanfic title               string          optional
    fanfic author              string          required if fanfic title is filled
'''
# This class uses the panda lib, shortened to 'pd' (which is accurate since 
# its obtuse rules gave me predator disease, predator's disease, anxiety,
# The Hunger, Flood from Halo, COVID, vendemic, and every other real or 
# fictional or fictional fictional disease out there).  It parses through an
# xslx file, and is used to interface with the other parts of the program.
class datatable:

    '''======== INIT ======================================================='''
    # instantiates the file with the excel data.  
    def __init__(self, filename):
        # Read in file. TODO: Give an error if the input is wrong. 
        file = pd.ExcelFile(filename)
        
        # Open the individual sheets, and set them to scan columns, because
        # you can't do that by default.
        self.infotable = pd.read_excel(file, 'Basic Information, Affiliations', index_col = 0)
        self.desctable = pd.read_excel(file, 'Author, Description, and Colors', index_col = 0)
    '''====================================================================='''

    '''======== GET SPECIES ================================================'''
    # returns a species object of the requested name.  Throws an error if
    # data is invalid.
    def get_species(self, species_name):
        #-------- VARIABLES --------------------------------------------------#
        sp = species()                                          # Sepecies data
        stab = self.infotable.loc[species_name]       # Table with species data
        #---------------------------------------------------------------------#
        
        # Because index_col was set, species names are now off-limits from
        # being read as data.  Because panda retroactively gave me autism, the
        # species name must be set here.
        sp.name = species_name

        #-------- CHECK STANCE 1 ---------------------------------------------#
        if(pd.isnull(stab['stance 1'])):
            raise RuntimeError(nForm(sp.name,1)+" stance 1 is blank.  This is a required field.")
        #---------------------------------------------------------------------#

        #-------- CHECK HEIGHT 1 ---------------------------------------------#
        if(not(isNum(stab['height 1 (m)'])) or pd.isnull(stab['height 1 (m)'])):
            raise RuntimeError("Height 1 is blank or invalid.  This is a required field.")
        #---------------------------------------------------------------------#

        # Add Height 1
        sp.add_stance(stab['stance 1'], stab['height 1 (m)'])

        #-------- CHECK AND ADD STANCE 2 -------------------------------------#
        if( not( pd.isnull(stab['stance 2']) ) ):
            
            #-------- CHECK HEIGHT 2 -----------------------------------------#
            if(not(isNum(stab['height 2 (m)'])) or pd.isnull(stab['height 2 (m)'])):
                raise RuntimeError(nForm(sp.name,1)+" height 2 is blank or invalid.")
            #-----------------------------------------------------------------#
            
            sp.add_stance(stab['stance 2'], stab['height 2 (m)'])
        #---------------------------------------------------------------------#
            
        #-------- CHECK AND ADD BLOOD COLOR ----------------------------------#
        if(pd.isnull(stab["blood color"])):
            sp.blood = "unknown"
            print(nForm(sp.name,1)+" blood color is blank.  Displaying as \"unknown\".")

        sp.blood = stab["blood color"]
        #---------------------------------------------------------------------#

        #-------- CHECK AND ADD HOMEWORLD ------------------------------------#
        if(pd.isnull(stab['homeworld'])):
            sp.homeworld = "unknown"
            print(nForm(sp.name,1)+" homeworld is blank.  Displaying as \"unknown\".")
        sp.homeworld = stab["homeworld"]
        #---------------------------------------------------------------------#

        #-------- CHECK AND ADD BLOOD COLOR ----------------------------------#
        if(pd.isnull(stab["diet"])):
            sp.diet = "unknown"
            print(nForm(sp.name,1)+" diet is blank.  Displaying as \"unknown\".")
        sp.diet = stab["diet"]
        #---------------------------------------------------------------------#

        #-------- CHECK AND ADD BLOOD COLOR ----------------------------------#
        if(not(stab["is cured"] == True or stab["is cured"] == False)):
            raise RuntimeError(nForm(sp.name,1)+" cure status is blank or invalid.  This is a required field.")
        sp.cure = stab["is cured"]
        #---------------------------------------------------------------------#

        #-------- CHECK AND ADD BLOOD COLOR ----------------------------------#
        if(not(stab["is genetically altered"] == True or stab["is genetically altered"] == False)):
            raise RuntimeError(nForm(sp.name,1)+" genetic alteration status is blank or invalid.  This is a required field.")
        sp.alter = stab["is genetically altered"]
        #---------------------------------------------------------------------#

        #-------- ADD AFFILIATIONS -------------------------------------------#
        num_affil = 1 # It's not 0 based because of the way the sheet is set up
        
        # This number is directly fed into the string we use to search the
        # table.
        while(stab["affiliation " + str(num_affil)+" head"] and num_affil < 6):
            # Get the name of the affiliation
            affil = stab["affiliation " + str(num_affil)+" head"]
            # Get the description, if one exists.  Otherwise, set it to a blank
            # space to ensure it's not set to "NaN."
            if(pd.isnull(stab["affiliation " + str(num_affil)+" description"])):
                desc = " "
            else:
                desc = stab["affiliation " + str(num_affil)+" description"]
            
            # Add the affiliation to the species object
            sp.add_affil(affil, desc)
            num_affil += 1
        #---------------------------------------------------------------------#
        
        #-------- CHECK AND ADD FEDERATION ID --------------------------------#
        if(not(pd.isnull(stab['federation id']))):
            sp.id = stab['federation id']
        #---------------------------------------------------------------------#
            
        # Set the table to the description sheet.
        stab = self.desctable.loc[species_name]

        # Set the description
        sp.desc = stab["description"]

        #Set the flavor text
        sp.flavor = stab["flavor text"]
        
        #-------- CHECK AND ADD COLOR FOR CARD'S A-SIDE ----------------------#
        try:
            sp.set_color_A(stab["a-side color"])
        except:
            sp.set_color_A("000000")
            print("Side A for "+nForm(sp.name,None)+" card is blank or invalid.  Setting to black.")
        #---------------------------------------------------------------------#
        
        #-------- CHECK AND ADD COLOR FOR CARD'S B-SIDE ----------------------#
        try:
            sp.set_color_B(stab["b-side color"])
        except:
            sp.set_color_B("000000")
            print("Side B for "+nForm(sp.name,None)+" card is blank or invalid.  Setting to black.")
        #---------------------------------------------------------------------#
        
        #-------- CHECK AND ADD FANFIC TITLE ---------------------------------#
        if(not(pd.isnull(stab["fanfic title"]))):
            
            #-------- CHECK FOR FANFIC AUTHOR --------------------------------#
            if(pd.isnull(stab["fanfic author"])):
                raise RuntimeError("The fanfic the "+sp.name+"s come from has no author!  Please add an author.")
            #-----------------------------------------------------------------#

            sp.add_fic(stab["fanfic title"], stab["fanfic author"])
        #---------------------------------------------------------------------#
            
        # We're all done, so return the species object to the user.
        return(sp)
    '''====================================================================='''
    
    '''======== GET ALL ===================================================='''
    def get_all(self):
        sp_arr = []
        for row in self.infotable.iterrows():
            try:
                sp_arr.append(self.get_species(row[0]))
            except:
                print("The entry for " + row[0] + " is incomplete.  Skipping.")
        return(sp_arr)
    '''====================================================================='''

'''=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='''