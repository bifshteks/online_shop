$(document).ready(function () {
	$('.add-to-cart1').click(function() {
		

		var sbmt_btn = $(this);
		var items_id = sbmt_btn.data('id');
		console.log('qwert')
		console.log(items_id)
		var items_price = sbmt_btn.data('price');
		var items_title = sbmt_btn.data('title');
		var amount = 1


		var form = $('#csrf_form')

		var data = {};
		data.items_id = items_id;
		data.amount = amount;
		var csrf_token = $('#csrf_form [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;


		var url = form.attr("action");

		console.log(data)
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log("OK");

				// console.log(data.products_total_nmb);
				// if (data.products_total_nmb || data.products_total_nmb == 0){
				// 	$('#basket_total_nmb').text("("+data.products_total_nmb+")");
				// 	console.log(data.products);
				$('ul.dropdown-menu.no-padding').html("");
				$.each(data.item, function(k, v){
				$('ul.dropdown-menu.no-padding').append(
					`<li class="mini_cart_item">
						<a title="Remove this item" class="remove" href="#">&#215;</a>
						<a href="#" class="shop-thumbnail">
							<img alt="poster_2_up" class="attachment-shop_thumbnail" src="`+ v.img_url +`">`+ v.title +
						`</a>
						<span class="quantity">` + v.amount + `&#215; <span class="amount">` + v.price_per_item + `P</span></span>
					</li>`



					// '<li>'+ v.title+' x' + v.amount + '</li>'




					);
				});
			// };
			 // $('.your-cart ul').append('<li>' + items_title + ' x' + amount + '</li>');

			},
			error: function(){
				console.log("error");
			}
		});

		return false;
	});
});
