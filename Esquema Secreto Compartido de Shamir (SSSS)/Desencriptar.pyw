from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Protocol.SecretSharing import Shamir

#a = unhexlify('4133d3e03a460ff5344a26af5f88dd3c')
# a = unhexlify('2199a5727b78c7d26e325bb1ff9ffeaa')
# print(a)
shares = []
# for x in range(2):
#     idx = input("Enter index: ")
#     share = input("Enter share: ")
#     # idx, share = [ in_str.strip(s) for s in in_str.split(",") ]
#     # print(idx)
#     # print(share)
#     print(share)
#     shares.append((idx, unhexlify(share)))
a = unhexlify('8f8e5cbe9ebf9cee28f6f77b7fb1190b')
b = unhexlify('65c4e6e4b8f3b82eb04e77487e706d38')
shares.append((1,a))
shares.append((4,b))
print(shares)
key = Shamir.combine(shares)
print(key)

with open("enc.txt", "rb") as fi:
     nonce, tag = [ fi.read(16) for x in range(2) ]
     cipher = AES.new(key, AES.MODE_EAX, nonce)
     try:
         result = cipher.decrypt(fi.read())
         cipher.verify(tag)
         with open("clear2.txt", "wb") as fo:
             fo.write(result)
     except ValueError:
         print("The shares were incorrect")
