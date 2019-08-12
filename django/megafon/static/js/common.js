$(document).ready(function () {
  function getForm(url, func) {
    req = $.ajax({
      method: 'GET',
      url: url,
      dataType: 'html',
      success: function (result) {
        func(result);
      }
    });
  }
  var set_result_form = function setResult(result){
    $('#forms_result').empty();
    $('#forms_result').html(result);
    $('.close').click(function(e){
        e.preventDefault();
        $('#forms_result').empty();
    });
  };
  var ajax_result = function ajaxResult(result){
    $('#ajax_result').html(result);
  };
  $("*[data-action='getForm']").unbind().each(function(){
      $(this).click(function(e){
        e.preventDefault();
        url = $(this).attr('href');
        getForm(url, set_result_form);
      });
  });
  window.search = function search(value, id){
    var url = '/' + id + '/?search=' + value;
    getForm(url, ajax_result);
  };
});
