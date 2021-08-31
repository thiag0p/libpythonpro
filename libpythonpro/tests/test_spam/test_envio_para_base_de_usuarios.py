from unittest.mock import Mock
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
import pytest
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Thiago', email='thiagop.oceano@gmail.com'),
            Usuario(nome='Luciano', email='luciano@mmail.com')
        ],
        [
            Usuario(nome='Thiago', email='thiagop.oceano@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'thiago_franca_1@hotmail.com',
        'Curso Python Pro',
        'Condia os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Thiago', email='thiagop.oceano@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'thiago_franca_1@hotmail.com',
        'Curso Python Pro',
        'Condia os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'thiago_franca_1@hotmail.com',
        'thiagop.oceano@gmail.com',
        'Curso Python Pro',
        'Condia os módulos fantásticos'
    )
