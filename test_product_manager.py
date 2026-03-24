import pytest
from product_manager import ProductManager

def test_create_and_read_product():
    manager = ProductManager()
    # Test de création
    produit = manager.create(1, "Ordinateur", "PC Portable", 1200.50, 10)
    assert produit["nom"] == "Ordinateur"
    
    # Test de lecture
    produit_lu = manager.read(1)
    assert produit_lu["prix"] == 1200.50

def test_update_product():
    manager = ProductManager()
    manager.create(2, "Souris", "Souris sans fil", 25.0, 50)
    
    # On met à jour le prix et la quantité
    produit_maj = manager.update(2, prix=20.0, quantite=45)
    assert produit_maj["prix"] == 20.0
    assert produit_maj["quantite"] == 45

def test_delete_product():
    manager = ProductManager()
    manager.create(3, "Clavier", "Clavier mécanique", 80.0, 15)
    
    # On supprime et on vérifie que la suppression a fonctionné
    resultat = manager.delete(3)
    assert resultat is True
    assert manager.read(3) is None