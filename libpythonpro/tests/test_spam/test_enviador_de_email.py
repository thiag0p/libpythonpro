import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['thiagop.oceano@gmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'thiago_franca_1@hotmail.com',
        'Curso Python Pro',
        'Teste de envio automatico de e-mail')
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['teste1', 'teste2']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'thiago_franca_1@hotmail.com',
            'Curso Python Pro',
            'Teste de envio automatico de e-mail'
        )
