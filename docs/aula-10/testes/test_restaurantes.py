from pages.restaurantes_page import RestaurantesPage

def test_visualizar_restaurante(page):
    restaurante = RestaurantesPage(page)

    restaurante.acessar()

    assert "local-eats" in page.url