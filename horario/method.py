class Horario:
    def __init__(self, hora: int, minuto: int): #_init_ é o construtor!
        self.hora = hora
        self.minuto = minuto
        
    def incrementar_hora(self): #Método que incrementa o horário em uma hora
        self.hora += 1
        if self.hora == 24:
            self.hora = 0
    
    def decrementar_hora(self): #Método que decrementa o horário em uma hora
        self.hora -= 1
        if self.hora == -1:
            self.hora = 23
    
    def decrementar_minuto(self): #Método que decrementa o horário em 1min
        self.minuto -= 1
        if self.minuto == -1:
            self.minuto = 59
            self.decrementar_hora()
    
    def incrementar_minuto(self): #Método que incrementa o horário em 1min
        self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.incrementar_hora()
    
    def __str__(self): #Método que retorna o horário no formato string
        return f"{self.hora:02d}:{self.minuto:02d}"
    
    def am_pm(self): #Método que verifica se é AM ou PM
        if self.hora > 12:
            return "PM"
        else:
            return "AM"