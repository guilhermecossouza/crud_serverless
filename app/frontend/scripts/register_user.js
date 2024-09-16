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
        await fetch("http://localhost:3000/dev/user/insert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)
        })
        .then(respose => respose.json())
        .then(data => {
            console.log(data);            
        })
        .catch((erro) => {
            console.error(erro);            
        });
    }else {        
        formAlert.style.display = "block";
    }
});

