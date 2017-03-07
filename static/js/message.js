$(document).ready(function() {
  $('.sms').click(function(){
    var id = $(this).data('chatid');
    $('.message').show();
    $('.dialog').show();
    $('.dialog').load(id);
    $('.dialog').scrollIntoView(true);
    });

    $('.message').click(function(){
      $('.message').css('display', 'none');
      $('.dialog').css('display', 'none');
    });

    $(document).on('submit', '.ajax-form', function(){
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function(data){
            form.html(data);
        })
        return false;
      });
});
