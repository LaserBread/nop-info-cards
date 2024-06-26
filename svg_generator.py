from sapient import species
from lxml import etree
import os




'''======== CHECK CONTRAST ================================================='''
# Check the color and determine whether white text or black text should be
# used.
# Thanks to Filip Němeček for making a function I could plagirize or something 
#lol.
def check_contrast(hex_color):
        color = hex_color[1:]

        hex_red = int(color[0:2], base=16)
        hex_green = int(color[2:4], base=16)
        hex_blue = int(color[4:6], base=16)

        if (hex_red * 0.2126 + hex_green * 0.7152 + hex_blue * 0.0722 < 170):
            return("#ffffff")
        else:
            return("#000000")
'''========================================================================='''

affil_layout=[
    [],
    ['a'],
    ['a','b'],
    ['a','b','c'],
    ['0','1','2','3'],
    ['0','1','2','3','c'],
    ['0','1','2','3','4','5']
]

'''=+=+=+=+ SVG BUILDER +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='''
#Build an SVG image.
class builder:
    '''======== CLEAR AFFILIATIONS ========================================='''
    def clear_affil(self):
        for affil in self.affils.items():
            affil[1]['head'].text = ' '
            affil[1]['desc'].text = ' '
    '''====================================================================='''


    '''======== INIT ======================================================='''
    def __init__(self,filename):   
        with open(filename) as file:
            xml = file.read()
        self.fanfic = False
        self.isCured = False
        self.isAltered = False
        self.root = etree.fromstring(bytes(xml,encoding = 'utf-8'))
        self.name_pos = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:text[@id='name']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.name = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:text[@id='name']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.homeworld = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:text[@id='homeworld']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.blood = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:text[@id='blood-color']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.fed_id = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:text[@id='fed-id']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.diet = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:text[@id='diet']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.ftitle = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='fanfic-data']/svg:text[@id='fanfic-title']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.fauth = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='fanfic-data']/svg:text[@id='fanfic-author']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.ffrom = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='fanfic-data']/svg:text[@id='fanfic-header-from']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.desc = self.root.xpath("svg:g/svg:text[@id='desc']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.flavor = self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:text[@id='flavor-text']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]

        
        self.affils = {
            '0':{
                'head':self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-0']/svg:text[@id='affil-head-0']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-0']/svg:text[@id='affil-desc-0']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            '1':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-1']/svg:text[@id='affil-head-1']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-1']/svg:text[@id='affil-desc-1']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            '2':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-2']/svg:text[@id='affil-head-2']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-2']/svg:text[@id='affil-desc-2']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            '3':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-3']/svg:text[@id='affil-head-3']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-3']/svg:text[@id='affil-desc-3']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            '4':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-4']/svg:text[@id='affil-head-4']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-4']/svg:text[@id='affil-desc-4']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
            },
            '5':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-5']/svg:text[@id='affil-head-5']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-5']/svg:text[@id='affil-desc-5']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            'a':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-a']/svg:text[@id='affil-head-a']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-a']/svg:text[@id='affil-desc-a']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            'b':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-b']/svg:text[@id='affil-head-b']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-b']/svg:text[@id='affil-desc-b']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
            },
            'c':{
                "head":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-c']/svg:text[@id='affil-head-c']/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
                "desc":self.root.xpath("svg:g/svg:g[@id='b-side-text']/svg:g[@id='affiliation-c']/svg:text[@id='affil-desc-c']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
            }
        }
        
        self.clear_affil()

        self.bistance_stance = [
            self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='stance-1']/svg:text[@id='stance-name-1']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
            self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='stance-2']/svg:text[@id='stance-name-2']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        ]

        for stance in self.bistance_stance:
            stance.text = ' '
        
        self.bistance_height = [
            self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='stance-1']/svg:text[@id='height-1']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0],
            self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='stance-2']/svg:text[@id='height-2']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        ]
    
        for stance in self.bistance_height:
            stance.text = ' '
        
        self.monostance_stance = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='stance-0']/svg:text[@id='stance-name-0']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.monostance_stance.text = ' '
        self.monostance_height = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='stance-0']/svg:text[@id='height-0']/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.monostance_height.text = ' '

        self.cure_badge = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='cure-badge']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.alter_badge = self.root.xpath("svg:g/svg:g[@id='a-side-text']/svg:g[@id='alter-badge']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]

        self.kisser = self.root.xpath("svg:g/svg:g[@id='portrait']/svg:image", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]

        self.bg_aside = self.root.xpath("svg:g/svg:rect[@id='backdrop-a-side']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.bg_bside = self.root.xpath("svg:g/svg:rect[@id='backdrop-b-side']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]

        self.style_aside = self.root.xpath("svg:defs/svg:style[@id='a-side-style']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
        self.style_bside = self.root.xpath("svg:defs/svg:style[@id='b-side-style']", namespaces={'svg':'http://www.w3.org/2000/svg'})[0]
    '''====================================================================='''


    '''======== BUILD CARD ================================================='''
    def build(self,species):
        self.set_name(species.name)
        self.set_id(species.id)

        if(species.num_stances() == 1):
            self.set_monostance(species.get_stance(0)['stance'], species.fancy_height(0))
        else:
            self.set_bistance(species.get_stance(0)['stance'], species.fancy_height(0),species.get_stance(1)['stance'], species.fancy_height(1))

        self.set_blood(species.blood)
        self.set_homeworld(species.homeworld)
        self.set_diet(species.diet)
        
        self.set_fanfic(species.fic_name, species.fic_author)
        
        self.set_badges(species.cure, species.alter)

        self.set_affil(species)
        
        self.set_desc(species.desc)
        self.set_flavor(species.flavor)

        self.set_color_a(species.color_A_side)
        self.set_color_b(species.color_B_side)
        self.set_image("./assets/kissers/"+species.name+"-kisser.png")
        self.export("tmp.svg")
    '''====================================================================='''


    '''======== SET A-SIDE COLOR ==========================================='''
    # Set the color for the a-side of the image. Ajust text color for contrast.
    def set_color_a(self,colorIn):
        self.bg_aside.attrib['style'] = "fill: " + colorIn + ";fill-opacity: 1;"
        self.style_aside.text=".a-side {\nfill:" + check_contrast(colorIn) + ";\n }"
    '''====================================================================='''


    '''======== SET B-SIDE COLOR ==========================================='''
    # Set the color for the b-side of the image. Ajust text color for contrast.
    def set_color_b(self,colorIn):
        self.bg_bside.attrib['style'] = "fill: " + colorIn + ";fill-opacity: 1;"
        self.style_bside.text=".b-side {\nfill:" + check_contrast(colorIn) + ";\n }"
    '''====================================================================='''


    '''======== SET SPECIES NAME ==========================================='''
    # Set the species name.
    def set_name(self,nameIn):
        self.name.text = nameIn
    '''====================================================================='''


    '''======== SET FED ID ================================================='''
    # Set the species fed id.
    #I've explained this in sapient.py
    def set_id(self,idIn):
        if(idIn == None):
            self.name_pos.attrib['transform'] = "translate(-139.5019,0)"
            self.fed_id.text = ' '
        else:
            self.name_pos.attrib['transform'] = "translate(-139.5019,-46.630571)"
            self.fed_id.text = idIn
    '''====================================================================='''


    '''======== SET BLOOD COLOR ============================================'''
    # Set the blood color text.
    def set_blood(self,bloodIn):
        self.blood.text = bloodIn
    '''====================================================================='''


    '''======== SET BISTANCED HEIGHT ======================================='''
    # Set the heights for species with two stances.
    def set_bistance(self,stance0,height0,stance1,height1):
        #-------- CLEAR MONOSTANCE TEXT --------------------------------------#
        self.monostance_stance.text = ' '
        self.monostance_height.text = ' '
        #---------------------------------------------------------------------#

        #-------- SET BISTANCE TEXT ------------------------------------------#
        self.bistance_stance[0].text = stance0
        self.bistance_height[0].text = height0

        self.bistance_stance[1].text = stance1
        self.bistance_height[1].text = height1
        #---------------------------------------------------------------------#
    '''====================================================================='''


    '''======== SET MONOSTANCED HEIGHT ====================================='''
    #Set the height for species with only one stance.
    def set_monostance(self,stance,height):
        #-------- CLEAR BISTANCE TEXT ----------------------------------------#
        for st in self.bistance_height:
            st.text = ' '
        
        for st in self.bistance_stance:
            st.text = ' '
        #---------------------------------------------------------------------#
        
        #-------- SET MONOSTANCE TEXT ----------------------------------------#
        self.monostance_stance.text = stance
        self.monostance_height.text = height
        #---------------------------------------------------------------------#
    '''====================================================================='''


    '''======== SET HOMEWORLD =============================================='''
    # Set the homeworld
    def set_homeworld(self,homeworldIn):
        self.homeworld.text = homeworldIn
    '''====================================================================='''


    '''======== SET DIET ==================================================='''
    # Set the diet
    def set_diet(self,dietIn):
        self.diet.text = dietIn
    '''====================================================================='''

    '''AFFILIATIONS ARE LAID OUT AS SUCH
    full   1 affil   2 affil  3 affil  4 affil  5 affil  6 affil                                                                       
    0a1       a         a        a       0 1      0 1      0 1                                                                  
    2b3                 b        b       2 3      2 3      2 3                              
    4c5                          c                 c       4 5                                                                     

    '''


    '''======== SET AFFILIATION ============================================'''
    def set_affil(self,species):
        # Clear all affiliations from the thing.
        self.clear_affil()

        # Get the number of affiliations.  This is fed into the affil_layout
        # contains the dictionary keys for each layout.  Pretty elegant, if
        # I do say so myself.
        num_affils = len(species.affiliations)

        for i in range (0,num_affils):
           self.affils[affil_layout[num_affils][i]]['head'].text = (
               species.get_affil_name(i))
           self.affils[affil_layout[num_affils][i]]['desc'].text = (
               species.get_affil_desc(i))
    '''====================================================================='''


    '''======== SET FANFIC INFO ============================================'''    
    def set_fanfic(self,name,author):
        #-------- FANFIC HAS NO NAME, CLEAR DATA -----------------------------#
        if(name == None):
            self.fanfic = False
            self.ffrom.text = ' '
            self.ftitle.text = ' '
            self.fauth.text = ' '
        #-------- FANFIC HAS NAME, SET DATA ----------------------------------#
        else:
            self.fanfic = True
            self.ffrom.text = 'from'
            self.ftitle.text = name
            self.fauth.text = author
        #---------------------------------------------------------------------#

        #Reposition the badges
        self.set_badges(self.isCured, self.isAltered)
    '''====================================================================='''


    '''======== SET IMAGE =================================================='''
    # Set image, and fallback if there is none
    def set_image(self,imagefile):
        # Image exists, set it
        if(os.path.exists(imagefile)):
            self.kisser.attrib['href'] = imagefile
        # Image doesn't exist, do nothing.
        else:
            self.kisser.attrib['href'] = "./assets/placeholder-kisser.png"
    '''====================================================================='''


    '''======== POSITION BADGES ============================================'''
    # Set badge options
    def set_badges(self, cure, alter):
        #-------- SET CURE DATA ----------------------------------------------#
        self.isCured = cure
        self.isAltered = alter
        #---------------------------------------------------------------------#

        #-------- CURED AND ALTERED ------------------------------------------#
        if(cure and alter):
            #There is a fanfic, position both badges on the left side.
            if(self.fanfic):
                self.cure_badge.attrib['transform'] = "translate(-412.07,-1060.24)"
                self.alter_badge.attrib['transform'] = "translate(-374.967,-891.952)"
            #There is no fanfic, position on either side of the portrait
            else:
                self.cure_badge.attrib['transform'] = "translate(-412.07,-982.96)"
                self.alter_badge.attrib['transform'] = "translate(177.033,-982.973)"
        #-------- ONLY CURE --------------------------------------------------#
        elif(cure):
            self.cure_badge.attrib['transform'] = "translate(-412.07,-982.96)"
            self.alter_badge.attrib['transform'] = "translate(0,0)"
        #-------- ONLY ALTER -------------------------------------------------#
        elif(alter):
            self.cure_badge.attrib['transform'] = "translate(0,0)"
            self.alter_badge.attrib['transform'] = "translate(-374.967,-982.973)"
        #-------- NO BADGES --------------------------------------------------#
        else:
            self.cure_badge.attrib['transform'] = "translate(0,0)"
            self.alter_badge.attrib['transform'] = "translate(0,0)"
        #---------------------------------------------------------------------#
    '''====================================================================='''


    '''======== SET DESCRIPTION ============================================'''
    #Set description
    def set_desc(self,descIn):
        self.desc.text = descIn
    '''====================================================================='''


    '''======== SET FLAVOR TEXT ============================================'''
    #Set the funny flavor text
    def set_flavor(self,flavorIn):
        self.flavor.text = flavorIn
    '''====================================================================='''


    '''======== EXPORT FILE ================================================'''
    def export(self,filename):
        with open(filename, 'w') as file:
            file.write(etree.tostring(self.root).decode('utf-8'))
    '''====================================================================='''

'''=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+='''