$(document).ready(function(){tbx.heroImages(),tbx.mobileMenu(),tbx.loadMore(),tbx.clipThru(),tbx.scrollEvents(),tbx.map(),tbx.signUp()});var tbx={heroImages:function(){function e(){n.removeClass(r)}function t(e){s.not(e).removeClass(a),i.removeClass(a)}function o(e){m=e.data("name"),e.addClass(a),l.find('[data-name="'+m+'"]').addClass(a)}var s=$(".featured-case-studies li"),n=$(".home-hero"),l=$(".feature-images"),i=$(".feature-image"),a="active",r="initial-load",m=null;s.mouseenter(function(){e(),t($(this)),o($(this))})},mobileMenu:function(){function e(){s.removeClass(a),n.removeClass(l),setTimeout(function(){o.removeClass(i)},500)}function t(e){o.addClass(i),n.addClass(l),s.each(function(){e=$(this),e.addClass(a)})}var o=$(".bleed"),s=o.find("li"),n=$(".menu-button"),l="twist",i="visible out-animation",a="show";n.click(function(){n.hasClass(l)?e():t($(this))}),$(window).on("resize",function(){e()})},loadMore:function(){var e=$(".clients"),t=e.find("button"),o=$(".clients ul"),s="visible",n="Load more",l="Show less";t.click(function(){var e=$(this);o.hasClass(s)?(o.removeClass(s),setTimeout(function(){e.html(n)},900)):(o.addClass(s),setTimeout(function(){e.html(l)},1300))})},scrollEvents:function(){$(window).width()>768&&$(window).on("scroll",function(){var e=$(".about-text"),t=$(".hero-text"),o=$(window).scrollTop(),s="stop";!function(){o>=335?t.addClass(s):t.removeClass(s)}(),function(){o>=465?e.addClass(s):e.removeClass(s)}(),function(){var e=285,t=$(".text-content"),o=Math.abs($(document).scrollTop()+60),e=340;t.length&&(o<=e&&(paddingTop=o),t.css({paddingTop:paddingTop}))}()})},clipThru:function(){$("#tester-unique").clipthru({autoUpdate:!0,autoUpdateInterval:30})},map:function(){function e(){function e(){new google.maps.Marker({position:new google.maps.LatLng(39.950865,(-75.14559)),map:l,title:"PHILADELPHIA",icon:"/static/torchbox/images/pin.png"})}function t(){new google.maps.Marker({position:new google.maps.LatLng(51.858469,(-1.480863)),map:l,title:"Oxford",icon:"/static/torchbox/images/pin.png"})}function o(){new google.maps.Marker({position:new google.maps.LatLng(51.454814,(-2.597802)),map:l,title:"Bristol",icon:"/static/torchbox/images/pin.png"})}var s={zoom:4,scrollwheel:!1,center:new google.maps.LatLng(45,(-30)),styles:[{featureType:"all",elementType:"labels.text.fill",stylers:[{saturation:36},{color:"#000000"},{lightness:40}]},{featureType:"all",elementType:"labels.text.stroke",stylers:[{visibility:"on"},{color:"#000000"},{lightness:16}]},{featureType:"all",elementType:"labels.icon",stylers:[{visibility:"off"}]},{featureType:"administrative",elementType:"geometry.fill",stylers:[{lightness:"69"}]},{featureType:"administrative",elementType:"geometry.stroke",stylers:[{color:"#000000"},{lightness:17},{weight:1.2}]},{featureType:"administrative.country",elementType:"geometry",stylers:[{lightness:"35"}]},{featureType:"administrative.country",elementType:"geometry.fill",stylers:[{lightness:"1"}]},{featureType:"administrative.province",elementType:"geometry.fill",stylers:[{weight:"3.94"},{lightness:"45"}]},{featureType:"landscape",elementType:"geometry",stylers:[{color:"#000000"},{lightness:20}]},{featureType:"poi",elementType:"geometry",stylers:[{color:"#000000"},{lightness:21}]},{featureType:"road.highway",elementType:"geometry.fill",stylers:[{color:"#000000"},{lightness:17}]},{featureType:"road.highway",elementType:"geometry.stroke",stylers:[{color:"#000000"},{lightness:29},{weight:.2}]},{featureType:"road.arterial",elementType:"geometry",stylers:[{color:"#000000"},{lightness:18}]},{featureType:"road.local",elementType:"geometry",stylers:[{color:"#000000"},{lightness:16}]},{featureType:"transit",elementType:"geometry",stylers:[{color:"#000000"},{lightness:19}]},{featureType:"water",elementType:"geometry",stylers:[{color:"#000000"},{lightness:17}]}]},n=document.getElementById("map"),l=new google.maps.Map(n,s);e(),t();var i=l.getZoom();l.addListener("zoom_changed",function(){i>5?t():(t(),o())})}$("#map").length&&google.maps.event.addDomListener(window,"load",e)},signUp:function(){}};