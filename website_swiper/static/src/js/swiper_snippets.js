odoo.define('website_swiper.swiper_snippet', function (require) {
    'use strict';

var publicWidget = require('web.public.widget');

//Cover Flow

publicWidget.registry.swiperCoverFlow = publicWidget.Widget.extend({
    selector: '#swiper-coverflow',

    start: function () {
        var self = this;
        var config = document.getElementById('swiper-coverflow');
        var swiperStyle = {
            effect: 'coverflow',
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            coverflowEffect: {
              rotate: 50,
              stretch: 0,
              depth: 100,
              modifier: 1,
              slideShadows : true,
            }}
      // Navigation
      if (config.dataset.navigation=='True'){
          swiperStyle['navigation']= {
              nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          }
      }    	
      //Pagination
      if (config.dataset.pagination=='numbered'){
          swiperStyle['pagination'] = {
                el: '.swiper-pagination',
                clickable: true,
                renderBullet: function (index, className) {
                return '<span class="' + className + '">' + (index + 1) + '</span>';
              },};    		
      } else if (config.dataset.pagination=='dots') {
          swiperStyle['pagination'] = {
                  el: '.swiper-pagination',
            };
      } else if (config.dataset.pagination=='progress') {
          swiperStyle['pagination'] = {
                  el: '.swiper-pagination',
                  type: 'progressbar',
            };
      } else if (config.dataset.pagination=='fraction') {
          swiperStyle['pagination'] = {
                  el: '.swiper-pagination',
                  type: 'fraction',
            };
      } else if (config.dataset.pagination=='scrollbar') {
          swiperStyle['pagination'] = {
                  el: '.swiper-scrollbar',
                  hide: true,
            };
      }
      
      var swiper = new Swiper(config.dataset.container, 
              swiperStyle);


    },


});

})