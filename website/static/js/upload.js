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
        let flask_resp = await fetch('/upload-trail', {
            method: "POST",
            body: JSON.stringify({
                'trail_name': $('#trail_name').val(),
                'location': $('#autocomplete').val(),
                'date': $('#date').val(),
                'difficulty': $('#difficulty').val(),
                'trail_type': $('#trail_type').val(),
                'miles': $('#miles').val(),
                'hours': $('#hours').val(),
                'minutes': $('#minutes').val(),
                'notes': $('#notes').val(),
                "image_url": cloud_res_json.url,
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
  
  const form = document.querySelector("#upload-trail-form");
  
  form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    addImage()
        })