function send() {
    const numero = document.getElementById("numero").value;
    const resultadod = document.getElementById("contenido");
    let contenido = `<h2> ¿El número ${numero} es múltiplo de 5?</h2>`;
    let div
    if (numero % 5 === 0) { div = `El número ${numero} es múltiplo de 5`; 
    contenido += `<p> ${div} </p>`}
    else {
        div = `El número ${numero} no es múltiplo de 5`;
        contenido += `<p> ${div} </p>`
    }


    resultadod.innerHTML = contenido;
}
