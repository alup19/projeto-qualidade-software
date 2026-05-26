Feature: Navegação entre páginas

  Scenario: Navegar para favoritos
    Given que o usuário acessa o sistema
    When acessar a página de favoritos
    Then o sistema deve exibir a tela de favoritos

  Scenario: Navegar para pedidos
    Given que o usuário acessa o sistema
    When acessar a página de pedidos
    Then o sistema deve exibir a tela de pedidos