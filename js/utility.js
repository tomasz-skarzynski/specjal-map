var language = navigator.language || navigator.userLanguage;
var language = (language === "pl") ? "pl" : "en";

function displayDate(datetimeJson) {
  var datetime = new Date(datetimeJson);
  var datetimeString = datetime.toISOString();
  var date = datetimeString.substring(0,10);
  if(datetimeJson.length >= 16) {
      var time = datetimeString.substring(11,16);
      return date + ' ' + time;
  }else{
      return date;
  }
}

function isAnniversary(datetimeJson) {
  if (!datetimeJson) return false;

  var markerDate = new Date(datetimeJson);
  var today = new Date();

  // Check if it's the same day and month, but different year
  return markerDate.getMonth() === today.getMonth() &&
         markerDate.getDate() === today.getDate() &&
         markerDate.getFullYear() !== today.getFullYear();
}