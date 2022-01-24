<script type="text/javascript">
function include(file) { 
  
    var script  = document.createElement('script'); 
    script.src  = file; 
    script.type = 'text/javascript'; 
    script.defer = true; 
    
    document.getElementsByTagName('head').item(0).appendChild(script); 
    
} 

$(function() {
    $(".flexslider").flexslider({
    slideshowSpeed: 5000, //展示时间间隔ms
    animationSpeed: 500, //滚动时间ms
    touch: true //是否支持触屏滑动
  });
}); 
</script>