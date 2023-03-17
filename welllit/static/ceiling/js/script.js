function open_qab(number){
    parent=document.getElementById('quest-answ-block-btn-' + number).parentElement
    icon=document.getElementById('quest-answ-block-btn-' + number).lastElementChild
    if(parent.classList.contains('opend-block')){
        parent.classList.remove('opend-block');
        parent.classList.add('closed-block');
        icon.style.transform = 'rotate('+0+'deg)'
    }
    else{
        parent.classList.remove('closed-block')
        parent.classList.add('opend-block');
        icon.style.transform = 'rotate('+90+'deg)'
    }
}