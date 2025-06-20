function calcularIMC (){
    const pes = document.getElementById("peso").value;
    const alt = document.getElementById("altura").value;
    const imc = pes / (alt**2);
    const resultado = document.getElementById("IMC");
    resultado.innerHTML = "Su IMC es: " + imc.toFixed(2); }