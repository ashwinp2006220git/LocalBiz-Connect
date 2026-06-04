function showMessage(){
    document.getElementById('Message').textContent="Thank you for visiting LocalBiz Connect";
}
function submitEnquiry(event){
    event.preventDefault();
     const name=document.getElementById("Name").value.trim();
     const email=document.getElementById("Email").value.trim();
     const service=document.getElementById("service").value.trim();
     const message=document.getElementById("message").value.trim();
     const formMessage=document.getElementById("formMessage");
    if(name===""|| email===""||message===""||service===""){
        formMessage.textContent="Please enter all the fields";
        formMessage.style.color="red";
        return;
    }
    formMessage.textContent = "Thank you, " + name + "! Your enquiry has been recorded for the Day 2 demo.";
    formMessage.style.color = "#123c69";
}