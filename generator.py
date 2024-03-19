import random
import base64

def generate_random_multihash():
    # Generate a random 32-byte (256-bit) multihash
    random_bytes = bytes([random.randint(0, 255) for _ in range(32)])
    return random_bytes

def encode_multihash_to_cid(multihash):
    # Encode the multihash using base32
    encoded_bytes = base64.b32encode(multihash)
    # Trim the padding characters ("====") from the end
    encoded_string = encoded_bytes.decode().rstrip("=")
    # Format the encoded string as an IPFS CID
    ipfs_cid = "bafybei" + encoded_string
    return ipfs_cid

# Generate a random multihash
random_multihash = generate_random_multihash()
# Encode the multihash to an IPFS CID
random_ipfs_cid = encode_multihash_to_cid(random_multihash)

print("Random IPFS v1 CID:", random_ipfs_cid.lower())
