from random import randint

class Again_Map ():
  __coords= []
  color_occupied_columns=[]
  
  def __init__(self,logger,row_count=7, column_count=15,  color_count=5, star_count=14,  ):
    """
    set size x,y color_amount
    """
    self.__column_count = column_count
    self.__row_count = row_count
    self.logger = logger
    coords = [ [0] * column_count for _ in range(row_count) ]
    color_occupied_columns = [[0] *column_count for _ in range (color_count) ]

    self.__coords= coords
    
  def set_tile(tile, color):
    """
    Place tile on map 
    """


  def get_column_count(self):
    return self.__column_count
    
  def get_row_count(self):
    return self.__row_count
 
  def draw_current_map_cli(self):
    logger=self.logger

    cli_output = ""

    ##
    # header
    ##


    header_list =[]
    for i in range (self.__column_count):
      header_list.append("{:>2}".format(i) )
    logger.debug("header_list: {}".format (header_list) )
    
    row_spacer="   "
    header = "{}{}|\n".format(row_spacer,  '|'.join(header_list) ) 
    logger.debug(header)
    cli_output += header 
    logger.debug("coords {}".format(self.__coords))
    map_content = ""
    for i in range (self.__row_count):
      current_row = ""
      for j in range (self.__column_count):
        #current_row += "  |"
        current_row += " {}|".format(self.__coords[i][j]) 
      map_content += "{}{}\n".format(row_spacer, current_row)
      
    cli_output += map_content  
    logger.debug("\n{}".format(cli_output))
    return cli_output
  

  def place_tile_on_map(self, tile):
    """
    This routine should move into againmap!
    Tiles of the same color may not touch each other
      diagonal tiles of the same color are oke
    tiles do not overlap columnwise 
      in a single column there are only tiles of the very same tile
    """
    
    logger = self.logger
    color = tile.get_color()
    row_max = tile.get_row_max()
    column_max = tile.get_column_max()
    tile_cli = tile.draw_to_cli()
    tile_size = tile.get_size()
    tile_coords=tile.get_coords()
    
    #again_map = self.__map
    
    logger.info("Placing tile {}row_max={}\ncolumn_max={}\non map".format(tile_cli, row_max, column_max))
    

    ###
    # get random position
    ###
    
    row_start     = randint(0,self.get_row_count()  )
    column_start  = randint(0,self.get_column_count() )

    ###
    # try to place tile on this position
    ###
  
  
    logger.debug("Trying to place Tile on row={} column={}".format(row_start, column_start) )
  
    if self.color_occupied_columns[color][row_start]:
      logger.warn("color {} already in coloun {}".format(color, row_sta))
    



  def generate_test_map(self, test_map = "green"):
    
    logger = self.logger
    
    logger.debug("Generating test map") 
    self.__column_count = 15
    self.__row_count = 7
    self.__color_count = 5
    self.__star_count=14
    self.__coords= []
    if test_map in ["green"] : # add other cards in here
      logger.debug("Generating {} map".format (test_map) )
    
    else:
      logger.debug("Could not find specified map {} leaving test routine".format (test_map))
      return #exception in future here! 
      
    if test_map == "green":
      
      ## green card
      self.__coords.append([5,1,3,3,4,4,4,1,1,1,2,2,2,4,4])
      self.__coords.append([1,1,1,1,4,2,1,4,1,1,4,2,2,4,2])
      self.__coords.append([3,3,5,1,2,2,1,3,4,4,4,4,5,5,2])
      self.__coords.append([3,5,5,5,5,1,1,3,3,3,3,5,4,5,5])
      self.__coords.append([3,4,5,4,3,5,5,5,3,2,5,5,4,2,5])
      self.__coords.append([4,4,4,4,3,3,3,2,2,2,5,3,1,1,1])
      self.__coords.append([2,2,2,2,1,3,2,2,5,5,1,1,3,3,3])
      
      #self.__coords.append([5,1,3,3,3,4,2])
      #self.__coords.append([1,1,3,5,4,4,2])
      
      """   
      self.__coords.append([5, 1, 3, 3, 3, 4, 2])
      self.__coords.append([1, 1, 3, 5, 4, 4, 2])
      self.__coords.append([3, 1, 5, 5, 5, 4, 2])
      self.__coords.append([3, 1, 1, 5, 4, 4, 2])
      self.__coords.append([4, 4, 2, 5, 3, 3, 1])
      self.__coords.append([4, 2, 2, 1, 5, 3, 3])
      self.__coords.append([4, 1, 1, 1, 5, 3, 2])
      self.__coords.append([1, 4, 3, 3, 5, 2, 2])
      self.__coords.append([1, 1, 4, 3, 3, 2, 5])
      self.__coords.append([1, 1, 4, 3, 2, 2, 5])
      self.__coords.append([2, 4, 4, 3, 5, 5, 1])
      self.__coords.append([2, 2, 4, 5, 5, 3, 1])
      self.__coords.append([2, 2, 5, 4, 4, 1, 3])
      self.__coords.append([4, 4, 5, 5, 2, 1, 3])
      self.__coords.append([4, 2, 2, 5, 5, 1, 3])
      """
      
