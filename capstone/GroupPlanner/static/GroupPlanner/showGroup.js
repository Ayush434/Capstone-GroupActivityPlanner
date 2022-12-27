document.addEventListener('DOMContentLoaded', function() {
    // if a new member is added
    document.querySelector("#compose-form").addEventListener("submit", add_member);
    
 
  });

  function add_member(event){

    event.preventDefault();
  
    var member = document.querySelector("#member");

    var username = member.value;
    var groupId = member.dataset.id;

    // console.log(username);
    // console.log(username.dataset.id);
    // console.log(username.value);

    fetch('/addNewMember', {
      method: 'POST',
      body: JSON.stringify({
        username: username,
        groupId: groupId
      })
    }).then(response => response.json())
    .then(result => {

      var message = document.querySelector(`#message_${groupId}`);
      console.log(message);


      if(result.result === "user already a member"){
        console.log(result);
        // after adding the member, clear the input field
        var member = document.querySelector("#member");
        // console.log(member);
        member.value = "";

        message.innerHTML = "user already exists";
        message.style.display = "block";
      }

      else if(result.result === "Username is invalid"){
        console.log(result);
        // after adding the member, clear the input field
        var member = document.querySelector("#member");
        // console.log(member);
        member.value = "";

        message.innerHTML = "Username is invalid";
        message.style.display = "block";
      }

      else if(result.result === "failed"){
        console.log(result);
        // after adding the member, clear the input field
        var member = document.querySelector("#member");
        // console.log(member);
        member.value = "";

        
        message.innerHTML = "Failed to find user";
        message.style.display = "block";
      }

      else{

        message.innerHTML = "";
        message.style.display = "none";

        // after adding the member, clear the input field
        var member = document.querySelector("#member");
        // console.log(member);
        member.value = "";

        // now add the member (html dynamically)

        var membersList = document.querySelector(`#members_list_${groupId}`);
        console.log(membersList);


        

        var item = document.createElement("li");
        item.className = `list-group-item text-left`;

        item.innerHTML = `<label class="name">
                        ${username}<br>
                    </label>`;
        
        
        membersList.appendChild(item);
      }
    });
    
    

  }






