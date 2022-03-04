// --------- NOTES MODAL-----------------------------

var notesModal = document.getElementById('notesModal');
notesModal.addEventListener('show.bs.modal', function (event) {
  var notesButton = event.relatedTarget
  var trailID = notesButton.getAttribute('data-modal')

  console.log(trailID);
  console.log(notesButton);

      $.get(`/api/notes-modal/${trailID}`, (resp) => {
      let trailTitle = resp.title
      let trailNotes = resp.notes
      console.log(trailTitle);
      console.log(trailNotes);

      var modalTitle = exampleModal.querySelector('.modal-title')
      var modalBody = exampleModal.querySelector('.modal-body')

      modalTitle.textContent = trailTitle;
      modalBody.textContent = trailNotes;
    })

  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = '${trailID} ${notesButton}';
  modalTitle.textContent = 'Hello modal title';
});

// --------- PHOTO ALBUM -----------------------------

const photoAlbumButton = document.getElementById('photo-album-open');

photoAlbumButton.addEventListener('click', function() {
    // Get the data id that we identified in the element
    let trailId = photoAlbumButton.getAttribute('data-trail-id-for-album');
    // Call the function we wrote with this data id as argument
    
    $.get(`/api/node/${trailId}`, (resp) => {
      const photoArray = resp.photo_array
      // Loop through objects
      // access URL with dot notation 
      console.log(photoArray)

        // const outterDiv = document.createElement('div');
        // outterDiv.setAttribute("id")
        // <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">

        // const innerDiv = document.createElement('div')
        // append the follow to this div and them make it the child of the div above:
        // <div class="carousel-inner">
        
        for(let i = 0; i < photoArray.length; i+=1){
          if(i ===0) {
          
          const activeDiv = document.createElement('div')
          activeDiv.setAttribute("class", "carousel-item active" );
          
          const activeImg = document.createElement('img')
          activeImg.setAttribute("class","d-block w-100")
          activeImg.setAttribute("src",photoArray[i].url)
          activeImg.setAttribute("alt","First Slide")
          activeDiv.appendChild(activeImg)
          console.log(JSON.stringify(activeDiv))
          const innerDiv = document.querySelectorAll('.carousel-inner')
          console.log(innerDiv)
          innerDiv.appendChild(activeDiv)
          


              } else {
          
                console.log(photoArray[i].url);

              }
        }

    }

)});

