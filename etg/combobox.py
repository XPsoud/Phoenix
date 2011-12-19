#---------------------------------------------------------------------------
# Name:        etg/combobox.py
# Author:      Kevin Ollivier
#              Robin Dunn
#
# Created:     09-Sept-2011
# Copyright:   (c) 2011 by Kevin Ollivier
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"
MODULE    = "_core"
NAME      = "combobox"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ 'wxComboBox' ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    c = module.find('wxComboBox')
    c.abstract = False
    c.find('wxComboBox').findOverload('wxString choices').ignore()
    c.find('wxComboBox').findOverload('wxArrayString').find('choices').default = 'wxArrayString()'
    c.find('wxComboBox').findOverload('wxArrayString').find('value').default = 'wxEmptyString'

    c.find('Create').findOverload('wxString choices').ignore()
    c.find('Create').findOverload('wxArrayString').find('choices').default = 'wxArrayString()'
    c.find('Create').findOverload('wxArrayString').find('value').default = 'wxEmptyString'

    # We ignore this one because if from,to are set as output parameters the
    # methods will be ambiguous. Maybe the names should just be changed
    # instead?
    c.find('GetSelection').findOverload('long *from, long *to').ignore()
    
    # The docs say to not use this one.
    c.find('IsEmpty').ignore()

    tools.fixWindowClass(c)
    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

