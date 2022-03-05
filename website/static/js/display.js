// --------- NOTES MODAL-----------------------------

document.querySelectorAll('.notes').forEach(noteBtn => {
  console.log(noteBtn);
  noteBtn.addEventListener('click', function (event) {
  
    // var notesButton = event.relatedTarget
    var trailID = noteBtn.getAttribute('data-modal')
  
    console.log(trailID);

        $.get(`/api/notes-modal/${trailID}`, (resp) => {
        let trailTitle = resp.notes_data.title
        let trailNotes = resp.notes_data.notes
        console.log(trailTitle);
        console.log(trailNotes);
  
        var modalTitle = document.querySelector('.modal-title')
        var modalBody = document.querySelector('.modal-body')
  
        modalTitle.textContent = trailTitle;
        modalBody.textContent = trailNotes;
      })
  });
})

// --------- PHOTO ALBUM -----------------------------

document.querySelectorAll('.photo-album-open').forEach(btn => {
  
  btn.addEventListener('click', function() {
    let trailId = btn.getAttribute('data-trail-id-for-album');
    
    $.get(`/api/node/${trailId}`, (resp) => {
      const photoArray = resp.photo_array
      console.log(photoArray)
      
        // Loop through objects
        // access URL with dot notation 
        for(let i = 0; i < photoArray.length; i+=1){
          let currDiv;
          if(i === 0) {
            currDiv = document.createElement('div')
            currDiv.setAttribute('class', 'carousel-item active')
          } else {
            currDiv=  document.createElement('div')
            currDiv.setAttribute('class','carousel-item')
          }
           img = document.createElement('img')
            
          const urlOfActiveDivsImg = photoArray[i].url
          img.setAttribute('class',"d-block w-100")
          img.setAttribute('alt',"first slide")
          img.setAttribute("src",urlOfActiveDivsImg);
         
          currDiv.appendChild(img)
        
          const carouselInner = document.querySelectorAll(".carousel-inner")[0]
            
          carouselInner.appendChild(currDiv)
              
        }
    }

)});
})

// photoAlbumButton.addEventListener('click', function() {
//     let trailId = photoAlbumButton.getAttribute('data-trail-id-for-album');
    
//     $.get(`/api/node/${trailId}`, (resp) => {
//       const photoArray = resp.photo_array
//       console.log(photoArray)
      
//         // Loop through objects
//         // access URL with dot notation 
//         for(let i = 0; i < photoArray.length; i+=1){
//           let currDiv;
//           if(i === 0) {
//             currDiv = document.createElement('div')
//             currDiv.setAttribute('class', 'carousel-item active')
//           } else {
//             currDiv=  document.createElement('div')
//             currDiv.setAttribute('class','carousel-item')
//           }
//            img = document.createElement('img')
            
//           const urlOfActiveDivsImg = photoArray[i].url
//           img.setAttribute('class',"d-block w-100")
//           img.setAttribute('alt',"first slide")
//           img.setAttribute("src",urlOfActiveDivsImg);
         
//           currDiv.appendChild(img)
        
//           const carouselInner = document.querySelectorAll(".carousel-inner")[0]
            
//           carouselInner.appendChild(currDiv)
              
//         }
//     }

// )});

$('#photoModal').on('hidden.bs.modal', function (e) {
 const innerDiv = document.querySelectorAll(".carousel-inner")[0]
 while (innerDiv.firstChild) {
  innerDiv.removeChild(innerDiv.firstChild);
}
console.log("out of while loop!")
console.log(innerDiv)
})

