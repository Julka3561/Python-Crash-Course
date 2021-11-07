#import printing_functions
import printing_functions as pf
#from printing_functions import print_models
#from printing_functions import print_models as pm
#from printing_functions import *


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

