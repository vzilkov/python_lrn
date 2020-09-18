import logging
class logging_class:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, 
        filename='examle.log',
        format='%(asctime)s :: %(levelname)s :: %(message)s')
        logging.info("Class initialized")
        for i in range(0,100,1):
            logging.info('Loop FOR, i=%d'%(i))