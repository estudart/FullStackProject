const postItem = async (inputProduct, inputQuantity, inputPrice) => {
    const formData = new FormData();
    formData.append('nome', inputProduct);
    formData.append('telefone', inputQuantity);
    formData.append('email', inputPrice);
  
    let url = 'http://127.0.0.1:5000/cliente';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }

const newClient = () => {
    let inputProduct = document.getElementById("newClientName").value;
    let inputQuantity = document.getElementById("newClientTelephone").value;
    let inputPrice = document.getElementById("newClientEmail").value;
  
    if (inputProduct === '') {
      alert("Escreva o nome de um item!");
    /*} else if (isNaN(inputQuantity) || isNaN(inputPrice)) {
      alert("Quantidade e valor precisam ser números!");*/
    } else {
      /*insertList(inputProduct, inputQuantity, inputPrice)*/
      postItem(inputProduct, inputQuantity, inputPrice)
      alert("Cliente adicionado!")
    }
  }