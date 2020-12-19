$(document).ready(function(){
  $('.your-class').slick({
    slidesToScroll: 1,
    autoplay: true
  });
});

$('.lazy').slick({
  lazyLoad: 'ondemand',
  slidesToShow: 3,
  slidesToScroll: 1
});