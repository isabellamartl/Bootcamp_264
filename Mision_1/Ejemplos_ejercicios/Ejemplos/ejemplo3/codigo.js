     function mostraralerta() {
            alert('Hizo click')
        }
        function hacerclick(){
            document.getElementsByTagName("p")[0].onclick = mostraralerta;
        }
        window.onload = hacerclick;