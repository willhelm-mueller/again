from random import randint
class Tile ():
  __coords = []
  __color = 0
  
  __column_max = 0
  __row_max = 0
  
  def __init__(self,logger, size, color ):
    """
    """
    self.logger = logger 
    logger.debug ("Creating Tile size: {} color {}".format(size,color))
    self.__size = size
    self.__color = color

  def generate_coords(self):
    
    logger= self.logger
    
    ###
    # these start condition has to be random!
    ###
    column = 0
    row = randint(0,self.__size-1) 
    
    #zeros = [ [0] * N for _ in range(M)] this works ! 
    coords = [ [0] * self.__size for _ in range(self.__size) ]
    
    coords[row][column] = self.__color
    logger.debug ("create empty coords {}".format(coords) )
    remaining = self.__size -1 

    while remaining :
      row, column = self.calc_next_square(row,column)

      if  coords[row][column] == 0:
        logger.debug("Adding {} {} {}".format (row,column, remaining) )
        remaining -= 1
        
        coords[row][column] = self.__color
    self.__coords = coords
    logger.debug(self.draw_to_cli())
    ###
    # shrink coords, remove 0 rows and  0 columns
    ###    
    
    no_content =[]
    for i in range (len(coords) ):
      row_content = False 
      for j in range (self.__size):
        if coords[i][j]:
          row_content = True
      if  not row_content:
        logger.debug("row {} contains only zeros:{}".format (i,coords[i]))
        no_content.append(coords[i])
    
    for i in range (len(no_content)):
      logger.debug("removing from coords {}".format (no_content[i]))
      coords.remove(no_content[i])
    
    column_max = self.get_column_max()
    row_max = self.get_row_max()
      
    logger.debug("row_max: {}, column_max:{}".format(row_max, column_max ) ) 
      
    coords_shrink =   [ [0] * column_max for _ in range(row_max) ]
    
    for i in range (row_max):
      for j in range(column_max):
        coords_shrink[i][j] = coords[i][j]  
    logger.debug(coords_shrink)
    self.__coords = coords_shrink

  def calc_next_square(self,row, column): 
    new_column = 0
    new_row = 0
    
    ###
    # meh this "random" thing should be nicer in future ... <
    ###
    
    while (not new_column and not new_row) or (new_column and new_row): 
      if column == 0:
        new_column = randint(0,1)
      elif column == self.__size-1 :
        new_column = randint(-1,0)
      else: 
        new_column = randint(-1,1)
      if row == 0:
        new_row = randint(0,1)
      elif row == self.__size-1 :
        new_row = randint(-1,0)
      else:
        new_row = randint(-1,1)
    
    new_column += column 
    new_row += row 
    return  new_row, new_column

  def draw_to_cli(self):
    logger = self.logger
    logger.debug("current tile")
    cli_output = "\n"
    for i in range (len(self.__coords) ):
      for j in range (len (self.__coords[0])):
        cli_output += ("{}".format (self.__coords[i][j]))
      cli_output += ("\n")
    logger.debug (cli_output)
    logger.debug (self.__coords)
    return (cli_output)

  def get_color(self):
    return self.__color
    
  def get_coords(self):
    return self.__coords
    
  def get_size(self):
    return self.__size
  
  def get_column_max(self):
    if not self.__column_max:
      for i in range (len(self.__coords) ):
        for j in range (len(self.__coords[0]) ):
#      for i,j in zip (range (len(self.__coords) ), range (len(self.__coords[0])) ) :    
          if self.__coords[i][j]:
            if i > self.__row_max-1:
              self.__row_max = i+1
            if j > self.__column_max-1:
              self.__column_max = j+1
    return self.__column_max
    
    
  def get_row_max(self):
    if not self.__row_max:
      for i in range (len(self.__coords) ):
        for j in range (len(self.__coords[0]) ):
          if self.__coords[i][j]:
            if i > self.__row_max-1:
              self.__row_max = i+1
            if j > self.__column_max-1:
              self.__column_max = j+1
    return self.__row_max    
