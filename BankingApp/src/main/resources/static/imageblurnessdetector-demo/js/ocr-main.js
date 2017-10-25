$(document).ready(function(){
	jQuery('input[type=checkbox]').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green',
        increaseArea: '20%' // optional
    });

	

	$(".extract_fields").click(function(){
		//Disable the button after clicked
			$('.pace').css('display','block');	

		processImage();
	
		//$(this).attr('disabled',false);
		//$(this).css('cursor','not-allowed');
		//$(this).css('opacity','0.3');
		
		
	});

	
});
