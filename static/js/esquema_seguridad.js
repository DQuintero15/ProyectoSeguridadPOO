$(document).ready(function () {
  $(".card-body").each(function () {
    var $militar = $(this);
    $militar.on("click", ".btn-primary", function () {
      var id = $militar.find(".id").text().trim();
      // Change modal valuew onclick primary btn
      $(".modal-body #id_militar").val(id).change();
    });
  });
});
