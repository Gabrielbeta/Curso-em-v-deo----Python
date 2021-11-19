import emojis
from time import sleep

for contagem in range(10, -1, -1):
    print(contagem)
    sleep(0.5)
    
boom = emojis.encode(":bomb::bomb: BOOOOOMMMM!!! :bomb::bomb::bomb:")
print(boom)