import settings

def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage):
    return(settings.WIDTH / 100) * percentage

#defazer comentarios para testes se nessesário
# print(height_prct(25))
# print(width_prct(25))