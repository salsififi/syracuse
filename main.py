def syracuse(x):
    print(f"En partant de {x}, ", end="")
    nb_etapes = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        nb_etapes += 1
    print(f"il faut {nb_etapes} étapes pour arriver à 1.")
    return nb_etapes

# TODO: mettre sur Github

def main():
    nb_max = int(input("Jusqu'à quel entier voulez-vous tester la conjecture de Syracuse ? "))
    nb = 1
    etapes = [0]
    while nb < nb_max:
        nb_etapes = syracuse(nb)
        etapes.append(nb_etapes)
        nb += 1

    # Recherche du maximum
    maximum = 1
    the_nb = 1
    for nb_depart, nb_etapes in enumerate(etapes):
        if nb_etapes > maximum:
            maximum = nb_etapes
            the_nb = nb_depart
    print(f"Nombre d'étapes maximum: {maximum}, en partant du nombre {the_nb}.")


if __name__ == "__main__":
    main()
