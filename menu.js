const menu = document.getElementById("menu_hamb");
const navegacion_contenedor = document.getElementById("navegacion_contenedor");
menu.addEventListener("click",()=>{
    navegacion_contenedor.style.flexDirection = "column";
    navegacion_contenedor.style.border = "solid 1px red";
    console.log(navegacion_contenedor)
})