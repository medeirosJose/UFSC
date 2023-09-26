#include <iostream>
#include <string>
#include "../include/HexToB64.h"
#include "../include/FixedXOR.h"
#include "../include/XORCypher.h"
#include "../include/single-charXOR.h"

int main()
{
    int opcao;
    std::cout << "Escolha o challenge a ser executado: " << std::endl;
    std::cout << "1 - Challenge 1 " << std::endl
              << "2 - Challenge 2 " << std::endl
              << "3 - Challenge 3 " << std::endl
              << "4 - Challenge 4 " << std::endl
              << std::endl
              << "0 - Encerrar" << std::endl
              << std::endl;
    std::cin >> opcao;
    while (opcao != 0)
    {

        switch (opcao)
        {
        case 1:
            std::cout << "\nOUTPUT - CH1" << std::endl;
            resolveC1();
            break;
        case 2:
            std::cout << "\nOUTPUT - CH2" << std::endl;
            resolveC2();
            break;
        case 3:
            std::cout << "\nOUTPUT - CH3" << std::endl;
            resolveC3();
            break;
        case 4:
            std::cout << "\nOUTPUT - CH4" << std::endl;
            resolveC4();
            break;
        case 0:
            return 0;
        }
        std::cout << "\nEscolha outro challenge ou 0 para sair." << std::endl;
        std::cin >> opcao;
    }
    return 0;
};