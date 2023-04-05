function get_result(){
    result=0
    width = parseInt(document.getElementById('c-width').value)
    length = parseInt(document.getElementById('c-length').value)
    canvases_price = parseInt(document.getElementById('canvases').value)
    decor_insert = parseInt(document.getElementById('decor-insert').value)
    gordina = parseInt(document.querySelector('input[name="gordina"]:checked').value)
    lights = parseInt(document.getElementById('light').value)
    pipes = parseInt(document.getElementById('pipes').value)

    result=(width/100) * ( length/100) * (canvases_price + 180) + ((width/100) * 2 + ( length/100) * 2) * (decor_insert) + gordina  + lights*500 + pipes*250
    result_field=document.getElementById('calculator-result-field')
    if (result){
        result_field.textContent=result.toFixed(2)
    }
    else{
        result_field.textContent='-'
    }
}