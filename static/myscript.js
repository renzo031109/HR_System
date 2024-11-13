//Turn on active on active pages when click
document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.classList.add("active");
        link.setAttribute("aria-current", "page");
    }
});


//  Spinner script
$('#spinner').hide();


$('#submitbtn').click(function(){
    $('#spinner').show();
}) 