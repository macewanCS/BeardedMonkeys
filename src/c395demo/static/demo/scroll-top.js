$(document).ready(function () {
    size_tr = $("#ticket-table tr").size();
    x=11;
    if (size_tr <= 11) {
       $('#loadMore').hide();
    }
    else {
       $('#loadMore').show();
    }
    $('#ticket-table tr').hide();
    $('#ticket-table tr:lt('+x+')').show();
         $('#loadMore').click(function () {
             x= (x+10 <= size_tr) ? x+10 : size_tr;
             $('#ticket-table tr:lt('+x+')').show();
             if (x >= size_tr) {
                $('#loadMore').hide();
             }
         });
         
    if ($('#scroll-top').length) {
        var scrollTrigger = 200,
            backToTop = function () {
                var scrollTop = $(window).scrollTop();
                if (scrollTop > scrollTrigger) {
                    $('#scroll-top').addClass('display');
                } else {
                    $('#scroll-top').removeClass('display');
                }
            };
        backToTop();
        $(window).on('scroll', function () {
            backToTop();
        });
        $('#scroll-top').on('click', function (e) {
            e.preventDefault();
            $('html,body').animate({
                scrollTop: 0
            }, 500);
        });
    }
});
