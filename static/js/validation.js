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
      alert('Theres no such name dupa');
      addForm.fname.focus();
      return false;
    }

  addForm.submit();
}

function process_performance_check_request(data, textStatus, jqXHR) {
  alert("request processed");
} 
 


$(document).ready(function(){
  $('.button-grade').function(){
    console.log($(this));




  });
});
function check_Date_form() {
//  $.ajax("/get_performance")
//   .done(function() {
//     alert( "success" );
//   })
//   .fail(function() {
//     alert( "error" );
//   })
//   .always(function() {
//     alert( "complete" );
//   });
  

  $.ajax({
    type: "POST",
    url: "/get_performance",
    data: 
    var date_form = ,
    success: process_performance_check_request(),
    dataType: dataType
  });
  return alert("You have entered an invalid email address!");
}