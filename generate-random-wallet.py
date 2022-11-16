import ecdsa
from Crypto.Hash import keccak


private_key=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

private_key_hex = private_key.to_string().hex()
print("It is your private key and keep in secret(Never share to anyone/anywhere): \n" +str(private_key_hex))

public_key = private_key.get_verifying_key().to_string()

public_key_hex = private_key.get_verifying_key().to_string().hex()
print("It is public key. No problem to share: \n"+str(public_key_hex))

public_key_as_bytes = bytes.fromhex(str(public_key_hex))

keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_key_as_bytes)
full_keccak_hash= str(keccak_hash.hexdigest())

wallet_address = full_keccak_hash[24:]

print("Your public wallet address: 0x"+ wallet_address)

