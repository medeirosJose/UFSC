function haOnzeDigitos(cpf) {
    //console.log(cpf.length)
    if (cpf.length === 11) {
        return true
    }
    return false
}

function todosOsOnzeDigitosSaoNumeros(cpf) {

    if (cpf.match(/^[0-9]+$/)) {
        return true
    }
    /*if (isNaN(cpf)) {
        return false
    }
    return true*/
    
}

function osOnzeNumerosSaoDiferentes(cpf) {
    let primeiroDigito = cpf[0]
    console.log(primeiroDigito)

    for (let i = 1; i < cpf.length; i++) {
        console.log(cpf[i])
        if (cpf[i] !== primeiroDigito) {
            return true
        }
    
    }
}


function oPrimeiroDigitoVerificadorEhValido(cpf) {
    
}

function oSegundoDigitoVerificadorEhValido(cpf) {
}





//------------------- Não edite abaixo ----------------------------
function validarCPF(validacao, cpf) {
    switch (validacao) {
        case "onzeDigitos": return haOnzeDigitos(cpf)
        case "onzeSaoNumeros": return todosOsOnzeDigitosSaoNumeros(cpf) && validarCPF("onzeDigitos", cpf)
        case "naoSaoTodosIguais": return osOnzeNumerosSaoDiferentes(cpf) && validarCPF("onzeSaoNumeros", cpf)
        case "verificador10": return oPrimeiroDigitoVerificadorEhValido(cpf) && validarCPF("naoSaoTodosIguais", cpf)
        case "verificador11": return oSegundoDigitoVerificadorEhValido(cpf) && validarCPF("verificador10", cpf)

        default:
            console.error(validacao+" é um botão desconhecido...")
            return false
    }
}


function tratadorDeCliqueExercicio9(nomeDoBotao) {
    const cpf = document.getElementById("textCPF").value

    const validacao = (nomeDoBotao === "validade") ? "verificador11": nomeDoBotao
    const valido = validarCPF(validacao, cpf)
    const validoString = valido ? "valido": "inválido"
    const validadeMensagem = "O CPF informado ("+cpf+") é "+ validoString
    console.log(validadeMensagem)

    if (nomeDoBotao !== "validade") {
        let divResultado = document.getElementById(validacao);
        divResultado.textContent = validoString
        divResultado.setAttribute("class", valido ? "divValidadeValido": "divValidadeInvalido")    
    } else {
        window.alert(validadeMensagem)
    }

    
}