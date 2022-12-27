document.addEventListener('DOMContentLoaded', function () {
    // if a new comment is added
    document.querySelector("#compose-form").addEventListener("submit", add_comment);

    

});

function add_comment(event) {

    event.preventDefault();

    var commentElement = document.querySelector("#comment");

    var groupId = commentElement.dataset.id;
    var activityId = commentElement.dataset.id2;

    var comment = commentElement.value;

    var activityStatus = document.querySelector("#activity_status");

    var choice = activityStatus.value;

    fetch(`/addComments/${groupId}/${activityId}`, {
        method: 'POST',
        body: JSON.stringify({
            comment: comment,
            choice: choice
        })
    }).then(response => response.json())
        .then(result => {
            console.log(result);

            if(result.result === "comment saved"){
                console.log("working");

                var commentsDiv = document.querySelector(`#activity_comments_${groupId}`);
                console.log(commentsDiv);

                var username = result.user;
                console.log(username);

                if(choice == "yes"){
                    var status = "I am going!!";
                }else{
                    var status = ":( Not going.";
                }
                console.log(status);

                var item = document.createElement("div");
                item.className = `card text-left`;

                item.innerHTML = `
                <h5 class="card-header h5">Member: ${username}</h5>
                <div class="card-body">
                    <p class="lead">${comment}</p>
                    <p class="card-text">${status}</p>
                    
                </div>`;
                
                var br = document.createElement("br");

                if(commentsDiv == null){
                    var commentsMaster = document.querySelector(`#comments_master_${groupId}`);
                    console.log(commentsMaster);
                    commentsMaster.appendChild(item);
                }else{
                    console.log(commentsDiv);
                    commentsDiv.appendChild(br);
                    commentsDiv.appendChild(item);

                }                

                commentElement.value = "";
                
            }
            
        });
    
    
    

}




















