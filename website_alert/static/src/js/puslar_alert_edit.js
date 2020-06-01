odoo.define('website_alert.pulsar_alert.edit', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.PulsarAlertEdit = publicWidget.Widget.extend({

	selector: '#pulsar-alert',
	start: function () {
		$('#pulsar-alert').fadeIn( 3000 );

	},
});

});