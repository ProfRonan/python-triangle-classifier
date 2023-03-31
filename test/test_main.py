"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", side_effect=["1", "1", "1"])
    def test_1_1_1(self, _mock_input):
        """
        Testa se o programa responde "Equilátero"
        quando o usuário digita 1, 1, 1
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["5", "5", "5"])
    def test_5_5_5(self, _mock_input):
        """
        Testa se o programa responde "Equilátero"
        quando o usuário digita 5, 5, 5
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "2", "3"])
    def test_1_2_3(self, _mock_input):
        """
        Testa se o programa responde "Não é um triângulo"
        quando o usuário digita 1, 2, 3
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["3", "2", "1"])
    def test_3_2_1(self, _mock_input):
        """
        Testa se o programa responde "Não é um triângulo"
        quando o usuário digita 3, 2, 1
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["3", "4", "5"])
    def test_3_4_5(self, _mock_input):
        """
        Testa se o programa responde "Escaleno"
        quando o usuário digita 3, 4, 5
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Escaleno", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["5", "4", "3"])
    def test_5_4_3(self, _mock_input):
        """
        Testa se o programa responde "Escaleno"
        quando o usuário digita 5, 4, 3
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Escaleno", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Isósceles", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["3", "3", "5"])
    def test_3_3_5(self, _mock_input):
        """
        Testa se o programa responde "Isósceles"
        quando o usuário digita 3, 3, 5
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["3", "5", "3"])
    def test_3_5_3(self, _mock_input):
        """
        Testa se o programa responde "Isósceles"
        quando o usuário digita 3, 5, 3
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["5", "3", "3"])
    def test_5_3_3(self, _mock_input):
        """
        Testa se o programa responde "Isósceles"
        quando o usuário digita 5, 3, 3
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Isósceles", captured_output.getvalue().strip())
        self.assertNotIn("Não é um triângulo", captured_output.getvalue().strip())
        self.assertNotIn("Equilátero", captured_output.getvalue().strip())
        self.assertNotIn("Escaleno", captured_output.getvalue().strip())
