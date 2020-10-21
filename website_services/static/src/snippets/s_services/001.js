odoo.define('website_services.s_services.swiper.js', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.servicesSwiper = publicWidget.Widget.extend({
        selector: 'crmb-services-swiper',

        start: function () {
            console.log('Puto');
            var swiper = new Swiper('.crmb-services-container');    
            

        },
    });

})