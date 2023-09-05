//Crie um script que receba uma string (através de um prompt) como entrada e mostre a string invertida no console. 
//Coloque seu script no arquivo ./js/exercicio6.js. Note que será necessário atualizar o evento onclick do botão abaixo.

function inverterString() {
    let texto = window.prompt("Insira um texto: ")
    let textoInvertido = ""
    for (let i = texto.length - 1; i >= 0; i--) {
        textoInvertido += texto[i]
    }
    console.log(textoInvertido)
    // alert(textoInvertido)
}