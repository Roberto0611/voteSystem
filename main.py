from Classes import ballot
import time

# Crear Nueva instancia de la clase ballot
box = ballot.ballot()

# Iniciar el ciclo del sistema
while True:

    # Mensaje con los comandos tras esperar 2.5 segundos
    time.sleep(2.5)
    print("Bienvenido al sistema de votos, Ingresa uno de los siguientes comandos")
    action = input("Comandos: \n c - Agregar un candidato \n l - lista de candidatos \n v - votar por un candidato \n r - Recuento de votos \n s - salir del sistema ( se borraran los datos) \n").lower()

    # Comprobar la accion del usuario
    if action == "c":
        box.countVotes();
    elif action == "v":
        vote = input("Ingresa el candidato por el cual quieres votar: ").lower()

         # Comprobar que el candidato se encuentre en la lista
        if vote in box.showCandidates():
            box.vote(vote)
            print("Voto registrado!")
        else:
            print("El candidato no se encuentra en la lista. Inténtalo de nuevo.")
    
    if action == "c":
        newCandidate = input("Ingrese el nombre del candidato: ").lower()
        box.addCandidat(newCandidate)
        print('Candidato agregado con exito')
    elif action == "s":
        # Preguntar al usuario si esta seguro de salir del sistema
        confirmation = input("seguro que quieres salir del sistema? s/n \n").lower()
        if confirmation == "s":
            print("Gracias por usar el sistema! \nHecho por: Roberto Ochoa Cuevas con amor <3")
            break
    elif action == "r":
        box.countVotes()
    elif action == "l":
        print(box.showCandidates())
        