# Decoder Ring
class Decoder:
    first_ring = []
    second_ring = []
    def __init__(self, n):
        self.first_ring = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.first_ring_indexes = {}
        for i in range(len(self.first_ring)):
            self.first_ring_indexes[self.first_ring[i]] = i

        self.second_ring = self.generate_second_ring(n)

    def generate_second_ring(self, n):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        result = []

        index = 0
        while(len(alphabet) > 0):
            index += (n-1)
            index %= len(alphabet)  # Acts like circle

            result.append(alphabet[index])
            alphabet.pop(index)

        return result

    def encrypt(self, word):
        encrypted = ""
        index_offset = 0
        for char in word:
            if(char in self.first_ring_indexes):

                first_ring_index = self.first_ring_indexes[char] # Could use ord to get ASCII code then subtract ord(A)
                second_ring_index = (first_ring_index + index_offset) % 26 # Added modulus after seeing markscheme
                encrypted += self.second_ring[second_ring_index]

            else:
                encrypted += char

            index_offset += 1
            index_offset %= 26

        return encrypted

n = int(input("n: "))
word = input("Word: ")

decoder = Decoder(n)
print("".join(decoder.second_ring[0:6]))
print(decoder.encrypt(word))