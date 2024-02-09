jQuery(function($){
    $("#phone").mask("+7 (999) 999-9999");
 });

function ScrollToTarget() {
    var TargetElement = document.getElementById('TargetElement');
    if (TargetElement) {
        TargetElement.scrollIntoView({ behavior: 'smooth' });
    }
}
