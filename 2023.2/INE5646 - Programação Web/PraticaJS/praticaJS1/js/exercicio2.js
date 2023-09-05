// atualize esta função para
// exibir um alerta com a hora 
// atual no seguinte formato:
// Horário: 8 PM : 40m : 28s

function tratadorDeCliqueExercicio2() {
    
    let data = new Date()
    let hora = data.getHours()
    let minuto = data.getMinutes()
    let segundo = data.getSeconds()

    if (hora > 12){
        var periodo = "PM"
    }else {
        var periodo = "AM"}
    
    alert("Horário: "+hora+periodo+" : "+minuto+"m : "+segundo+"s")}
