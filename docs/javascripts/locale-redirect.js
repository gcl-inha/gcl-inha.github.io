(function () {
  var lang = navigator.language || navigator.userLanguage || "";
  var isKorean = lang.toLowerCase().startsWith("ko");
  var isEnglishPath = location.pathname.startsWith("/en/") || location.pathname === "/en";

  if (!isKorean && !isEnglishPath) {
    location.replace("/en" + location.pathname + location.search + location.hash);
  }
})();
