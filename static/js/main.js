$(document).ready(function(){

    $('#reviews tbody tr').on('click', function(){
        var href = $(this).find('a.review-link').attr('href');
        var iframe_src = $('iframe').attr('src');

        if (href === iframe_src)
            $('iframe').remove();
        else
        {
            $('iframe').remove();
            var $iframe = $('<iframe/>').attr({'src': href});
            $(this).find('.review-title').append($iframe);
        }

        return false;
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

})

    function createGraph(container, data)
    {
        if ($(container).length)
        {
            var ticks = data.length;

            default_max = 100;
            max = Math.max.apply(Math, data.map(function(o){return o[1];}));
            if (max > default_max)
                default_max = max;

            graph = Flotr.draw(container, [ {data:data, lines:{fill:true, show: true}, points: {show: true}, mouse: {track: true}} ], {
                xaxis : {
                    noTicks : ticks,
                    mode: "time",
                    timeFormat : '%d.%m.%y',
                    labelsAngle : 45,
                },
                yaxis: {
                    min: 0,
                    max: default_max,
                },
                grid: {
                    minorVerticalLines: true
                },
                mouse: {
                    track: true,
                    trackAll: true,
                    relative: true,
                    sensibility: 50,
                    trackDecimals: 0,
                    position: 'n',
                    trackFormatter: function(o){
                        var days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
                        var myDate = new Date(o.x);
                        return days[myDate.getDay()] + " " + myDate.toLocaleDateString() + " - " + o.y + " сделок";
                    }
                },
                HtmlText : false,
                title : 'Сделки'
            });
        }
    }