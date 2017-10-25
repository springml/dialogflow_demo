$(document).ready(function(){
	jQuery('input[type=checkbox]').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green',
        increaseArea: '20%' // optional
    });

	$("#select_document").change(function(){
		$('.extract_fields').attr('disabled',false);
		$('.extract_fields').css('cursor','pointer');
		$('.extract_fields').css('opacity','1');
		var document = $(this).val();
		//Hide extracyed fields on change
		$(".extracted_fields").css('display','none');
		if(document != 'select'){
			if (document == 'legal') {
				$(".legal").css({'display':'block'});
				$(".invoice, .resume").css('display','none');
				$(".extract_fields").css('display','block').addClass('legal_info_btn').removeClass('invoice_info_btn resume_info_btn');
			}else if (document == 'invoice') {
				$(".invoice").css('display','block');
				$(".legal, .resume").css('display','none');
				$(".extract_fields").css('display','block').addClass('invoice_info_btn').removeClass('legal_info_btn resume_info_btn');
			}else if (document == 'resume') {
				$(".resume").css('display','block');
				$(".legal, .invoice").css('display','none');
				$(".extract_fields").css('display','block').addClass('resume_info_btn').removeClass('legal_info_btn invoice_info_btn');
			}
		}
	});

	$(".extract_fields").click(function(){
		//Disable the button after clicked
		$(this).attr('disabled',true);
		$(this).css('cursor','not-allowed');
		$(this).css('opacity','0.3');
		$('.pace').css('display','block');
		setTimeout(function(){ 
			$('.pace').css('display','none');
			$(".extracted_fields").css('display','block');
			if ( $(".extract_fields").hasClass('legal_info_btn') ) {
				$(".legal_extracted_fields").css({'display':'block','border':'1px solid #e1e1e3','height':'auto','overflow':'auto','background-color':'#FFFFFF','border-radius':'2%'});
				$(".invoice_extracted_fields, .resume_extracted_fields").css('display','none');
			}else if ( $(".extract_fields").hasClass('invoice_info_btn') ) {
				$(".legal_extracted_fields, .resume_extracted_fields").css('display','none');
				$(".invoice_extracted_fields").css({'display':'block','border':'1px solid #e1e1e3','height':'auto','overflow':'auto','background-color':'#FFFFFF','border-radius':'2%'});
			}else if ( $(".extract_fields").hasClass('resume_info_btn') ) {
				$(".legal_extracted_fields, .invoice_extracted_fields").css('display','none');
				$(".resume_extracted_fields").css({'display':'block','border':'1px solid #e1e1e3','height':'auto','overflow':'auto','background-color':'#FFFFFF','border-radius':'2%'});
			}
		}, 3000);
	});

	$('.save_fields').click(function(){
		location.href = './success.html';
	});
});