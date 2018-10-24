document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });


$(document).ready(function(){
	$('.carousel').carousel();
});

$(document).ready(function(){
	$('.sidenav').sidenav();
});

$(document).ready(function(){
 	$('.carousel').carousel({
	 	indicators: true
	 	dist: 0
	 	padding: 0
   	});
});