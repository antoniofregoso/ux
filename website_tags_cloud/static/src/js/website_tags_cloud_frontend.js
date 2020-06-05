odoo.define('website_tag_cloud.tag_cloud', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.TagCloud = publicWidget.Widget.extend({
	jsLibs: [[
        '/website_tag_cloud/static/src/js/jquery.awesomeCloud-0.2.js,
    ]],
	
	
});

});