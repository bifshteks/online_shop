jQuery(document).ready(function ($) {

    var $div = $("#cscf");

    var $form = $div.find("#frmCSCF");

    $form.find("#recaptcha_response_field").focus(function () {

        $errele = $form.find("div[for='cscf_recaptcha']");
        $errele.html('');

    });

    $form.validate({

        errorElement: "span",

        highlight: function (label, errorClass, validClass) {
            $(label).closest('.form-group').removeClass('has-success').addClass('has-error');
            $(label).closest('.control-group').removeClass('success').addClass('error'); // support for bootstrap 2

        },
        unhighlight: function (label, errorClass, validClass) {
            $(label).closest('.form-group').removeClass('has-error').addClass('has-success');
            $(label).closest('.control-group').removeClass('error').addClass('success'); // support for bootstrap 2
        }
    });
    console.log('3');
    $form.submit(function (event) {
        console.log('1');
        event.preventDefault();
        console.log('2');
        if ($form.validate().valid()) {

            $button = $(this).find("#cscf_SubmitButton");
            $button.attr("disabled", "disabled");
console.log('21');
            $.ajax({
                type: "post",
                dataType: "json",
                cache: false,
                url: cscfvars.ajaxurl,
                data: $($form).serialize(),
                success: function (response) {
                    console.log(response);
                    if (response.valid === true) {
                        console.log('22');
                        //show sent message div
                        $formdiv = $div.find(".cscfForm");
                        $formdiv.css('display', 'none');
                        $messagediv = $div.find(".cscfMessageSent");
                        if (response.sent === false) {
                            $messagediv = $div.find(".cscfMessageNotSent");
                            console.log('24');
                        }
console.log('23');
                        $messagediv.css('display', 'block');

                        if (isScrolledIntoView($div) == false) {
                            jQuery('html,body')
                                .animate({
                                    scrollTop: jQuery($div.selector)
                                        .offset().top
                                }, 'slow');
                                console.log('25');
                        }
                    }

                    else {
                        console.log('else')
                        $.each(response.errorlist, function (name, value) {
                            $errele = $form.find("div[for='cscf_" + name + "']");
                            console.log('26');
                            $errele.html(value);
                            $errele.closest('.form-group').removeClass('has-success').addClass('has-error');
                            $errele.closest('.control-group').removeClass('success').addClass('error'); // support for bootstrap 2
                        });
                        $button.removeAttr("disabled");
                    }
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    if (window.console) {
                        console.log("Status: " + textStatus + "Error: " + errorThrown + "Response: " + XMLHttpRequest.responseText);
                        console.log('28');
                    }
                    $button.removeAttr("disabled");
                    console.log('27');

                }

            });

        }
        ;
    });

});


function isScrolledIntoView(elem) {
    var docViewTop = jQuery(window).scrollTop();
    var docViewBottom = docViewTop + jQuery(window).height();

    var elemTop = jQuery(elem).offset().top;
    var elemBottom = elemTop + jQuery(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}