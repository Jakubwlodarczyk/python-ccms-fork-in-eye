/**
 * Created by ika on 23.03.17.
 */
var addForm = document.forms['add-person-form'];
addForm.addEventListener('submit', validateContactData);

function validateContactData(evt) {
  evt.preventDefault();

  if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
        .test(addForm.email.value))) {
    alert("You have entered an invalid email address!");
    addForm.email.focus();
    return false;
  }


  var x = document.forms['add-person-form'].email.value;
  alert('email ' + x + '!');

  contactForm.submit();
}