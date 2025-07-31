from machine import Pin

from utime import sleep

print("Iniciando Sistema")

ledVerde = Pin(32,Pin.OUT)
ledAmarelo = Pin(25,Pin.OUT)
ledVermelho = Pin(5,Pin.OUT)

while True:
    ledVerde.on()
    print("Led Verde ligado")
    sleep(20)
    ledVerde.off()
    print("Led Verde desligado")
    sleep(0.5)
    
    ledAmarelo.on()
    print("Led Amarelo Ligado")
    sleep(10)
    ledAmarelo.off()
    print("Led Amarelo Desligado")
    sleep(0.5)

    ledVermelho.on()
    print("Led Vermelho Ligado")
    sleep(7)
    ledVermelho.off()
    print("Led Vermelho Desligado")
    sleep(0.5)

