from .againmap import *
from .tile import * 

import logging

class Again ():
  def __init__(self, logger = None ):
    """
    """
    if not logger:
        logging.basicConfig(format  = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    datefmt = '%Y-%m-%d %H:%M:%S',
                    level   = logging.INFO
                    )

        logger = logging.getLogger('again')

        logger.level=logging.DEBUG
        logger.debug('start logging')

    self.logger = logger
    self.logger.debug("Start")
    self.__map = Again_Map(logger=logger)




  def run_test(self):
    """
    This mehtod tests basic functionality 
    """
    logger = self.logger
    logger.debug("Start test")
    tile = Tile(logger,5,2)
    tile.generate_coords()
    tile.draw_to_cli()
    self.__map.draw_current_map_cli()
    
    self.__map.place_tile_on_map(tile)
    
    self.__map.generate_test_map()
    self.__map.draw_current_map_cli()
