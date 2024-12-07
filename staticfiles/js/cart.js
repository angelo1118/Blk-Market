// pos/static/js/cart.js
function addToCart(productId) {
    fetch(`/add-to-cart/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    }).then(response => {
        if (response.ok) {
            alert("Product added to cart!");
        }
    });
}
