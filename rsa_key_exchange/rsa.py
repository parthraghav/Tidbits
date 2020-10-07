
from tinyRSA.utils import generate_prime_number, find_coprime, rand_str, mod_inv
import binascii

def generate_keys():
	p = generate_prime_number()
	q = generate_prime_number()
	n = p * q
	t1 = ((p << 1) + (~p))
	t2 = ((q << 1) + (~q))
	t = t1 * t2
	d = find_coprime(t, n)
	e = mod_inv(d, t)
	return (n, e, d)

def encrypt(msg, public_key):
	ba = bytearray(msg, encoding='utf8')
	msg_bin = ''.join(format(char, 'b') for char in ba)
	msg_int = int(msg_bin, 2)
	c = pow(msg_int, public_key[1], public_key[0])
	return c

def decrypt(msg, keypair):
	def bitread(arr, i, chunk_size):
		return chr(int(arr[i*(chunk_size-1):i*(chunk_size-1)+chunk_size-1],2))

	public_key = keypair[:2]
	private_key = keypair[-1]
	decrypted = pow(msg, private_key, public_key[0])
	bitstring = '{0:08b}'.format(decrypted)
	chunk_size = 8
	bytearr = [bitread(bitstring, i, 8) for i in range(len(bitstring)//(chunk_size-1))]
	return ''.join(bytearr)

def twosided_rsa_test(L=None):
	node1 = { 
		'keys': generate_keys(),
		'msg': rand_str(L) if L else 'hello'
	}
	node2 = {
		'keys': generate_keys(),
		'msg': rand_str(L) if L else 'bye'
	}
	# Side 1
	msg12_encrypted = encrypt(node1['msg'], node2['keys'][:2])
	msg12_descrypted = decrypt(msg12_encrypted, node2['keys'])
	assert msg12_descrypted == node1['msg']
	# Side 2
	msg21_encrypted = encrypt(node2['msg'], node1['keys'][:2])
	msg21_descrypted = decrypt(msg21_encrypted, node1['keys'])
	assert msg21_descrypted == node2['msg']

if __name__ == '__main__':
	# generating keys takes time, so be patient
	twosided_rsa_test()


