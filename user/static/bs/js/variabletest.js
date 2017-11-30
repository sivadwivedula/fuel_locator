function updatePieFact(){
    var data = {'pieFact': pieFact};
    $.post(URL, data, function(response){
        if(response === 'success'){ alert('Yay!'); }
        else{ alert('Error! :('); }
    });
}
$(document).ready(function(){
    $('#bttnMinus').click(function(){
        pieFact *= 0.9;
        updatePieFact();
    });
    $('#bttnPlus').click(function(){
        pieFact *= 1.1;
        updatePieFact();
    });
});