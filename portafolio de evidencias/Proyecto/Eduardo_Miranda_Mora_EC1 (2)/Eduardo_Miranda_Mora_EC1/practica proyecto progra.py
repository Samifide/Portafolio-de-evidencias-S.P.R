reservas_activas = { "reserva1": {"cliente": "Juan", "monto": 100}, "reserva2": {"cliente": "Maria", "monto": 150}, "reserva3": {"cliente": "Pedro", "monto": 200} }

for reserva, datos in reservas_activas.items():
    print(f"Reserva: {reserva} - Cliente: {datos['cliente']} - Monto: ${datos['monto']}")

reserva_cancelar = "reserva2"

if reserva_cancelar in reservas_activas: 
    monto_reserva = reservas_activas[reserva_cancelar]["monto"] 
    penalidad = monto_reserva * 0.10

    print(f"La penalidad por cancelar la reserva es de ${penalidad}")
    confirmacion = input("¿Desea cancelar la reserva? (s/n): ")

    if confirmacion.lower() == "s":
        del reservas_activas[reserva_cancelar]
        print(f"La reserva {reserva_cancelar} ha sido cancelada")
    else:
        print("La reserva se mantendrá activa")
else: 
    print("La reserva ingresada no existe")
