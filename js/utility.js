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

function parseTitle(title) {
  // Parse title format: "Object - City - Country" or "Object - City - State, Country"
  // Returns: { object, city, state, country, fullLocation }

  var parts = title.split(' - ');
  var result = {
    object: '',
    city: '',
    state: '',
    country: '',
    fullLocation: title
  };

  if (parts.length === 1) {
    // No separator, treat as location
    result.city = parts[0].trim();
    result.country = parts[0].trim();
  } else if (parts.length === 2) {
    // "City - Country" or "Object - Country"
    result.object = parts[0].trim();
    var lastPart = parts[1].trim();

    if (lastPart.includes(',')) {
      var locationParts = lastPart.split(',');
      result.state = locationParts[0].trim();
      result.country = locationParts[1].trim();
      result.city = result.object; // In this case, first part might be city
    } else {
      result.city = parts[0].trim();
      result.country = lastPart;
    }
  } else if (parts.length >= 3) {
    // "Object - City - Country" or "Object - City - State, Country"
    result.object = parts[0].trim();
    result.city = parts[1].trim();
    var lastPart = parts[parts.length - 1].trim();

    if (lastPart.includes(',')) {
      var locationParts = lastPart.split(',');
      result.state = locationParts[0].trim();
      result.country = locationParts[1].trim();
    } else {
      result.country = lastPart;
    }
  }

  return result;
}