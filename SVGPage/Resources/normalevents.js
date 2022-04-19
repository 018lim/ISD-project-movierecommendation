//Para cambiar el SVG de los ejemplos
function cambio(element, shape){
  if((shape != 'poligono') && (shape != 'polilinea')){
    $("#"+shape).attr(element.id,element.value);
  }
  else{
    if(element.dataset.shape == 'points1')
      $("#"+shape).attr('points',$("#"+element.dataset.shape).val());
    else
      $("#"+shape).attr(element.dataset.shape,$("#"+element.dataset.shape).val());
  }

  if(shape=='rectangulo')
    $("#"+shape+"_card").html('&#60rect<br/>x="'+$("#"+shape).attr('x')+'"<br/>y="'+$("#"+shape).attr('y')+'"<br/>width="'+$("#"+shape).attr('width')+'"<br/>height="'+$("#"+shape).attr('height')+'"&#62');
  else{
    if(shape=='circulo')
      $("#"+shape+"_card").html('&#60circle<br/>cx="'+$("#"+shape).attr('cx')+'"<br/>cy="'+$("#"+shape).attr('cy')+'"<br/>r="'+$("#"+shape).attr('r')+'"&#62');
    else {
      if(shape=='elipse')
        $("#"+shape+"_card").html('&#60ellipse<br/>cx="'+$("#"+shape).attr('cx')+'"<br/>cy="'+$("#"+shape).attr('cy')+'"<br/>rx="'+$("#"+shape).attr('rx')+'"<br/>ry="'+$("#"+shape).attr('ry')+'"&#62');
      else{
        if(shape=='poligono')
          $("#"+shape+"_card").html('&#60polygon<br/>points="'+$("#"+element.dataset.shape).val()+'"/&#62');
        else {
          if(shape =='linea')
            $("#"+shape+"_card").html('&#60line<br/>x1="'+$("#"+shape).attr('x1')+'"<br/>y1="'+$("#"+shape).attr('y1')+'"<br/>x2="'+$("#"+shape).attr('x2')+'"<br/>y2="'+$("#"+shape).attr('y2')+'"&#62');
          else {
            if(shape =='polilinea')
              $("#"+shape+"_card").html('&#60polygon<br/>points="'+$("#"+element.dataset.shape).val()+'"<br/>fill="none"/&#62');
          }
        }
      }
    }
  }
}

