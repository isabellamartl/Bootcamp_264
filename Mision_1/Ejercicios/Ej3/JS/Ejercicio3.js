function enviar () {
    const n = document.getElementById ("n").value;
    const resultado = document.getElementById ("contenido");
    let contenido = `<h2> Números hasta el ${n}</h2>`;
for (let i = 1; i <= n ; i++) {
    console.log (i)

    contenido += `<p>${i}</p>`;
    
}

resultado.innerHTML = contenido;
}