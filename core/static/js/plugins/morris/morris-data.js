// Morris.js Charts sample data for SB Admin template

$(function() {

    $.ajax({
            url: "http://127.0.0.1:8000/getUserData/",
            type: 'GET',
            dataType: 'json',
            data: { id: $('input[name="username"]').val()}, 
            success: function (data) {
                montarGrafico(data);
            }
    });

    function montarGrafico(dados) {
        // Line Chart
    Morris.Line({
        // ID of the element in which to draw the chart.
        element: 'morris-area-chart',
        // Chart data records -- each entry in this array corresponds to a point on
        // the chart.
        data: 'entradas',
        // The name of the data record attribute that contains x-visitss.
        xkey: 'x',
        // A list of names of data record attributes that contain y-visitss.
        ykeys: names,
        // Labels for the ykeys -- will be displayed when you hover over the
        // chart.
        labels: names,
        // Disables line smoothing
        smooth: false,
        resize: true
    });
    }

});
