$(document).ready(function() {
  $('.sms').click(function(){
    $('.message').show();
    $('.dialog').show();
    //$(.'message').css('display','block');
            /*$('.dial').each(function(){
                this.style.display = 'none';
            });
            $('.dialcreate').each(function(){
                this.style.display = 'none';
            });
            var id = $($(this).data('dialogid'));
            id.css('display','block');
            id.load($(this).data('dialogload'));
            $($(this).data('dialogcreate')).css('display', 'block');
            $($(this).data('dialogcreate')).load($(this).data('dialogformload'));
            messageid = $(this).data('dialog');
            return false;*/
    });

    $('.message').click(function(){
      $('.message').css('display', 'none');
      $('.dialog').css('display', 'none');
    });
});
