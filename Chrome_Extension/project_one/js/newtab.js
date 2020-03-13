function ping(ip){
    var img = new Image();
    var start = new Date().getTime();
    var flag = false;
    var isCloseWifi = true;
    var hasFinish = false;
    img.onload = function() {
        if ( !hasFinish ) {
            flag = true;
            hasFinish = true;
            console.log('Ping ' + ip + ' success.---onload');
            alert("成功"+ip);
        }
    };
    img.onerror = function() {
        if ( !hasFinish ) {
            if ( !isCloseWifi ) {
                flag = true;
                console.log('Ping ' + ip + ' success.---onerror');
                alert("成功"+ip);
            } else {
                console.log('network is not working!');
            }
            hasFinish = true;
        }
    };
    setTimeout(function(){
        isCloseWifi = false;
        console.log('network is working, start ping...');
        alert("开始测试"+ip);
    },2);
    setInterval(function() {
        img.src = 'http://' + ip + '/' + start;
        if ( !flag ) {
            hasFinish = true;
            flag = false ;
            document.body.innerText += "'Ping ' + ip + ' fail. '";
        }
    }, 3000);
}
window.onload = function(){
    ping('192.168.1.3')
}
