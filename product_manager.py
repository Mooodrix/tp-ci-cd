class ProductManager:
    def __init__(self):
        # On utilise un dictionnaire pour stocker nos produits en mémoire
        self.products = {}

    def create(self, p_id, nom, description, prix, quantite):
        if p_id in self.products:
            raise ValueError("Un produit avec cet ID existe déjà.")
        self.products[p_id] = {
            "id": p_id,
            "nom": nom,
            "description": description,
            "prix": prix,
            "quantite": quantite
        }
        return self.products[p_id]

    def read(self, p_id):
        return self.products.get(p_id, None)

    def update(self, p_id, prix=None, quantite=None):
        if p_id not in self.products:
            raise ValueError("Produit introuvable.")
        if prix is not None:
            self.products[p_id]["prix"] = prix
        if quantite is not None:
            self.products[p_id]["quantite"] = quantite
        return self.products[p_id]

    def delete(self, p_id):
        if p_id in self.products:
            del self.products[p_id]
            return True
        return False