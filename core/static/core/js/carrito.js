var updateBtns = document.getElementsByClassName('update-carrito')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var espacioId = this.dataset.espacio
        var action = this.dataset.action
        console.log('espacioId:', espacioId, 'Action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Usuario no registrado ')
        } else {
            updateReserva(espacioId, action)
        }
    })
}

function updateReserva(espacioId, action){
    console.log('Usuario autenticado, enviando datos')

        var url = '/update_reserva/'

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'espacioId':espacioId, 'action':action})
        })
        .then((response)=> {
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data)
            location.reload()
        });
}