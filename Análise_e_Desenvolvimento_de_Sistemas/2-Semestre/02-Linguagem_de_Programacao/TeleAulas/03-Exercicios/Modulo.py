import Classe

conta1 = Classe.Conta('Marcio', 2)
conta1.Depositar(200.0)
print(conta1.GetCliente())

conta2 = Classe.Conta('Ana', 3)
conta2.Depositar(300.0)

conta1.Transferencia(conta2, 100)

print("O saldo de", conta1.GetCliente(), "é", conta1.Saldo())
print(conta2.Saldo())