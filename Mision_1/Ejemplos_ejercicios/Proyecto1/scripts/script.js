function mostrartabla() {
    const numero = document.getElementById("numero").value;
    const resultadodiv = document.getElementById("resultado");
    if (numero === "") {
        resultadodiv.innerHTML = "<p class = 'error'> Ingrese un número </p>";
        return;
    }
    /*  */
    /* Tilde invertida permite combinar texto y variables sin usar concatenación */
    let resultado = `<h2> Tabla del ${numero}</h2>`;
    for (let i = 1; i <= 10; i++) {
        resultado += `<p>${numero} x ${i} = ${numero*i} </p>`;
    }
    resultadodiv.innerHTML = resultado;
}