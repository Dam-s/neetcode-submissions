class Solution:
    def threeSum(self, liste: List[int]) -> List[List[int]]:
        resultats = []
        deja_vus = set()

        # Créer un dictionnaire qui mappe chaque valeur à ses indices
        valeur_indices = {}
        for idx, val in enumerate(liste):
            if val not in valeur_indices:
                valeur_indices[val] = []
            valeur_indices[val].append(idx)


       


        for i in range(len(liste)):
            for j in range(i + 1, len(liste)):
                cible = -(liste[i] + liste[j])
                
                # Vérifier si la cible existe dans la liste avec un indice différent de i et j
                if cible in valeur_indices:
                    for k in valeur_indices[cible]:
                        if k != i and k != j:
                            sous_liste = sorted([liste[i], liste[j], cible])
                            cle = tuple(sous_liste)
                            
                            if cle not in deja_vus:
                                deja_vus.add(cle)
                                resultats.append(sous_liste)
                            break
        return resultats