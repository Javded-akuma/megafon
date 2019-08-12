$(document).ready(function () {
  function getForm(url) {
    req = $.ajax({
      method: 'GET',
      url: url,
      dataType: 'html',
      success: function (result) {
        $('#forms_result').empty();
        $('#forms_result').html(result);
        $('.close').click(function(e){
            e.preventDefault();
            $('#forms_result').empty();
        });
      }
    });
  }
  $("*[data-action='getForm']").each(function(){
      $(this).click(function(e){
        e.preventDefault();
        url = $(this).attr('href');
        getForm(url);
      });
  });
});
