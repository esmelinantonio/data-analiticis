def torres_hanoi(n,origen,auxiliar,destino):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    torres_hanoi(n - 1, origen, destino, auxiliar, )
    print(f"Mover disco {n} de {origen} a {destino}")
    torres_hanoi(n - 1, auxiliar, origen,destino)

torres_hanoi(3,'A','B','C')
print("#######################################################")
def torres_hanoi(n, origen, destino, auxiliar):
  """
  Resuelve el problema de las Torres de Hanói de forma recursiva.

  Args:
    n: El número de discos a mover.
    origen: El poste de origen.
    destino: El poste de destino.
    auxiliar: El poste auxiliar.
  """
  # Caso base: Si solo hay un disco, muévelo y detente.
  if n == 1:
    print(f"Mover disco 1 de {origen} a {destino}")
    return

  # Paso 1: Mover n-1 discos del origen al auxiliar, usando el destino como temporal.
  torres_hanoi(n - 1, origen, auxiliar, destino)

  # Paso 2: Mover el disco más grande (el n-ésimo) del origen al destino.
  print(f"Mover disco {n} de {origen} a {destino}")

  # Paso 3: Mover los n-1 discos del auxiliar al destino, usando el origen como temporal.
  torres_hanoi(n - 1, auxiliar, destino, origen)

# ¡Probemos la magia con 3 discos!
num_discos = 3
torres_hanoi(num_discos, 'A', 'C', 'B')