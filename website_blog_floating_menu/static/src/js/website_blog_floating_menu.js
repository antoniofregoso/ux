odoo.define('website_blog_floating_menu.website_blog_floating_menu', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.BlogFloatingButton = publicWidget.Widget.extend({
	selector: '.st-blog-menuContainer',
	events: {
		 'click .st-blog-button-main': '_openPanel',
		 'click .st-blog-panel': '_boxClick',
		 'click .st-blog-modal': '_modalClick',
	 },

	start: function () {
		 var def = this._super.apply(this, arguments);
		 this._clicks = 0;
		 this._mainBtn = $(".st-blog-button-main")
	},
	
	_launchPanelAnim: function () {
		$(".st-blog-modal").fadeIn("300");
		 $(".st-blog-panel").animate({
		        opacity: "toggle",
		        height: "toggle"
		      }, 600);
	},
	
	_closePanelAnim: function () {
		$(".st-blog-modal").fadeOut("300");
		 $(".st-blog-panel").animate({
		        opacity: "hide",
		        height: "hide"
		      }, 200);
	},

	_openPanel: function (e) {
	      if (this._clicks === 0) {
	    	  this._mainBtn.removeClass('rotateBackward').toggleClass('rotateForward');  
	          this._launchPanelAnim();
	          this._clicks++;
	        } else {
	        	this._mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
	          this._closePanelAnim();
	          this._clicks--;
	        }
	        e.preventDefault();
	        return false;
		
	},
	
	_boxClick: function (e) {
	      e.stopPropagation();	
	},
	
	_modalClick: function (e) {
		this._closePanelAnim();
	      if (this._clicks === 1) {
	    	  this._mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
	        }
	      this._clicks = 0;
	    },
	
});
});