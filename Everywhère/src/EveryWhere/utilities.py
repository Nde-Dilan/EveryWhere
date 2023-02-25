from src.main.models import HSEreserve, HSE, Client, Proprietaire


def reservation_hse(Client, HSE):
    if not HSE.is_already_occupied:
        return "🥲 Sorry the location is already occupied. You can look for another HSE 👌"
    HSEreserve.objects.create(ClientId=Client, HSEmain=HSE)


def creation_hse(Proprietaire, informations=list()):
    HSE.objects.create(author=Proprietaire,
                       Lieu=informations[0],
                       Prix=informations[1],
                       Date_published=informations[2],
                       is_already_occupied=informations[3],
                       Surface_totale=informations[4])
    pass


def save_proprietaire(informations=list()):
    Proprietaire.objects.create(user=informations[0],
                                tel=informations[1])

    pass


def save_cleint(informations=list()):
    Client.objects.create(user=informations[0],
                          tel=informations[1])
    pass


# Pour un peu plus tard
def recherche_hse(informations=list()):
    pass
