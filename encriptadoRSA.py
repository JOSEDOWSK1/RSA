import random 
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def invmod(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def generarllave():
    p = int(input("numero p: "))
    q = int(input("numero q: "))
    n = p * q

    while True:
        x=(p - 1) * (q - 1)
        e = random.randrange(3,11)#obtener llave publica
        if gcd(e, x) == 1:
          break
    x=(p - 1) * (q - 1)
    d = invmod(e,x )#obtener llave privada
    llavepublica = (n, e)
    llaveprivada = (n, d)
    print("llave publica:", llavepublica)
    print("llave privada:", llaveprivada)
    mensaje=int(input("encriptar mensaje: "))
    mensajeencriptado=(mensaje**e)/n
    mensajeencriptado2=int(mensajeencriptado)
    cryp=int((mensaje**e)-(mensajeencriptado2)*n)
    print("mensaje encriptado: ", cryp)
    mensajedesencriptado=int((cryp**d)/n)
    mensajedesencriptado2=mensajedesencriptado*n
    decrypt=int((cryp**d)-mensajedesencriptado2)
    print("desencriptar mensaje: ", decrypt)
    return 0
def main():
  print(generarllave())
main()