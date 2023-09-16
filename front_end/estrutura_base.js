const postClient = async (inputName, inputEmail, inputTelephone) => {
    const formData = new FormData();
    formData.append('nome', inputName);
    formData.append('telefone', inputTelephone);
    formData.append('email', inputEmail);
  
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

const postGuide = async (inputName, inputEmail, inputTelephone, inputTransport) => {
    const formData = new FormData();
    formData.append('nome', inputName);
    formData.append('telefone', inputTelephone);
    formData.append('email', inputEmail);
    formData.append('transporte', inputTransport);
  
    let url = 'http://127.0.0.1:5000/guia';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }

const postPlace = async (inputName, inputPlaceType) => {
    const formData = new FormData();
    formData.append('nome', inputName);
    formData.append('tipo', inputPlaceType);
  
    let url = 'http://127.0.0.1:5000/lugar';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }

const getTrack = async () => {
  let url = 'http://127.0.0.1:5000/passeios';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.passeios.forEach(passeio => insertList(passeio.id, passeio.guia_nome, passeio.lugar_nome, passeio.cliente_nome, passeio.n_estrela))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const postComment = async (inputClientName, inputText, inputTrackIdComment) => {
    const formData = new FormData();
    formData.append('cliente_nome', inputClientName);
    formData.append('passeio_id', inputTrackIdComment);
    formData.append('texto', inputText);
  
    let url = 'http://127.0.0.1:5000/comentario';
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
    let inputName = document.getElementById("newClientName").value;
    let inputEmail = document.getElementById("newClientEmail").value;
    let inputTelephone = document.getElementById("newClientTelephone").value;
  
    if (inputName === '') {
      alert("Escreva o nome de um item!");
    /*} else if (isNaN(inputEmail) || isNaN(inputTelephone)) {
      alert("Quantidade e valor precisam ser números!");*/
    } else {
      /*insertList(inputName, inputEmail, inputTelephone)*/
      postClient(inputName, inputEmail, inputTelephone)
      alert("Cliente adicionado!")
    }
  }

const newGuide = () => {
    let inputName = document.getElementById("newGuideName").value;
    let inputTelephone = document.getElementById("newGuideTelephone").value;
    let inputEmail = document.getElementById("newGuideEmail").value;
    let inputTransport = document.getElementById("newGuideTransport").value;

    if (inputName === '') {
      alert("Escreva o nome de um item!");
    /*} else if (isNaN(inputEmail) || isNaN(inputTelephone)) {
      alert("Quantidade e valor precisam ser números!");*/
    } else {
      /*insertList(inputName, inputEmail, inputTelephone)*/
      postGuide(inputName, inputEmail, inputTelephone, inputTransport)
      alert("Guia adicionado!")
    }
  }

const newPlace = () => {
    let inputName = document.getElementById("newPlaceName").value;
    let inputPlaceType = document.getElementById("newPlaceType").value;
  
    if (inputName === '') {
      alert("Escreva o nome de um lugar!");
    /*} else if (isNaN(inputEmail) || isNaN(inputTelephone)) {
      alert("Quantidade e valor precisam ser números!");*/
    } else {
      /*insertList(inputName, inputPlaceType)*/
      postPlace(inputName, inputPlaceType)
      alert("Lugar adicionado!")
    }
  }

const newComment = () => {
    let inputName = document.getElementById("newClientNameComment").value;
    let inputText = document.getElementById("newText").value;
    let inputTrackIdComment = document.getElementById("newTrackIdComment").value;
  
    if (inputName === '') {
      alert("Escreva um comentario!");
    /*} else if (isNaN(inputEmail) || isNaN(inputTelephone)) {
      alert("Quantidade e valor precisam ser números!");*/
    } else {
      /*insertList(inputName, inputPlaceType)*/
      postComment(inputName, inputText, inputTrackIdComment)
      alert("Comentario adicionado!")
    }
  }

const insertList = (id, guia_nome, lugar_nome, cliente_nome, n_estrela) => {
  var passeio = [id, guia_nome, lugar_nome, cliente_nome, n_estrela]
  var table = document.getElementById('myTable');
  var row = table.insertRow();
  
  for (var i = 0; i < passeio.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = passeio[i];
  }

}