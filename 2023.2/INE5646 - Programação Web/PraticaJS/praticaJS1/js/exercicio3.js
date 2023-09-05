function stringCortada(){

    let stringInteira = prompt("Palavra: ")
    /*for (let i = 0; i < string.length; i++) {
        console.log(string[i])
    }*/
    
    // parametros de slide: (inicio, fim)
    resultado = stringInteira.slice(1, stringInteira.length - 1)
    
    alert(resultado)

}