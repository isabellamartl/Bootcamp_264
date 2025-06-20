let num

function multiplicar (){ 
    num= prompt("Ingrese un número")
for (let i= 1; i<=10 ;i++)
    {console.log(num+ "*" + i+ "=" +i*num)}
}

window.onload = multiplicar/* Cuando se inicia la ventana carga esa función */
