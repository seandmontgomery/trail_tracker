const photoAlbumButton = document.getElementById('photo-album-open');

photoAlbumButton.addEventListener('click', function() {
    // Get the data id that we identified in the element
    let trailId = photoAlbumButton.getAttribute('data-trail-id-for-album');
    // Call the function we wrote with this data id as argument
    
    $.get(`/api/node/${trailId}`, (resp) => {
      let photoArray = resp.photo_array
      // parse the json before the get?
      // Loop through objects
      // Make sure you handle an empty array
      // access URL with dot notation 
      console.log(photoArray)
      
      
      

      // use fslightbox...

      //const lightbox = new FsLightbox();

      // set up props, like sources, types, events etc.

      // lightbox.props.sources = [];
      // lightbox.props.onInit = () => console.log('Lightbox initialized!');
      // lightbox.open();

    }

)});
