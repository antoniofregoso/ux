odoo.define('website_lateral_menu.website_lateral_menu', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.MenuFloatingButton = publicWidget.Widget.extend({
	selector: '#container-wolf',
	events: {
		 'click #nav-wolf': '_wolfNav',
		 'click #nav-wolf': '_wolfNav',
	 },
	 
	 _wolfNav: function (e) {
			if($('#nav-wolf').hasClass('dock-wolf')){
				$('#nav-wolf').addClass('over-wolf');
				$('#logo-wolf').addClass('logo-wolf');
				$('#logo-wolf-big').removeClass('logo-wolf');
				$('.nav-wolf').animate({
					width: '190px'
				}, 500);
				$('#nav-wolf').removeClass('dock-wolf');		
			} else {
				$('#nav-wolf').removeClass('over-wolf');
				$('#logo-wolf').removeClass('logo-wolf');
				$('#logo-wolf-big').addClass('logo-wolf');
				$('.nav-wolf').animate({
					width: '70px'
				}, 500);
				$('#nav-wolf').addClass('dock-wolf');
			}
	 }
	 
});
});


