function dropmenu(){
    nav = document.querySelector('nav')
    if(nav.classList.contains('active-menu')){
        nav.classList.remove('active-menu');
    }
    else{
        nav.classList.add('active-menu');
    }
}

let header = document.querySelector(".header")
let dropdown = document.querySelector(".dropdown-content")
window.onscroll = function(){
    if(window.scrollY > 200){
        header.style.background = "rgba(30, 30, 30, 0.8)"
        dropdown.style.background = "rgba(30, 30, 30, 0.8)"
    }
    else{
        header.style.background = "#1e1e1e" 
        dropdown.style.background = "#1e1e1e"         
    }
}