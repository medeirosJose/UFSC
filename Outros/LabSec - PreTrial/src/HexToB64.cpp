/*
---
The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

! Cryptopals Rule !
! Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
----

A ideia do programa, basicamente, eh converter uma string em Hex -> bytes -> base64.
Base64 eh um sistema de codificacao que usa 64 caracteres
*/

#include "../include/HexToB64.h"

// caracteres possiveis de base64:
const std::string base64_chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789+/";

// Funcao que converte uma string em Hex para uma string em bytes:
std::vector<char> HexToBytes(const std::string &hex)
{
    // declara um vetor de chars que recebera os bytes:
    std::vector<char> bytes;

    // Loop que percorre a string em Hex e converte para bytes:
    for (int i = 0; i < hex.length(); i += 2)
    {
        // pega dois caracteres da string em Hex:
        std::string byteString = hex.substr(i, 2);
        // converte os dois caracteres para um byte:
        char byte = (char)strtol(byteString.c_str(), NULL, 16);
        // adiciona o byte ao vetor de bytes:
        bytes.push_back(byte);
    }

    return bytes;
}

// Funcao que converte uma string em bytes para uma string em Base64:
std::string BytesToBase64(const std::vector<char> &bytes)
{
    std::string base64;

    int size = bytes.size();
    int i = 0;

    // Loop que percorre o vetor de bytes e converte para base64:
    while (i < size)
    {
        // pega o primeiro byte e desloca 2 bits para a direita:
        char char1 = bytes[i] >> 2;
        // pega os 2 ultimos bits do primeiro byte e desloca 4 bits para a esquerda:
        char char2 = ((bytes[i] & 0x3) << 4) | (bytes[i + 1] >> 4);
        // pega os 4 ultimos bits do segundo byte e desloca 2 bits para a esquerda:
        char char3 = ((bytes[i + 1] & 0xf) << 2) | (bytes[i + 2] >> 6);
        // pega os 6 ultimos bits do terceiro byte:
        char char4 = bytes[i + 2] & 0x3f;

        // adiciona os caracteres ao string em base64:
        base64 += base64_chars[char1];
        base64 += base64_chars[char2];

        if (i + 1 < size)
        {
            base64 += base64_chars[char3];
        }
        else
        {
            base64 += '=';
        }

        if (i + 2 < size)
        {
            base64 += base64_chars[char4];
        }
        else
        {
            base64 += '=';
        }

        i += 3;
    }

    return base64;
}

int resolveC1()
{
    // string em Hex do desafio:
    std::string hexString;
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

    // Converte a string em Hex para uma string em bytes:
    std::vector<char> bytes = HexToBytes(hexString);

    // Converte a string em bytes para uma string em base64:
    std::string base64 = BytesToBase64(bytes);

    // std::cout << "tamanho da string original em Hex: " << hexString.length() << std::endl;
    // std::cout << "tamanho da string convertida em base64: " << base64.length() << std::endl;

    // Printa a string convertida p/ base64:
    std::cout << ""
              << base64 << std::endl
              << std::endl;

    return 0;
}