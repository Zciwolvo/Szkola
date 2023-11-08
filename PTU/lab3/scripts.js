
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
        
        document.getElementById("result").innerHTML = output;
      }
    };
    xhr.send();
  }