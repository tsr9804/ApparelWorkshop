// Drop down details menu on click

$(document).ready(function(){
      $('.item, details-btn').click(function(){
        $('.details-dropdown', this).slideToggle("slow,");
        if ($(this).find(".details-btn").text() == 'View Details'){
        	$(this).find(".details-btn").text('Hide Details');	
        } else{
        	$(this).find(".details-btn").text('View Details');
        }
      });
    });

$(document).ready(function(){
      $( ".btn" ).click(function( event ) {
  		  event.stopPropagation();
		});
    });