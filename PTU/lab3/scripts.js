
function GetPersons() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", 'https://localhost:7225/api/Persons', true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        var data = JSON.parse(xhr.responseText);
        var output = "<ul>";
        for (var i = 0; i < data.length; i++) {
          output += "<li>ID: " + data[i].id + ", Name: " + data[i].firstName + " " + data[i].lastName + "</li>";
        }
        output += "</ul>";
        
        document.getElementById("resultPersons").innerHTML = output;
      }
    };
    xhr.send();
  }


  function GetPersonById(id) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", `https://localhost:7225/api/Persons/${id}`, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4) {
        if (xhr.status == 200) {
          var data = JSON.parse(xhr.responseText);
          var output = "<ul>";
          output += "<li>ID: " + data.id + ", Name: " + data.firstName + " " + data.lastName + "</li>";
          output += "</ul>";
          document.getElementById("resultPerson").innerHTML = output;
        } else {
          document.getElementById("resultPerson").innerHTML = "Person not found";
        }
      }
    };
    xhr.send();
  }
  

  document.getElementById("personForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    var id = document.getElementById("getid").value;
  
    GetPersonById(id);
  });

  function DeletePersonById(id) {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", `https://localhost:7225/api/Persons/${id}`, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4) {
        if (xhr.status == 200) {
            console.log("Person deleted successfully!")
        }
        else{
          console.log("Person delete failed")
        }
      }
    };
    xhr.send();
  }
  

  document.getElementById("deletePersonForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    var id = document.getElementById("delid").value;
  
    DeletePersonById(id);
  });
  

  document.getElementById("addPersonForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    var firstName = document.getElementById("FirstName").value;
    var lastName = document.getElementById("LastName").value;
  
    var person = {
      id: 0,
      FirstName: firstName,
      LastName: lastName
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", `https://localhost:7225/api/Persons`, true);
    xhr.setRequestHeader("Content-Type", "application/json");
  
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          console.log('Person added successfully');
        } else {
          console.error('Failed to add person');
        }
      }
    };
  
    xhr.send(JSON.stringify(person));
  });
  

  