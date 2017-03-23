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

  if (addForm.fname.value.length < 3 || addForm.lname.value.length < 3) {
      alert('Name is too short!');
      addForm.fname.focus();
      addForm.lname.focus();
      return false;
    }

   if (addForm.fname.value == "dupa" || addForm.fname.value == "Dupa") {
      alert('Seriously?');
      addForm.fname.focus();
      return false;
    }

  addForm.submit();
}