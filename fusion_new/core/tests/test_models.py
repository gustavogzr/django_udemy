"""Testes de unidade do módulo models da aplicação core."""
import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path, Servico, Cargo, Funcionario, Recurso

class GetFilePathTestCase(TestCase):
    """Caso de teste para a função get_file_path"""

    def setUp(self):
        """Configurações iniciais para os testes"""
        self.filename = f'{uuid.uuid4()}.png' # cria um nome de arquivo aleatório

    def test_get_file_path(self):
        """Executa o teste do função get_file_path"""
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServicoTestCase(TestCase):
    """Caso de teste para o modelo Servico"""

    def setUp(self):
        """Configurações iniciais para os testes"""
        self.servico = mommy.make('Servico')

    def test_str(self):
        """Testa a representação de um Servico como string"""
        self.assertEqual(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    """Caso de teste para o modelo Cargo"""

    def setUp(self):
        """Configurações iniciais para os testes"""
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        """Testa a representação de um Cargo como string"""
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    """Caso de teste para o modelo Funcionario"""

    def setUp(self):
        """Configurações iniciais para os testes"""
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        """Testa a representação de um Funcionario como string"""
        self.assertEqual(str(self.funcionario), self.funcionario.nome)

class RecursoTestCase(TestCase):
    """Caso de teste para o modelo Recurso"""

    def setUp(self):
        """Configurações iniciais para os testes"""
        self.recurso = mommy.make('Recurso')

    def test_str(self):
        """Testa a representação de um Recurso como string"""
        self.assertEqual(str(self.recurso), self.recurso.recurso)