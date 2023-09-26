/*
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.
*/

/*
eh basicamente rodar o script do desafio 3, so que varias vezes, para cada uma das 60 strings do arquivo.
*/

#include "../include/single-charXOR.h"

/* funcao que decifra a string em hex e vai imprimindo os resultados na tela
funcao muito semelhante a utilizada no desafio 3, porem agora eh necessario
percorrer todas as keys possiveis*/
std::string XORDecypherResults(const std::string &HEX)
{
    std::vector<char> byteHEX = HexToBytes(HEX);
    std::multimap<double, std::string> map_results;

    // loop que percorre todos os caracteres possiveis de um byte
    for (int c = 0; c < 256; ++c)
    {
        std::string decodedString = XORWithKey(byteHEX, static_cast<char>(c));
        double score = scoreHEX(decodedString);
        // os resultados sao armazenados no multimap com a chave sendo o score e o valor sendo a string decifrada
        map_results.insert({score, decodedString});
        std::cout << "Key " << c << " | "
                  << "Score: " << score << " | " << decodedString << std::endl;
    }

    // retorna a string com maior score
    return map_results.rbegin()->second;
}

int resolveC4()
{
    std::ifstream file("4.txt");
    std::string line;
    std::string result;
    double score = 0.0;
    double max_score = 0.0;
    std::string best_result;

    while (std::getline(file, line))
    {
        result = XORDecypherResults(line);
        score = scoreHEX(result);
        if (score > max_score)
        {
            max_score = score;
            best_result = result;
        }
    }

    std::cout << "\nA frase decifrada com maior score eh: " << best_result;
    std::cout << "O score da frase eh: " << max_score << std::endl
              << std::endl;

    return 0;
}
