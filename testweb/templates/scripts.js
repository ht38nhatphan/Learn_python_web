window.onscroll = function() {
    scropfun()
};

function scropfun() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 30) {

        document.getElementById("hede").style.background = "#222222";
        document.getElementById("hede").style.position = "fixed";
    } else {
        // document.getElementById("hede").style.marginTop = "0";
        document.getElementById("hede").style.background = "transparent"
        document.getElementById("hede").style.position = "relative";
    }
}