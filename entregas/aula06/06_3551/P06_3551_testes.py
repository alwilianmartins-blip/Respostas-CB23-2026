import unittest

from P06_3551_pilha_encadeada import PilhaEncadeada
from P06_3551_fila_encadeada import FilaEncadeada


class TestPilhaEncadeada(unittest.TestCase):

    def test_ordem_lifo(self):
        """push/pop devem seguir ordem LIFO."""
        pilha = PilhaEncadeada()
        pilha.push(1)
        pilha.push(2)
        pilha.push(3)
        self.assertEqual(pilha.pop(), 3)
        self.assertEqual(pilha.pop(), 2)
        self.assertEqual(pilha.pop(), 1)

    def test_pop_em_pilha_vazia_levanta_excecao(self):
        pilha = PilhaEncadeada()
        with self.assertRaises(IndexError):
            pilha.pop()

    def test_topo_em_pilha_vazia_levanta_excecao(self):
        pilha = PilhaEncadeada()
        with self.assertRaises(IndexError):
            pilha.topo()

    def test_len_apos_insercoes_e_remocoes(self):
        pilha = PilhaEncadeada()
        self.assertEqual(len(pilha), 0)
        pilha.push("a")
        pilha.push("b")
        self.assertEqual(len(pilha), 2)
        pilha.pop()
        self.assertEqual(len(pilha), 1)
        pilha.pop()
        self.assertEqual(len(pilha), 0)

    def test_alternancia_de_push_pop(self):
        pilha = PilhaEncadeada()
        pilha.push(1)
        self.assertEqual(pilha.topo(), 1)
        pilha.push(2)
        self.assertEqual(pilha.pop(), 2)
        pilha.push(3)
        self.assertEqual(pilha.pop(), 3)
        self.assertEqual(pilha.pop(), 1)
        self.assertTrue(pilha.esta_vazia())

    def test_tipos_diferentes_incluindo_repetidos_e_none(self):
        pilha = PilhaEncadeada()
        pilha.push(10)
        pilha.push("Texto")
        pilha.push(True)
        pilha.push(None)
        pilha.push(3.1415)
        pilha.push(3.1415)
        pilha.push([1, 2, 3])
        pilha.push({"chave": "valor"})

        self.assertEqual(pilha.pop(), {"chave": "valor"})
        self.assertEqual(pilha.pop(), [1, 2, 3])
        self.assertEqual(pilha.pop(), 3.1415)
        self.assertEqual(pilha.pop(), 3.1415)
        self.assertIsNone(pilha.pop())
        self.assertEqual(pilha.pop(), True)
        self.assertEqual(pilha.pop(), "Texto")
        self.assertEqual(pilha.pop(), 10)
        self.assertTrue(pilha.esta_vazia())


class TestFilaEncadeada(unittest.TestCase):

    def test_ordem_fifo(self):
        fila = FilaEncadeada()
        fila.enfileirar("A")
        fila.enfileirar("B")
        fila.enfileirar("C")
        self.assertEqual(fila.desenfileirar(), "A")
        self.assertEqual(fila.desenfileirar(), "B")
        self.assertEqual(fila.desenfileirar(), "C")

    def test_intercalar_enfileirar_e_desenfileirar(self):
        fila = FilaEncadeada()
        fila.enfileirar(1)
        fila.enfileirar(2)
        self.assertEqual(fila.desenfileirar(), 1)
        fila.enfileirar(3)
        self.assertEqual(fila.frente(), 2)
        self.assertEqual(fila.desenfileirar(), 2)
        self.assertEqual(fila.desenfileirar(), 3)

    def test_esvaziar_e_reusar_mesma_instancia(self):
        fila = FilaEncadeada()
        fila.enfileirar("x")
        fila.desenfileirar()
        self.assertTrue(fila.esta_vazia())

        fila.enfileirar("y")
        fila.enfileirar("z")
        self.assertEqual(fila.desenfileirar(), "y")
        self.assertEqual(fila.desenfileirar(), "z")
        self.assertTrue(fila.esta_vazia())

    def test_desenfileirar_em_fila_vazia_levanta_excecao(self):
        fila = FilaEncadeada()
        with self.assertRaises(IndexError):
            fila.desenfileirar()

    def test_frente_em_fila_vazia_levanta_excecao(self):
        fila = FilaEncadeada()
        with self.assertRaises(IndexError):
            fila.frente()

    def test_len_coerente(self):
        fila = FilaEncadeada()
        self.assertEqual(len(fila), 0)
        fila.enfileirar(1)
        fila.enfileirar(2)
        fila.enfileirar(3)
        self.assertEqual(len(fila), 3)
        fila.desenfileirar()
        self.assertEqual(len(fila), 2)
        fila.desenfileirar()
        fila.desenfileirar()
        self.assertEqual(len(fila), 0)


if __name__ == "__main__":
    unittest.main()