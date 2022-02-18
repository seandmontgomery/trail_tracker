
/*
  The following function manages interactions
  between Trail Tracker's UI and backend, namely,
  it allows users to add trails. Before interacting
  with TT's backend, a roundtrip is first made to
  Cloudinary, where media files are uploaded and stored.
*/
async function addImage() {
    const cloudinary_url = "/upload-cloudinary";
    const fileList = document.querySelectorAll("[type=file]");

    /*  - - - - - - - - - - - - - - - - - - - - - - - - -
        STEP 1: Upload images to Cloudinary

    */
    // Get a url for each image (once uploaded to cloudinary)
    const image_urls = []
    console.log(image_urls);
    // iterate over the image files
    for (let i = 0; i < fileList.length; i++) {
        const formData = new FormData();

        let file = fileList[i];
        formData.append("file", file.files[0]);

        // this is where we send the data to the /upload-cloudinary end point
        let cloud_res = await fetch(cloudinary_url, {
            method: "POST",
            body: formData
        })
        //we are waiting for cloudinary to return the image object
        let cloud_res_json = await cloud_res.json();

        // Save this url
        image_urls.push(cloud_res_json.url)
      }

    console.log(image_urls);

    /*  - - - - - - - - - - - - - - - - - - - - - - - - -
        STEP 2: Send trail data (with image URLs) to
        trail tracker backend

        Notes:
          * this is where we store the image in the database
    */

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
            "image_urls": image_urls,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    /*  - - - - - - - - - - - - - - - - - - - - - - - - -
        STEP 2: Send trail data (with image URLs) to
        trail tracker backend

    */
      if (!flask_resp.ok) {
          alert(`Unable to load files. ${flask_resp.statusText}`)
      }
    //once function has completed, we reroute to the gallery
    window.location = '/feed';
  }




const form = document.querySelector("#upload-trail-form");

form.addEventListener("submit", (evt) => {
  evt.preventDefault();
  addImage()
})
