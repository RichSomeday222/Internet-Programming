$(function () {
    $("img.zoom").mouseover(
        function () {
            $(".preview").html($("<img>").attr("src", $(this).attr("rel")));
        }
    );
    $("img.zoom").mouseout(
        function () {
            $(".preview").html($("<img>").attr("src", $(this).attr("rel")));
        }
    );
});