def crearBaraja(palos):

    baraja = []
    for idx, palo in enumerate(palos):
        for i in range(1, 13):
            # if i == 8 or i == 9
                # continue
            baraja.append(str(i) + palo)

    return baraja
