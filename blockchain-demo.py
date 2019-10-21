import hashlib

class Bloco:
    def __init__(self, id, transacoes, hash_anterior):
        self.id = id
        str_transacoes = ",".join([str(transacao) for transacao in transacoes])
        self.nonce = get_nonce(id, str_transacoes, hash_anterior)
        self.transacoes = transacoes
        self.hash_anterior = hash_anterior
        self.hash = get_hash(self.id + self.nonce + str_transacoes + self.hash_anterior)

class Transacao:
    def __init__(self, remetente, destinatario, valor):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
    def __str__(self):
        return self.remetente + " => " + self.destinatario + " : " + self.valor
        
def get_hash(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def get_nonce(id, transacoes, hash_anterior):
    nonce = 0
    while (get_hash(id + str(nonce) + transacoes + hash_anterior)[:4] != "0000"):
        nonce += 1
    return str(nonce)

# Bloco 1
t1 = Transacao("Daniel", "Joao", "5 BTC")
t2 = Transacao("Matheus", "Iago", "1 BTC")
t3 = Transacao("Joaquim", "Jorge", "2 BTC")
b1 = Bloco("1", [t1, t2, t3], "0000000000000000000000000000000000000000000000000000000000000000")

# Bloco 2
t4 = Transacao("Cleiton", "Daniel", "3 BTC")
b2 = Bloco("2", [t4], b1.hash)

# Bloco 3
t5 = Transacao("Erick", "Cleiton", "1 BTC")
t6 = Transacao("Joaquim", "Iago", "5 BTC")
b3 = Bloco("3", [t5, t6], b2.hash)

# Bloco 4
t7 = Transacao("Iago", "Joao", "10 BTC")
t8 = Transacao("Joaquim", "Jorge", "1 BTC")
b4 = Bloco("4", [t7, t8], b3.hash)

print("Bloco: " + b1.id)
print("Nounce: " + b1.nonce)
print("Hash: " + b1.hash)
print("--- Transações ---")
print(*(b1.transacoes), sep = "\n")
print(" ")

print("Bloco: " + b2.id)
print("Nounce: " + b2.nonce)
print("Hash: " + b2.hash)
print("--- Transações ---")
print(*(b2.transacoes), sep = "\n")
print(" ")

print("Bloco: " + b3.id)
print("Nounce: " + b3.nonce)
print("Hash: " + b3.hash)
print("--- Transações ---")
print(*(b3.transacoes), sep = "\n")
print(" ")

print("Bloco: " + b4.id)
print("Nounce: " + b4.nonce)
print("Hash: " + b4.hash)
print("--- Transações ---")
print(*(b4.transacoes), sep = "\n")
print(" ")
