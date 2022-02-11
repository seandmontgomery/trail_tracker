// ###################################CLOUDINARY#######################################

  async function addImage() {
    const url = "/upload-cloudinary";
    const fileList = document.querySelectorAll("[type=file]");
  
    //iterate over the image files
    for (let i = 0; i < fileList.length; i++) {
        const formData = new FormData();
      
        let file = fileList[i];
        formData.append("file", file.files[0]);
        //this is where we send the data to the /upload-cloudinary end point
        let cloud_res = await fetch(url, {
            method: "POST",
            body: formData
        })
        //we are waiting for cloudinary to return the image object 
        let cloud_res_json = await cloud_res.json();
  
        //this is where we store the image in the database
        let flask_resp = await fetch('/submit-media', {
            method: "POST",
            body: JSON.stringify({
              "media_url": cloud_res_json.url,
              "media_title": $(`#media-title-${i+1}`).val(),
            }),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        
        if (!flask_resp.ok) {
            alert(`Unable to load files. ${flask_resp.statusText}`)
            break 
        }   
    }
    //once function has completed, we reroute to the gallery
    window.location = '/feed'
  }

    // #######################ON SUBMIT####################################
  
  const form = document.querySelector("#upload-trail-form");
  
  form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    addImage()
        })

        form.addEventListener("submit", (evt) => {
          evt.preventDefault();
          // here, we are getting the user input   
          const trailInputs = {
            'trail_name': $('#trail_name').val(),
            'location': $('#autocomplete').val(),
            'date': $('#date').val(),
            'miles': $('#miles').val(),
            'hours': $('#hours').val(),
            'minutes': $('#minutes').val(),
            'notes': $('#notes').val(),
            "image_url": cloud_res_json.url,
          };

          fetch('/upload-trail', {
            method: "POST",
            body: JSON.stringify(trailInputs),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })

        .then((response) => response.json())
        .then((data) => {
            //this is where we send data to the backend for the audition to be created
           fetch('/upload-trail', {
            method: "POST",
            body: JSON.stringify(trailInputs),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }) 

        .then((response) => response.json())
        .then((data) => {
            trail_id = data.trail_id;
            return data
            //once all previous data is returned, then we call the addMedia function
        }).then(addMedia())})})
