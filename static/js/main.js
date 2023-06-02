let cep = document.querySelector('.input_cep')
let span = document.querySelector('.span_required')
let btn = document.querySelector('#btn_buscar')

function cep_valido(cep) {
    return !isNaN(cep.value) && cep.value.length === 8
}

cep.oninput = function () {
    if (cep_valido(cep)) {

        span.style.display = 'none'
        btn.disabled = false
        btn.style.cursor = 'pointer'
        btn.style.opacity = '1'

    } else if (cep.value.length < 8) {

        span.innerHTML = 'O CEP deve conter 8 dígitos numéricos'
        span.style.display = 'block'
        btn.disabled = true
        btn.style.cursor = 'not-allowed'
        btn.style.opacity = '0.5'

    } else {

        span.innerHTML = 'O CEP deve conter apenas números'
        span.style.display = 'block'
        btn.disabled = true
        btn.style.cursor = 'not-allowed'
        btn.style.opacity = '0.5'

    }
}