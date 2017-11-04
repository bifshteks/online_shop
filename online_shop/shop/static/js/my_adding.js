$(document).ready(function() {
	// $('.ajax_add_to_cart').click(function(){
	$('#posts_cont').on('click', 'a:not(.added)', function(){
		var this_item_button =$(this);
		$(this).addClass('loading');

		$(this).siblings('a.added_to_cart').css('display', 'inline-block');
		// console.log($(this).closest('a.added_to_cart').html())
// <a id="a_for_ajax_adding_cart" data-url="{% url 'cart_adding' %}" ></a>

		var url = $('#a_for_ajax_adding_cart').data('url');
		var item_id = $(this).data('product_id');
		var data = {};
		data.item_id = item_id;
		var csrf_token = $('#csrf-form [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;


		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				this_item_button.addClass('added');
				this_item_button.removeClass('loading');
				this_item_button.html('Добавлено');
				this_item_button.removeAttr('href')
				this_item_button.off('click');
				console.log('OK')
			},
			error: function(){
				console.log("error");
			}
		});



		return false
	})
})