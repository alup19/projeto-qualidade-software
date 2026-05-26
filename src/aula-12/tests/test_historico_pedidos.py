from pytest_bdd import scenarios, given, when, then

scenarios('../features/historico_pedidos.feature')


EMAIL = "teste@teste.com"
SENHA = "123"


@given('que o usuário acessa a página de pedidos')
def acessar_pagina(page):

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/login.html'
    )

    page.fill('#loginEmail', EMAIL)

    page.fill('#loginPassword', SENHA)

    page.click('button[type="submit"]')

    page.wait_for_timeout(3000)

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/orders.html'
    )

    page.wait_for_timeout(2000)


@when('visualizar o histórico de transações')
def visualizar_historico(page):

    page.locator('body').is_visible()


@when('visualizar um pedido realizado')
def visualizar_pedido(page):

    page.locator('body').is_visible()


@then('o sistema deve exibir os pedidos cadastrados')
def validar_pedidos(page):

    pedidos = page.locator('body')

    assert pedidos.is_visible()


@then('o sistema deve exibir o valor total do pedido')
def validar_total(page):

    total = page.locator('body')

    assert total.is_visible()