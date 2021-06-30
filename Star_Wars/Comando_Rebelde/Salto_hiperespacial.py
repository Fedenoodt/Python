class Flota_Rebelde_antes():
    cruseroMonCalamari = 75
    fragataNebulonB_1 = 52
    fragataNebulonB_2 = 67
    corbetaCorelliana_1 = 53
    corbetaCorelliana_2 = 33
    corbetaCorelliana_3 = 96
    cruseroMerodeador_1 = 15
    cruseroMerodeador_2 = 56
    saltoHiperespacial = False
    DañodeDestructorEstelar = 20



    def daño(self):
        Flota_Rebelde_antes.cruseroMonCalamari = Flota_Rebelde_antes.cruseroMonCalamari - DañodeDestructorEstelar
        Flota_Rebelde_antes.fragataNebulonB_1 = Flota_Rebelde_antes.fragataNebulonB_1 - DañodeDestructorEstelar
        Flota_Rebelde_antes.corbetaCorelliana_3 = Flota_Rebelde_antes.corbetaCorelliana_3 - DañodeDestructorEstelar
        Flota_Rebelde_antes.cruseroMerodeador_2 = Flota_Rebelde_antes.cruseroMerodeador_2 - DañodeDestructorEstelar

    def saltar(self):
        if Flota_Rebelde_antes.cruseroMonCalamari >= 6 and Flota_Rebelde_antes.fragataNebulonB_1 >= 6 and Flota_Rebelde_antes.fragataNebulonB_2 >= 6 and Flota_Rebelde_antes.corbetaCorelliana_1 >= 6 and Flota_Rebelde_antes.corbetaCorelliana_2 >= 6 and Flota_Rebelde_antes.corbetaCorelliana_3 >= 6 and Flota_Rebelde_antes.cruseroMerodeador_1 >= 6 and Flota_Rebelde_antes.cruseroMerodeador_2 >= 6:
            self.saltoHiperespacial = True

    def estadoSalto(self):
        if(self.saltoHiperespacial):
            return "Todos en la flota han saltado."
        else:
            return "Los motores están fritos, no pudimos saltar."

Flota_Rebelde_despues = Flota_Rebelde_antes

print(Flota_Rebelde_despues.estadoSalto)

print('Motores cruseroMonCalamari al ', Flota_Rebelde_despues.cruseroMonCalamari, 'por ciento.')
print('Motores fragataNebulonB_1 al ', Flota_Rebelde_despues.fragataNebulonB_1, 'por ciento.')
print('Motores fragataNebulonB_2 al ', Flota_Rebelde_despues.fragataNebulonB_2, 'por ciento.')
print('Motores corbetaCorelliana_1 al ', Flota_Rebelde_despues.corbetaCorelliana_1, 'por ciento.')
print('Motores corbetaCorelliana_2 al ', Flota_Rebelde_despues.corbetaCorelliana_2, 'por ciento.')
print('Motores corbetaCorelliana_3 al ', Flota_Rebelde_despues.corbetaCorelliana_3, 'por ciento.')
print('Motores cruseroMerodeador_1 al ', Flota_Rebelde_despues.cruseroMerodeador_1, 'por ciento.')
print('Motores cruseroMerodeador_2 al ', Flota_Rebelde_despues.cruseroMerodeador_2, 'por ciento.')


