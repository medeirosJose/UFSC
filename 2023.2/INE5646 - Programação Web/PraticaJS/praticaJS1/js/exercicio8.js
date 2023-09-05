function obterRegiaoFiscalAtravesDoCPFInformado(cpfInformado) {
    //edite esta função!
    let regiaoFiscal = undefined
    console.log(cpfInformado)

    if (cpfInformado[9] == 0){
        regiaoFiscal = "RS"}

    else if (cpfInformado[9] == 1){
        regiaoFiscal = "DF, GO, MT, MS e TO"
    }
    else if (cpfInformado[9] == 2){
        regiaoFiscal = "AC, AP, AM, PA, RO e RR"
    }
    else if (cpfInformado[9] == 3){
        regiaoFiscal = "CE, MA e PI"
    }
    else if (cpfInformado[9] == 4){
        regiaoFiscal = "AL, PB, PE e RN"
    }
    else if (cpfInformado[9] == 5){
        regiaoFiscal = "BA e SE"
    }
    else if (cpfInformado[9] == 6){
        regiaoFiscal = "MG"
    }
    else if (cpfInformado[9] == 7){
        regiaoFiscal = "ES e RJ"
    }
    else if (cpfInformado[9] == 8){
        regiaoFiscal = "SP"
    }
    else if (cpfInformado[9] == 9){
        regiaoFiscal = "PR e SC"
    }
    
    //----------------------------
    return regiaoFiscal
}



function tratadorDeCliqueExercicio8() {
    let textCPF = document.getElementById("textCPF")
	let textRegiao = document.getElementById("regiaoFiscal")

    const regiaoFiscal = obterRegiaoFiscalAtravesDoCPFInformado(textCPF.value);
    textRegiao.textContent = "Região fiscal: "+regiaoFiscal
}
