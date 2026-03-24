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

# --- Mode d'utilisation simple (Démonstration) ---
if __name__ == "__main__":
    print("=== Démarrage de l'application de Gestion de Produits ===")
    app = ProductManager()

    # 1. Création (Create)
    print("\n[+] Ajout d'un produit...")
    produit1 = app.create(101, "Casque Audio", "Casque Bluetooth réducteur de bruit", 199.99, 15)
    print(f"Produit ajouté : {produit1}")

    # 2. Lecture (Read)
    print("\n[?] Recherche du produit 101...")
    recherche = app.read(101)
    print(f"Résultat : {recherche}")

    # 3. Mise à jour (Update)
    print("\n[*] Mise à jour du prix et du stock...")
    app.update(101, prix=179.99, quantite=10)
    print(f"Produit mis à jour : {app.read(101)}")

    # 4. Suppression (Delete)
    print("\n[-] Suppression du produit 101...")
    app.delete(101)
    print(f"Vérification (doit afficher None) : {app.read(101)}")
    print("\n=== Fin de la démonstration ===")