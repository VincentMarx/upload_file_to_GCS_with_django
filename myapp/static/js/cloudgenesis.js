$(document).ready(function(){
  $("#selectAll").click(function(){
    alert("yy")
    $("#selectFiles").prop("checked", this.prop("checked"));
  });
});