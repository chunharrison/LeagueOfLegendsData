''' all controllers for various collections of database '''

# will import all the routes in all the files inside controllers directory. 
# When controllers module will be imported, 
# it will automatically define all the routes.
import os
import glob
__all__ = [os.path.basename(f)[:-3]
    for f in glob.glob(os.path.dirname(__file__) + "/*.py")]