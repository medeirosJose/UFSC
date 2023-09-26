/*
---
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
Evaluate each output and choose the one with the best score.
----

desafio 3.

tenho que definir algum criterio de pontuacao para cada character
farei isso utilizando a frequencia dos caracteres na lingua inglesa definido pelo site:

https://en.wikipedia.org/wiki/Letter_frequency

ou

https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html

provavelmente seria interessante fazer um dicionario, como os de python
para armazenar as chaves (letras) e os valores (frequencia)

porem, nao existe dicionario em c++ (in-built pelo menos)
pesquisando, descobri que ha algo semelhante: map

https://www.cplusplus.com/reference/map


*/

#include "../include/XORCypher.h"

/* Funcao responsavel por analisar uma string e definir uma pontuacao a ela,
essa pontuacao eh gerada com base na frequencia dos caracteres na lingua inglesa.
Segundo o site https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
*/
double scoreHEX(const std::string &text)
{
    std::map<char, double> mmap = {
        /* Caso nao seja adicionado os espacos entre characteres, o score fica muito baixo
        e o resultado obtido fica diferente do esperado. Eh possivel testar comentando
        a linha 54, perceberemos que a frase correta vai para a 4a posicao. */

        {' ', 0.2},
        {'e', 0.111607},
        {'a', 0.08486},
        {'r', 0.075809},
        {'i', 0.075448},
        {'o', 0.071635},
        {'t', 0.069509},
        {'n', 0.066544},
        {'s', 0.057351},
        {'l', 0.054893},
        {'c', 0.045388},
        {'u', 0.036308},
        {'d', 0.033844},
        {'p', 0.031671},
        {'m', 0.030129},
        {'h', 0.030034},
        {'g', 0.024705},
        {'b', 0.020720},
        {'f', 0.018121},
        {'y', 0.017779},
        {'w', 0.012899},
        {'k', 0.011016},
        {'v', 0.010074},
        {'x', 0.002902},
        {'z', 0.002722},
        {'j', 0.002032},
        {'q', 0.001362}};

    double score = 0.0;

    // deve-se transformar a string em lower
    // para que nao haja problemas com as letras maiusculas
    std::string text_lower = text;
    for (char &c : text_lower)
    {
        c = tolower(c);
    }

    // dentro desse for, ocorre a comparacao entre os caracteres da string e seu respectivo score
    for (char c : text_lower)
    {
        if (mmap.find(c) != mmap.end())
        {
            score += mmap[c];
        }
    }
    return score;
}

// funcao que faz o XOR da string com uma determinada key
std::string XORWithKey(const std::vector<char> &input, char key)
{
    std::string result;
    // loop que percorre a string e faz o XOR com a key recebida
    for (char c : input)
    {
        result += c ^ key;
    }
    return result;
}

// funcao que faz o decypher da string em hex
void XORdecypher(const std::string &HEX)
{
    std::vector<char> byteHEX = HexToBytes(HEX);
    // os valores sao armazenados em um multimap, para que seja possivel ordenar os resultados
    std::multimap<double, std::string> map_results;

    // loop que percorre todos os caracteres possiveis de um byte
    for (int c = 0; c < 256; ++c)
    {
        std::string decodedString = XORWithKey(byteHEX, static_cast<char>(c));
        double score = scoreHEX(decodedString);
        // os resultados sao armazenados no multimap com a chave sendo o score e o valor sendo a string decifrada
        map_results.insert({score, decodedString});
    }

    // o multimap eh ordenado em ordem decrescente de score
    for (auto it = map_results.rbegin(); it != map_results.rend(); ++it)
    {
        // o resultado eh impresso na tela
        // dando um destaque a primeira frase da lista ordenada
        if (it == map_results.rbegin())
        {
            std::cout << "Frase com maior score: " << it->second << " - " << it->first << std::endl
                      << std::endl;
            continue;
        }

        std::cout << it->second << std::endl
                  << std::endl;
    }
}

int resolveC3()
{
    std::string hex_string;
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
    XORdecypher(hex_string);
    return 0;
}