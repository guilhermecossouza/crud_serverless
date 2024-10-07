const btnBack = document.querySelector("#btn-back");
const frmUser = document.querySelector("#frm-user");
const formAlert = document.querySelector("#form-alert");
formAlert.style.display = "none";
btnBack.addEventListener("click", (event) => {
    window.location.href = "search_user.html";
});


frmUser.addEventListener("submit", async (event) => {    
    event.preventDefault();
    const nome = document.querySelector("#nome").value.trim();
    const email = document.querySelector("#user-email").value.trim();
    if (nome !== "" && email !== "") {
        const user = {
            nome: nome,
            email: email
        }
        const response = await fetch("http://localhost:3000/dev/user/insert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)
        });

        const data = await response.json()
        console.log(response)
        console.log(data);
        

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

