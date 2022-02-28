$('.card-text-wrapper').click(function() {
  clickToExapndCards($(this));
});

function clickToExapndCards($obj){
  var clickedElement = $obj;
  if (clickedElement.hasClass('expanded')) {
    clickedElement.find('.card-text').hide('slow');
    clickedElement.removeClass('expanded');
  } else {
     clickedElement.find('.card-text').show('slow');
    clickedElement.addClass('expanded');
  }
  
};

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

const photoAlbumDropdown = document.getElementById('album-dropdown');

photoAlbumDropdown.addEventListener('click', function() {
    // Get the data id that we identified in the element
    let trailId = photoAlbumDropdown.getAttribute('data-trail-id-for-album');
    // Call the function we wrote with this data id as argument
    
    $.get(`/api/node/${trailId}`, (resp) => {
      let photoArray = resp.photo_array
      function addCode() { 
      for (let i = 0; i < photoArray.length; i++) {
          photoAlbumDropdown.innerHTML += "<h3>This is the text which has been inserted by JS {{ trail.trail_id }}</h3>";
      }}
      // access URL with dot notation 
      console.log(photoArray)

    }

)});
