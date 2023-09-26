
#include "../include/FixedXOR.h"

/*
---
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179
---

o desafio dois faz uso de algumas funcoes do desafio 1

tambem eh necessario fazer uma funcaoXOR que recebe dois vetores de bytes e retorna um vetor de bytes

em seguida eh necessario converter isso em hex para chegar no resultado desejado

*/

// funcao que faz o xor entre os dois vetores de bytes:
std::vector<char> FixedXOR(std::vector<char> &bytes1, std::vector<char> &bytes2)
{
  std::vector<char> result;
  // loop que percorre os dois vetores e faz o xor entre eles
  for (int i = 0; i < bytes1.size(); i++)
  {
    // o resultado eh adicionado ao vetor result
    result.push_back(bytes1[i] ^ bytes2[i]);
  }
  return result;
}

// os caracteres possiveis de hex:
const std::string hex_chars = "0123456789abcdef";

// funcao que converte string xor para hex:
std::string BytesToHex(const std::vector<char> &bytes)
{
  std::string hex;

  for (int i = 0; i < bytes.size(); i++)
  {
    // pega o byte e desloca 4 bits para a direita:
    char byte = bytes[i];
    char nibble1 = (byte & 0xf0) >> 4;
    char nibble2 = byte & 0x0f;

    // adiciona os caracteres ao string em hex:
    hex += hex_chars[nibble1];
    hex += hex_chars[nibble2];
  }

  return hex;
}

int resolveC2()
{
  std::string buffer1, buffer2;

  // os inputs que se deseja fazer o XOR:
  buffer1 = "1c0111001f010100061a024b53535009181c";
  buffer2 = "686974207468652062756c6c277320657965";

  // teste para ver se sao do mesmo tamanho
  try
  {
    if (buffer1.size() != buffer2.size())
    {
      throw -1;
    }
  }
  catch (int e)
  {
    std::cout << "Os inputs devem ser de mesmo tamanho!" << std::endl;
    return 0;
  }

  // sao convertidos em bytes:
  std::vector<char> bytes1 = HexToBytes(buffer1);
  std::vector<char> bytes2 = HexToBytes(buffer2);

  // sao feitos os XORs:
  // se for printar o resultado do vetor, veremos "the kid don't play"
  std::vector<char> result = FixedXOR(bytes1, bytes2);

  // aqui eh feita a conversao da string "the kid don't play" para o hex desejado
  std::string hex = BytesToHex(result);

  std::cout << hex << std::endl;

  return 0;
}