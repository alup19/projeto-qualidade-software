Feature: Histórico de pedidos

  Scenario: Visualizar pedidos realizados
    Given que o usuário acessa a página de pedidos
    When visualizar o histórico de transações
    Then o sistema deve exibir os pedidos cadastrados

  Scenario: Validar valor total do pedido
    Given que o usuário acessa a página de pedidos
    When visualizar um pedido realizado
    Then o sistema deve exibir o valor total do pedido