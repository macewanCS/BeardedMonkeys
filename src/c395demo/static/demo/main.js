$(document).ready(function(){
    $( "a[id*='logout']" ).click(function(){
        $("#logoutModal").css("display", "block")
    });
    //for the mobile-view logout button
    $( "a[id*='lit-log']" ).click(function(){
        $("#logoutModal").css("display", "block")
    });
    //resolved/reopen button for view pages
    $( "a[id*='myBtn']" ).click(function(){
        id = $(this).attr('id').replace("myBtn_", "")
        $("#myModal").css("display", "block");
        if ($("#status_"+id).text().indexOf("Open")>=0){
            $("#modalText").html("Are you sure the ticket has been resolved?");
        } else {
                $("#modalText").html("Are you sure that you want to re-open the ticket?");
        }
    });
    //manager's approve and disapprove buttons for view pages
    $( "a[id*='appBtn']" ).click(function(){
        id = $(this).attr('id').replace("appBtn_", "")
        $("#appModal").css("display", "block");
        $("#appModalText").html("Are you sure you wish to approve the ticket?");
    });
    $( "a[id*='disBtn']" ).click(function(){
        id = $(this).attr('id').replace("disBtn_", "")
        $("#disModal").css("display", "block");
        $("#disModalText").html("Are you sure you wish to disapprove the ticket?");
    });
        

//fixing the status bar bug
        //yes buttons for popups (resolve/reopen, approve, disapprove)
        $("#yButton").click(function() {
           $("#myModal").css("display", "none");
           //checking whether ticket status is open to decide which button to display
           if ($("#status_"+id).text().indexOf("Open")>=0){
            alterData(id, "Resolved")
            $("#myBtn_"+id).html('<i class="fa fa-check" aria-hidden="true"></i>Re-open');
            $('.stat').attr('src', '/static/demo/view-ticket/resolved-bar.jpg')
           }
           else {
            alterData(id, "Open")
            $("#myBtn_"+id).html('<i class="fa fa-check" aria-hidden="true"></i>Resolved');
            $('.stat').attr('src', '/static/demo/view-ticket/open-bar.jpg')
           }
        });
        $("#appYButton").click(function() {
            $("#appModal").css("display", "none");
            alterData(id, "Open")
            $('.stat').attr('src', '/static/demo/view-ticket/open-bar.jpg')
            window.location.reload()
        });
        $("#disYButton").click(function() {
            $("#disModal").css("display", "none");
            alterData(id, "Disapproved")
        });
    
    $(".nButton").click(function () {
        $(".modal").css("display", "none");
    });

    $(".close").click(function () {
        $(".modal").css("display", "none");
    });

    $('html').click(function(e) {
       if($(e.target).hasClass('modal') )
       {
           $(".modal").css("display", "none");
       }
    });

//    highlight field
    $("button").click(function(){
        $('input[required]').each(function(){
            if (!$(this).val()) {
               $(this).addClass("required")
            } else {
                $(this).removeClass("required")
            }

       });

       $('textarea[required]').each(function(){
            if (!$(this).val()) {
               $(this).addClass("required")
            } else {
                $(this).removeClass("required")
            }
       });
    });

    function alterData(id, status){
        console.log(id, status)
        console.log(window.location.host)
        $.ajax({
            url : window.location.origin+"/alter-status/", // the endpoint
            type : "POST", // http method
            data : { status : status, id: id }, // data sent with the post request

            // handle a successful response
            success : function(json) {
                $('#status_'+id).html(status); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log('error')
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
});
