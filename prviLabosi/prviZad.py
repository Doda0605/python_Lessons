def total_euro(h_placa, radni_sati):
    ukupno = h_placa * radni_sati
    print("Ukupno: ", ukupno, "eura")


radni_sati = int(input())
h_placa = int(input())

total_euro(h_placa, radni_sati)
