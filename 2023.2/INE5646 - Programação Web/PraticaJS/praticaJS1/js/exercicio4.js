//Crie um script no arquivo ./js/exercicio4.js capaz de verificar se dois números estão no 
//intervalo 30..50 ou no intervalo 60..100 inclusive.

//Se o número estiver em algum dos intervalos, é necessário indicar o número e em qual intervalo ele se encontra. 
//Se o número não estiver em nenhum dos intervalos, é necesário dizer que não está em nenhum dos intervalos. 
//Os valores devem ser informados por meio de janelas prompt ao se clicar no botão abaixo e a saída deve ser apresentada no console.

function noIntervalo() {
    let numero = parseInt(window.prompt("Insira um número: "))
    
    if (numero >= 30 && numero <= 50) {
        console.log(""+numero+" está no intervalo [30,50].")
    } else if (numero >= 60 && numero <= 100) {
        console.log(""+numero+" está no intervalo [60,100].")
    } else {
        console.log("O número ["+numero+"] não está em nenhum dos dois intervalos.")
    }
}