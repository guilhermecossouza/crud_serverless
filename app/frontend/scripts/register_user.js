const btnBack = document.querySelector("#btn-back");
const frmUser = document.querySelector("#frm-user");
const formAlert = document.querySelector("#form-alert");
const btnRegister = document.querySelector("#btn-register");
const btnEdit = document.querySelector("#btn-edit");
btnEdit.style.display = "none"

formAlert.style.display = "none";
btnBack.addEventListener("click", (event) => {
    window.location.href = "search_user.html";
});

frmUser.addEventListener("submit", async (event) => {    
    event.preventDefault();
    const nome = document.querySelector("#nome").value.trim();
    const email = document.querySelector("#user-email").value.trim();
    const codUser = document.querySelector("#codUser");
    if (nome !== "" && email !== "" && codUser === null) {   
        const user = {
            nome: nome,
            email: email
        }
        const response = await fetch("http://localhost:3000/dev/user/insert/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)
        });

        const data = await response.json()

        if(!response.ok) {
            formAlert.removeAttribute("class");
            formAlert.setAttribute("class", "alert alert-danger");
            formAlert.textContent = "";
            formAlert.textContent = data.message;
            formAlert.style.display = "block";
            return;
        }
        formAlert.removeAttribute("class");
        formAlert.setAttribute("class", "alert alert-success");
        formAlert.textContent = "";
        formAlert.textContent = data.message;
        formAlert.style.display = "block";        
        return;
    } else if(nome !== "" && email !== "" && codUser !== null) {
        const user = {
            nome: nome,
            email: email,
            idUsuario: codUser.value.trim()
        }
        const parameter =  new URLSearchParams({data : codUser.value.trim()})
        const response = await fetch(`http://localhost:3000/dev/user/edit/${parameter.toString()}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)    
        });

        const data = await response.json() 

        if(!response.ok) {
            formAlert.removeAttribute("class");
            formAlert.setAttribute("class", "alert alert-danger");
            formAlert.textContent = "";
            formAlert.textContent = data.message;
            formAlert.style.display = "block";
            return;
        }

        formAlert.removeAttribute("class");
        formAlert.setAttribute("class", "alert alert-success");
        formAlert.textContent = "";
        formAlert.textContent = data.message;
        formAlert.style.display = "block";        
        return;
        
    }else {        
        formAlert.style.display = "block";
    }
});

const getUser = async (idUser) => {
    const parameter =  new URLSearchParams({data : idUser})
    const response = await fetch(`http://localhost:3000/dev/user/list/${parameter.toString()}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });

    const data = await response.json();
    
    if(!response.ok) {
        formAlert.removeAttribute("class");
        formAlert.setAttribute("class", "alert alert-danger");
        formAlert.textContent = "";
        formAlert.textContent = data.message;
        formAlert.style.display = "block";
        return;    
    }

    if (data.dados.length === 1) {
        const inputName = document.querySelector("#nome");
        const inputEmail = document.querySelector("#user-email");       
        data.dados.forEach((element) => {            
            inputName.value = element.nome
            inputEmail.value = element.email 
            const inputId = document.createElement("input");
            inputId.setAttribute("type", "hidden");
            inputId.setAttribute("name", "codUser");
            inputId.setAttribute("id", "codUser");
            inputId.setAttribute("value", element.idUsuario);      
            frmUser.appendChild(inputId);    
        });
    }
}

const currentUrl = window.location.href;
if(currentUrl.indexOf("?datauser=") > 0) {
    btnRegister.style.display = "none"
    btnEdit.style.display = "block"
    const url = new URL(currentUrl);
    const params = new URLSearchParams(url.search);
    const dataUser = params.get("datauser");
    if(dataUser !== "" && parseInt(dataUser) > 0) {
        getUser(dataUser)    
    }
}



