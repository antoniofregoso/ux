odoo.define('website_lateral_menu.website_lateral_menu', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.MenuLateral = publicWidget.Widget.extend({
	selector: '#container-wolf',
	events: {
		 'mouseover #items-wolf': '_wolfOver',
		 'mouseleave #items-wolf': '_wolfLeave',
	 },
	 
	 _wolfOver: function (e) {
			if($('#nav-wolf').hasClass('dock-wolf')){
				$('#nav-wolf').addClass('over-wolf');
				$('#logo-wolf').addClass('logo-wolf');
				$('#logo-wolf-big').removeClass('logo-wolf');
				$('.nav-wolf').animate({
					width: '220px'
				}, 500);
				$('#nav-wolf').removeClass('dock-wolf');
			} 
	 },
	 
	 _wolfLeave: function (e) {
		 if($('#nav-wolf').hasClass('over-wolf')){
			 $('#nav-wolf').removeClass('over-wolf');
			 $('#logo-wolf').removeClass('logo-wolf');
			 $('#logo-wolf-big').addClass('logo-wolf');
			 $('.nav-wolf').animate({
				width: '70px'
			  }, 250);
			 $('#nav-wolf').addClass('dock-wolf');			 
		 }
	 },
	 
});
});


