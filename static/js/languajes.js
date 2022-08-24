var check=document.querySelector(".check")
check.addEventListener('click', idioma)

function idioma(){
    let id=check.checked;
    if (id=true){
        location.href="templates/base.html"
    }else{
        location.href="templates/base_en.html"
    }
}