class Calculator:
    def add(self, int_a, int_b):
        """Fonction permettant d'effectuer la somme des paramètres de la méthode seulement si
        les deux paramètres sont des entiers

        Parameters :
        a (int) : premier paramètre de la méthode

        b (int) : deuxieme paramètre de la méthode


        returns :
        int : somme de a et b
        str : message erreur si un paramètre est non entier
        """
        if (isinstance(int_a, int)) & (isinstance(int_b, int)):
            return int_a + int_b
        return "ERROR"


    def subtract(self, int_a, int_b):
        """Fonction permettant d'effectuer la différence des paramètres de la méthode seulement si
        les deux paramètres sont des entiers

        Parameters :
        a (int) : premier paramètre de la méthode

        b (int) : deuxième paramètre de la méthode


        returns :
        int : différence entre a et b
        str : message erreur si un paramètre est non entier
        """
        if (isinstance(int_a, int)) & (isinstance(int_b, int)):
            return int_a - int_b
        return "ERROR"


    def multiply(self, int_a, int_b):
        """Fonction permettant d'effectuer la multiplication des paramètres de la méthode seulement si
        les deux paramètres sont des entiers

        Parameters :
        a (int) : premier paramètre de la méthode
        b (int) : deuxième paramètre de la méthode

        returns :
        int : Le produit de int_a et int_b.
        str : message d'erreur si un paramètre est non entier
        """
        if (isinstance(int_a, int)) & (isinstance(int_b, int)):
            return int_a * int_b
        return "ERROR"

    def divide(self, int_a, int_b):
        """Fonction permettant d'effectuer la division des paramètres de la méhode seulement si
        les deux paramètres sont des entiers et que le deuxieme est non nul

        Parameters :
        a (int) : premier paramètre de la méthode
        b (int) : deuxième paramètre de la méthode

        returns:
        int : La division de a par b
        str : message erreur si un paramètre est non entier ou que le deuxième est nul
        """
        if (isinstance(int_a, int)) & (isinstance(int_b, int)):
            if int_b != 0:
                return int_a / int_b
            return "Impossible de diviser par zéro"
        return "ERROR"
