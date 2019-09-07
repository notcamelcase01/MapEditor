 {% load static %}
i=0;


$(document).ready(function(){
    var photo = document.getElementById("photo");
var b = document.getElementById("b");
var d = document.getElementById("d");
var c = document.getElementById("c");
var foot = document.getElementById("foot");

TweenMax.from(photo, 4, {width:"0px"});
TweenMax.from(b, 4, {opacity:"0"});
TweenMax.from(c, 4, {opacity:"0"});
TweenMax.from(d, 4, {opacity:"0"});
TweenMax.from(foot,1,{opacity:"0",right:"0",delay:2});
    console.log("dfs");
    setTimeout(function() {
    $('#foot').css({
    right: ''
});
   $('.bg-1').mousemove(function(e){
      var mousePosY = (e.pageY/$(window).height())*100;
      var mousePosX = (e.pageX/$(window).width())*100;
      $('.bg-1').css('background-position-x', mousePosX/20 +'%');
      var mousePosY = (e.pageY/$(window).height())*100;
      $('.bg-1').css('background-position-y', mousePosY/20 +'%');

   });



var $circle = $('.circle'),
    $wrapper = $('.bg-1');

  function moveCircle(e) {
    TweenLite.to($circle, 0.3, {
      css: {
        left: e.pageX,
        top: e.pageY
      }
    });
  }

var flag = false;
$($wrapper).mouseover(function(){
  flag = true;
  TweenLite.to($circle,0.4,{scale:1,autoAlpha:1})
  $($wrapper).on('mousemove', moveCircle);
});
$($wrapper).mouseout(function(){
    flag = false;
    TweenLite.to($circle,0.4,{scale:0.1,autoAlpha:0})
});


$($wrapper).click(function(){
  TweenMax.to($circle,1,{scale:5,opacity:0});
  TweenMax.to($circle,0.4,{scale:1,opacity:1,delay:1});
 // TweenMax.to($circle,.1,{scale:1,opacity1});
});

 },4100);






});