function cambiopath(element, comand){
  if(comand =='M'){//Para el path con "d": moveto
    var moveto = element.dataset.moveto+" "+$("#Mx").val()+" "+$("#My").val();
    var circx = $("#Mx").val();
    var circy = $("#My").val();
    $('svg path.M').attr("d",moveto);
    $('svg circle.M').attr("cx",circx);
    $('svg circle.M').attr("cy",circy);
    $("#"+comand+"_card").html('&#60path d="'+moveto+'"/&#62<br/>&#60circle cx="'+circx+'" cy="'+circy+'" r="2"/&#62');
  }
  if(comand=="L"){
    var lineto = element.dataset.lineto+" "+$("#Lx").val()+" "+$("#Ly").val();
    $("#"+comand+"_card").html('&#60path d="<br/>M 10 10<br/>'+lineto+'"<br/>stroke="black"<br/>stroke-width="2"/&#62');
    $('svg path.L').attr("d","M 10 10 "+lineto);
  }
  if(comand=='H'||comand=='V'){
    var V="V "+$("#Vy").val();
    var H="H "+$("#Hx").val();
    $('svg path.V').attr("d","M 100 100 "+V)
    $('svg path.H').attr("d","M 100 100 "+H);
    $("#HV_card").html('&#60path d="M 100 100 '+H+'" stroke="black" stroke-width="2"/&#62<br/>&#60path d="M 100 100 '+V+'" stroke="red" stroke-width="2"/&#62');
  }
  if(comand=='C'){
    var Cx1 = $('#Cx1').val();
    var Cy1 = $('#Cy1').val();
    var Cx2 = $('#Cx2').val();
    var Cy2 = $('#Cy2').val();
    var Cx = $('#Cx').val();
    var Cy = $('#Cy').val();
    var newC = "M 20,80 C "+Cx1+","+Cy1+" "+Cx2+","+Cy2+" "+Cx+","+Cy;
    var newhtmlC = '&#60;path d="M 20,80<br/>C '+Cx1+','+Cy1+'<br/>'+Cx2+','+Cy2+'<br/>'+Cx+','+Cy+'<br/>stroke="black" stroke-width="2" fill="none"/&#62;<br/><br/>&#60;line x1="20" y1="80" x2="'+Cx1+'" y2="'+Cy1+'" stroke="red"/&#62;<br/>&#60;line x1="'+Cx+'" y1="'+Cy+'" x2="'+Cx2+'" y2="'+Cy2+'" stroke="blue"/&#62;';
    $('svg path.C').attr('d',newC);
    $('#CLine1').attr({
      "x2":Cx1,
      "y2":Cy1
    });
    $('#CLine2').attr({
      "x1":Cx,
      "y1":Cy,
      "x2":Cx2,
      "y2":Cy2
    });
    $("#curveto_card").html(newhtmlC);
  }
  if(comand=='S'){
    var Sx2 = $("#Sx2").val();
    var Sy2 = $("#Sy2").val();
    var Sx = $("#Sx").val();
    var Sy = $("#Sy").val();
    var newS = 'M 20,80 C 0,120 120,120 100,80 S '+Sx2+','+Sy2+' '+Sx+','+Sy;
    $('svg path.S').attr('d',newS);
    $('svg #SLine3').attr({
      "x1":Sx,
      "y1":Sy,
      "x2":Sx2,
      "y2":Sy2
    });
    var newhtmlS = '&#60;path d="M 20 80<br/>C 0,120<br/>170,120<br/>150,80<br/> S '+Sx2+','+Sy2+'<br/>'+Sx+','+Sy+'"<br/>stroke="black" stroke-width="2" fill="none"/&#62;<br/><br/>&#60;line x1="'+Sx+'" y1="'+Sy+'" x2="'+Sx2+'" y2="'+Sy2+'" stroke="red"/&#62;';
    $("#smoothcurveto_card").html(newhtmlS);
  }
  if(comand=='Q'){
    var Qx1 = $("#Qx1").val();
    var Qy1 = $("#Qy1").val();
    var Qx = $("#Qx").val();
    var Qy = $("#Qy").val();
    var newQ = 'M 20,80 Q '+Qx1+','+Qy1+' '+Qx+','+Qy;
    $("svg path.Q").attr("d",newQ);
    $('#QLine1, #QLine2').attr({
      "x1":Qx1,
      "y1":Qy1
    });
    $('#QLine2').attr({
      "x2":Qx,
      "y2":Qy
    });
    var newhtmlQ = '&#60;path d="M 20 80<br/>Q '+Qx1+','+Qy1+'<br/>'+Qx+','+Qy+'<br/>stroke="black" stroke-width="2" fill="none"/&#62;<br/><br/>&#60;line x1="'+Qx1+'" y1="'+Qy1+'" x2="20" y2="80" stroke="red"/&#62;<br/>&#60;line x1="'+Qx1+'" y1="'+Qy1+'" x2="'+Qx+'" y2="'+Qy+'" stroke="red"/&#62;';
    $("#quadratic_card").html(newhtmlQ);
  }
  if(comand=='T'){
    var Td = $("#dsq").val();
    $("svg path.T").attr("d",Td);
  }
  if(comand=='A'){
    $("svg path.A").attr("d",$("#arc").val());
  }
}

$('#timeButton').click(function(){
  var MyDate= new Date();
  $('#timeI').html(MyDate.getHours()+':'+MyDate.getMinutes()+' hrs.');
});

$(document).ready(function(){
  $(".button-collapse").sideNav();
  $('.parallax').parallax();

  $('#boton_mostrar').click(function(){
    $('#rectangulo_png,#rectangulo_svg').attr({
      "class": "tooltipped",
      "data-position": "bottom"
    });
    $('#rectangulo_png').attr('data-tooltip',"1'161 bytes (1.13 KB)");
    $('#rectangulo_svg').attr('data-tooltip',"267 bytes");
    $('.tooltipped').tooltip({delay: 50});
  });

  $('.prefijos').hide();
  $('#mostrar_prefijos').click(function(){
    $('#mostrar_prefijos').hide();
    $('.prefijos').show();
    Materialize.fadeInImage('.prefijos')
  });

  $("#mostrar_axis").click(function(){
    $("#mostrar_axis").hide();
    Materialize.fadeInImage('#axis');
  });

  var options = [
    {selector: '#secret_part', offset: 500, callback: function() {
      Materialize.fadeInImage('#secret_part');
    } },
  ];
  Materialize.scrollFire(options);

  $(".dropdown-button").dropdown();

  $('.modal').modal();

  $('#prac1', '#prac2').modal('open');

  $('#prac1', '#prac2').modal('close');

})
