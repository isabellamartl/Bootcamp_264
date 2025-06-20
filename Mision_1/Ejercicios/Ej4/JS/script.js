function cambiarcolor() {
    let color = "#"+ Math.floor(Math.random() * 16777215).toString(16)
    /* Math.random (Libreria de matemáticas para generar números aleatorios entre 0 y 1) */
    /* Math.floor para redondear */

/*     console.log(color); */
    ;
   /*  to string para convertirlo a string */
   document.body.style.backgroundColor = color ;
}