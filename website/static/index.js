// ###################################DELETE NOTES#######################################

function deleteTrail(trailId) {
    fetch("/delete-trail", {
      method: "POST",
      body: JSON.stringify({ trailId: trailId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
  
  // ###################################GOOGLE MAPS#######################################

  // todo: get google maps api key to be called with environment variable 
  
  // var placeSearch, autocomplete;
  //       var componentForm = {
  //         street_number: 'short_name',
  //         route: 'long_name',
  //         locality: 'long_name',
  //         administrative_area_level_1: 'short_name',
  //         country: 'long_name',
  //         postal_code: 'short_name'
  //       };
  
  //       function initAutocomplete() {
  //         autocomplete = new google.maps.places.Autocomplete(
  //             /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
  //             {types: ['geocode', 'establishment']});
  //         }
  
  //       function geolocate() {
  //         if (navigator.geolocation) {
  //           navigator.geolocation.getCurrentPosition(function(position) {
  //             var geolocation = {
  //               lat: position.coords.latitude,
  //               lng: position.coords.longitude
  //             };
  //             var circle = new google.maps.Circle({
  //               center: geolocation,
  //               radius: position.coords.accuracy
  //             });
  //             autocomplete.setBounds(circle.getBounds());
  //           });
  //         }
  //       }

