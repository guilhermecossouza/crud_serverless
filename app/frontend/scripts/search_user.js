const alertMessage = document.querySelector("#alert-message");
const tableUser = document.querySelector("#table-user");
const btnSearchUsers = document.querySelector("#btn-search-users");
const inputBusca = document.querySelector("#nome-emai");

const getUsers = async (search) => {
    const parameter =  new URLSearchParams({data : search})
    response = await fetch(`http://localhost:3000/dev/user/list/${parameter.toString()}`, {
        method: "GET",
        headers: {
            "Content-Type": "apllication/json"
        }
    }); 

    const data = await response.json()
    
    if (!response.ok) {
        alertMessage.textContent = "";
        alertMessage.textContent = data.message;    
        return;
    }
    const tbody = tableUser.getElementsByTagName("tbody")[0]
    data.dados.forEach((element) => {
       
        const row = document.createElement("tr");

        const cellId = document.createElement("td");
        cellId.textContent = element.idUsuario;
        row.appendChild(cellId);

        const cellNmae = document.createElement("td");
        cellNmae.textContent = element.nome;
        row.appendChild(cellNmae);

        const cellEmail = document.createElement("td");
        cellEmail.textContent = element.email;
        row.appendChild(cellEmail);

        const cellEdit = document.createElement("td");
        cellEdit.setAttribute("class", "text-center")
        const tagIEdit = document.createElement("i");
        tagIEdit.setAttribute("class", "fa-regular fa-pen-to-square icon-edit");
        tagIEdit.setAttribute("data-user", ""+element.idUsuario+"");
        tagIEdit.setAttribute("style", "cursor: pointer;");
        cellEdit.appendChild(tagIEdit)
        row.appendChild(cellEdit)

        const cellDelete = document.createElement("td");
        cellDelete.setAttribute("class", "text-center")
        const tagIDelete = document.createElement("i");
        tagIDelete.setAttribute("class", "fa-solid fa-trash icon-delete");
        tagIDelete.setAttribute("data-user", ""+element.idUsuario+"");
        tagIDelete.setAttribute("style", "cursor: pointer;");
        cellDelete.appendChild(tagIDelete);
        row.appendChild(cellDelete);  
        
        tbody.appendChild(row);
    });
}

getUsers("");

btnSearchUsers.addEventListener("click", async (event) => { 
    const tbody = tableUser.getElementsByTagName("tbody")[0]
    tbody.innerHTML = "";
    if (inputBusca.value.trim() !== "") {        
        getUsers(inputBusca.value.trim());
    }else {
        getUsers("");
    }
});
