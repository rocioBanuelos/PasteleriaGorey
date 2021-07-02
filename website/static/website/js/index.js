
let cart = [];
let buyTotal = 0;

const addToCart = (id_product, name, price) => {
    let isInCart = false;
    id_product = parseInt(id_product);
    price = parseFloat(price);


    for(item in cart){
        if(parseInt(cart[item].id_product) == id_product){
            cart[item].quantity += 1;
            cart[item].subtotal = cart[item].quantity * cart[item].price;
            isInCart = true;
        }
    }

    if(!isInCart){
        let newItem = {
            id_product: id_product,
            quantity: 1,
            name: name,
            price: price,
            subtotal: price
        }
        document.querySelector(`#product${id_product}Remove`).style.display = 'block';
        cart.push(newItem);
    }
    drawCart();
    toggleCart();
};

const removeFromCart = (id_product) => {
    id_product = parseInt(id_product);

    for(item in cart){
        if(parseInt(cart[item].id_product) == id_product){
            if (cart[item].quantity <= 1){
                cart.splice(item, 1);
                document.querySelector(`#product${id_product}Remove`).style.display = 'none';
            }
            else{
                cart[item].quantity -= 1;
                cart[item].subtotal = cart[item].quantity * cart[item].price;
            }
        }
    }
    toggleCart();
    drawCart();
};

const drawCart = () => {
    let items = `<li> <span class="name">Producto</span> <span class="quantity">Cantidad</span> <span class="subtotal">Subtotal</span> </li>`;
    let total = 0;

    for(i in cart){
        let aux = cart[i];
        items += `<li> <span class="name">${aux.name}</span> <span class="quantity">${aux.quantity}</span> <span class="subtotal">$${aux.subtotal}</span> </li>`;
        total += aux.subtotal;
    }
    buyTotal = total;
    let container = document.querySelector('#list-items');
    container.innerHTML = items;
    let totalContainer = document.querySelector('#total');
    totalContainer.innerHTML = total;
};

const toggleCart = () => {
    if( cart.length > 0){
        document.querySelector('.shopCart').style.display = 'block';
    }
    else {
        document.querySelector('.shopCart').style.display = 'none';
    }
}

const sendCart = (e) => {

    e.preventDefault();

    const email = $('input[name=email]').val();
    const name = $('input[name=name]').val();
    const auth = $('input[name=csrfmiddlewaretoken]').val();
    const url = `api/loadShopCart`;
    $.ajax({
        data: {
                "cart": JSON.stringify(cart),
                "total": buyTotal,
                "email": email,
                "name": name,
                "csrfmiddlewaretoken": auth
            },
        url: url,
        type: "post",
        success:  function (response) {
            $('#clientSearch').fadeOut();
            console.log(response);
            window.location.replace(`resume/${response.IDBuy}`);
        },
        error: function (response) {
        }
    });
};  

$(document).on('submit', '#clientForm', (e) => sendCart(e));

  
  