$(document).ready(function(){
    console.log("working"); 
    $.ajax({
      url: "/api/candidates/",
      method: "GET",
      success: function(data){
        // console.log(data)
        $.each(data, function(key, value){
            var candidateKey = key;
            var candidate_id_candidate = value.id_candidate;
            var candidatetUser = value.userID;
            $("#candidate-container").append(
                "<div class=\"media\"><div class=\"media-body\">" + tweetContent + "<br/> via " + candidateUser.userID + " | " + "<a href='#'>View</a>" + "</div></div><hr/>"
            )
        })
      },
      error: function(data){
        console.log("error")
        console.log(data)
      }
    })
  });