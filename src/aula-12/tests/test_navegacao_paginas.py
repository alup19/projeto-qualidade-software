from pytest_bdd import scenarios, given, when, then

scenarios('../features/navegacao_paginas.feature')


EMAIL = "teste@teste.com"
SENHA = "123"


@given('que o usuário acessa o sistema')
def acessar_sistema(page):

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/login.html'
    )

    page.fill('#loginEmail', EMAIL)

    page.fill('#loginPassword', SENHA)

    page.click('button[type="submit"]')

    page.wait_for_timeout(3000)


@when('acessar a página de favoritos')
def acessar_favoritos(page):

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/profile.html'
    )

    page.wait_for_timeout(2000)


@then('o sistema deve exibir a tela de favoritos')
def validar_favoritos(page):

    assert page.locator('body').is_visible()


@when('acessar a página de pedidos')
def acessar_pedidos(page):

    page.goto(
        'https://local-eats-unisenac.vercel.app/static/orders.html'
    )

    page.wait_for_timeout(2000)


@then('o sistema deve exibir a tela de pedidos')
def validar_pedidos(page):

    assert page.locator('body').is_visible()