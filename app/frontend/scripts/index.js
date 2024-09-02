"use strict"

const alert_error = document.querySelector("#message-error");
alert_error.textContent = "Campos de nome e e-mail são obrigatórios e o e-mail tem que ser válido.";
alert_error.style.display = "none";

const user_add = {}

const search_users = async () => {
    try {
        await fetch("http://localhost:3000/dev/user/list", {
            method: "GET",
            headers: {
                "Content-Type": "Application/json"
            }
        }).then(
            response => response.json()
        ).then(data => {
            const data_user = data[0]
            if(data_user.dadosError[0].error) {
                alert_error.innerHTML = ""
                alert_error.textContent = data_user.dadosError[0].message
                alert_error.style.display = "block";    
            }else {
                const table_body = document.getElementById("table-users").querySelector("tbody");
                data_user.dadosUsuario.forEach((element, indece) => {
                   
                    const row = document.createElement("tr"); 

                    const cell_qtd = document.createElement("td");
                    cell_qtd.textContent = indece + 1;

                    const cell_name = document.createElement("td");
                    cell_name.textContent = element.nome;

                    const cell_email = document.createElement("td");
                    cell_email.textContent = element.email;

                    const cell_edit = document.createElement("td");
                    const cell_edit_icon = document.createElement("i")
                    cell_edit_icon.setAttribute("class", "fa-regular fa-pen-to-square cls-edit")
                    cell_edit_icon.setAttribute("data-idUsuaro", ""+element.Id+"")
                    cell_edit.appendChild(cell_edit_icon)

                    const cell_delete = document.createElement("td");
                    const cell_delete_icon = document.createElement("i")
                    cell_delete_icon.setAttribute("class", "fa-solid fa-trash cls-delete")
                    cell_delete_icon.setAttribute("data-idUsuaro", ""+element.Id+"")
                    cell_delete.appendChild(cell_delete_icon)

                    row.appendChild(cell_qtd)
                    row.appendChild(cell_name)
                    row.appendChild(cell_email)
                    row.appendChild(cell_edit)
                    row.appendChild(cell_delete)
                    table_body.appendChild(row);
                });
            }
            
        }).catch((error) => {
            console.log(error);
        });        
    } catch (error) {
        console.error(error)
    }    
}

search_users();

const valid_email = (email) => {
    const regex = /^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i
    return regex.test(email)
}

const insert_user = async (object_user) => {
    await fetch("http://localhost:3000/dev/user/insert/", {
        method: "POST",
        headers: {
            "Content-Type": "Applicatio/json"
        },
        body: JSON.stringify(object_user)
    }).then(
        response => response.json()
    ).then(data => {
        console.log(data)
    }).catch((error) => {
        console.log(error)
    });
}

document.querySelector("#btn-insert-user").addEventListener("click", (event) => {      
    alert_error.style.display = "none";  
    const input_nome = document.querySelector("#nome").value.trim();
    const input_email = document.querySelector("#email").value.trim();
    if (input_nome === "" && input_email === "" && !valid_email(input_email)) {
        alert_error.style.display = "block";
        event.preventDefault();
    }else {
        user_add.nome =  input_nome;
        user_add.email = input_email;
        insert_user(user_add);
    }    
});