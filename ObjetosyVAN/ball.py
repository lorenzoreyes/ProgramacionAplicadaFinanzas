import random

class Tablero():
  """
  Descripcion del comportamiento de una pelota
  dentro de un tablero
  Configurar una matriz que sera la mesa
  indicador cantidad de filas rows
  indicador cantidad de columnas columns 
  asegurarse que la pelota no se vaya de los limites
  CURSOR 
  
  by_row ubicacion por fila
  by_column ubicacion por columna
  
  instancia __init__(self,lista,row,column,by_row=0)
  setear by_column, by_row =  0,0 
  
  field_oculto CURSOR variable que va a interactuar posicion
      self.row = int
      self.column = int 
      {"row":row,"column":column}
  
  funciones 
  get_position(self,row=self.row,column=self.column)
  setea ubicacion especifica fila y columna
  
  get_coordinates(self,m=print([self.row,self.column]))
  imprime la ubicacion 
  
  # switch intercambio de posicion fila x columna, reasigno valores
  switch(get_position(self,row=self.column,columnk=self.row))
  
  # imprimo contenido fila en que estoy ubicado
  get_row(self, print(self.row))
  
  # imprimo contenido de la columna en que estoy ubicado
  get_column(self, print(self.column))
  
  # borrar fila columna seleccionada
  del_row(self,del(self.row)) | del_column(self,del(self.column))
  
  # swap repetimos el switch intercambio orden filas y columnas
  swap(get_position(self,j=self.column,k=self.row))
  
  # Transpose transponer la matriz
  transpone(self,self.rows=self.columns,self.columns=self.rows)
  LISTO CON SWAP
    
  # mover: Arriba, Abajo, Izquierda y Derecha
  Asegurar respetar los limites
  """


  def __init__(self,lista):
        """
        matriz[row][column]
        lista:  list = lista que contenga las filas del tablero del juego
        row:    int =  posicion fila inicial en  el tablero asignado a 0
        column: int =  posicion columna inicial en  el tablero asignado a 0
        len_row: int = cantidad de filas - 1 (debido a que la funcion len arranca desde 1)
        len_column: int = cantidad de columnas - 1 (debido a que la funcion len arranca desde 1)
        row_bounds: list = limites inferior y superior de filas para no salirse del tablero
        column_bounds: list = limites inferior y superior de columnas para no salirse del tablero
        ball: dict = contiene la 
            position: de la pelota [fila=0, columna=0] como punto de partida
            value:    el valor del tablero donde esta posicionada la pelota
            row:      los datos de la fila donde esta posicionada la pelota
            column:   los datos de la columna donde esta posicionada la pelota        
        """
        self.lista = lista
        self.row = 0
        self.column = 0
        # aclaracion, la funcion len no arranca desde 0
        # por eso le resto 1 para que sea exacto
        self.len_row    = len(self.lista)    - 1
        self.len_column = len(self.lista[0]) - 1
        self.row_bounds = [min(0,self.len_row),max(1,self.len_row)]
        self.column_bounds = [min(0,self.len_column),max(1,self.len_column)]
       # punto de partida del indicador de posicion [0][0]
        self.ball = {"position": [self.row,self.column],
                       "value":  lista[self.row][self.column],
                       "row":    self.lista[0],
                       "column": [i[0] for i in self.lista]}
        
  def print(self):
      """Funcion para imprimir el estado del juego
      con todos sus datos, es llamada al final de cada
      funcion asi se notifica los cambios al usuario"""
      lista = self.lista 
      len_row, len_column = self.len_row, self.len_column
      print(f"La Matriz es {len_row} x {len_column}\n")
      print(*lista,sep='\n')
      print('\n\nBall Data')
      for key, value in self.ball.items():
              print(key,'\n\t',value)
    
  def set_position(self,row,column):
        """Funcion para setear una ubicacion 
        en caso de especificar solo row o column
        afectara la variable mencionada
        sin alterar la no mencionada"""
        self.row = row
        self.column = column
        # tengo que actualizar el ball
        self.ball = {"position": [self.row,self.column],
                       "value": self.lista[self.row][self.column],
                       "row": self.lista[self.row],
                       "column": [i[self.column] for i in self.lista]}
        # si, puedo llamar a otra funcion y compruebo si ejecuto los cambios
        self.print()
    
  def get_row(self):
      """Imprimo la lista ubicada"""
      print("La fila ubicada es {}\n\n{}".format(self.row,self.ball['row']))
    
  def get_colum(self):
        """Imprimo la lista ubicada"""
        print("La columna ubicada es {}\n\n{}".format(self.column,self.ball['column']),sep='\n')
       
  def del_row(self,row:int):
        """Borrar Fila"""
        del self.lista[row]
        self.print()
        
  def del_column(self,column:int):
    """Borrar Columna"""
    for i in range(len(selflista)):
        del self.lista[i][column]
        self.print()
            
  def swap(self):
        """Funcion para intercambiar los valores position del ball"""
        self.row, self.column = self.column, self.row
        # actualizo el ball
        self.ball = {"position": [self.row,self.column],
                       "value": self.lista[self.row][self.column],
                       "row": self.lista[self.row],
                       "column": [i[self.column] for i in self.lista]}
        self.print()
        
  def transpose(self):
        """Transpose matrix"""
        #lista = [[i[j] for i in lista] for j in range(len(lista))]
        self.lista = [[self.lista[i][j] for i in range(len(self.lista))] for j in range(len(self.lista))]        
        self.swap()
        self.print()
    
  def arriba(self):
      """Mover la pelota una fila arriba, dentro del limite"""
      self.row = self.row + 1  if self.row + 1 < max(self.row_bounds)  else max(self.row_bounds)
      # tengo que actualizar el ball
      self.ball = {"position": [self.row,self.column],
                       "value": self.lista[self.row][self.column],
                       "row": self.lista[self.row],
                       "column": [i[self.column] for i in self.lista]}
      self.print()
        
  def abajo(self):
      """Mover la pelota una fila abajo, dentro del limite"""
      self.row = self.row - 1  if self.row -1 > min(self.row_bounds) else min(self.row_bounds)
      self.ball = {"position": [self.row,self.column],
                       "value": self.lista[self.row][self.column],
                       "row": self.lista[self.row],
                       "column": [i[self.column] for i in self.lista]}
      self.print()

  def izquierda(self):
      """Mover la pelota una fila abajo, dentro del limite"""
      self.column = self.column - 1  if self.column - 1 > min(self.column_bounds) else min(self.column_bounds)
      # tengo que actualizar el ball
      self.ball = {"position": [self.row,self.column],
                       "value": self.lista[self.row][self.column],
                       "row": self.lista[self.row],
                       "column": [i[self.column] for i in self.lista]}
      self.print()
      
  def derecha(self):
      """Mover la pelota una columna derecha, dentro del limite"""
      self.column = self.column + 1  if self.column + 1 < max(self.column_bounds) else max(self.column_bounds)
      # tengo que actualizar el ball
      self.ball = {"position": [self.row,self.column],
                       "value": self.lista[self.row][self.column],
                       "row": self.lista[self.row],
                       "column": [i[self.column] for i in self.lista]}
      self.print()


# generamos una matriz 5 x 5 aleatoria
lista = [[random.randint(10,99) for _ in range(5)] for _ in range(5)]

# la inicializamos con la lista creada
pelota = Tablero(lista)

# observamos el punto de partida
pelota.print()

# imprimimos sus fields
#print([print(f"\nKey es:\t{k},\tSu value:\t{v}\n") for k,v in pelota.__dict__.items()])
