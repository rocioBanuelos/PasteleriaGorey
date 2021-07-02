
const getBuy = (id, total) => {

    $.ajax({
        data: {},
        url: `api/loadBuy/${id}`,
        type: "get",
        success:  function (response) {
            
            $('.modal').fadeIn();
            $('#total').text(total);
            const titles = `<div class="item title">
                                <span class="name">Producto</span>
                                <span class="price">Precio</span>
                                <span class="quantity">Cantidad</span>
                                <span class="subtotal">Subtotal</span>
                            </div>`;

            $('#buyItems').html(titles);

            let items = ``;
            for(i in response.buyItems){
                let itemAux = response.buyItems[i];

                items += `<div class="item">
                            <span class="name">${itemAux.name}</span>
                            <span class="price">$ ${itemAux.price}</span>
                            <span class="quantity">${itemAux.quantity}</span>
                            <span class="subtotal">${itemAux.price * itemAux.quantity}</span>
                        </div>`;
            }

            $('#buyItems').append(items);

            $('div').removeClass('actual');
            $(`#item${id}`).addClass('actual');

            $('#deliveredURL').attr('href', `api/setDelivered/${id}`);
        },
        error: function (response) {
        }
    });
};

