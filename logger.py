#import logging
import logging.config

def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()

@singleton
class Logger():
    def __init__(self):
        self.logr = logging.getLogger('root')

	log_filename='/var/log/RomyBox.log'

# set up logging to file - see previous section for more details
	logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_filename,
                    filemode='w')

	self.handler = logging.handlers.RotatingFileHandler(
              log_filename, maxBytes=20, backupCount=5)

# define a Handler which writes INFO messages or higher to the sys.stderr
	self.console = logging.StreamHandler()
	self.console.setLevel(logging.INFO)

# set a format which is simpler for console use
	self.formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format
	self.console.setFormatter(self.formatter)
# add the handler to the root logger
	self.logr.addHandler(self.console)
#	self.logr.addHandler(self.handler)
