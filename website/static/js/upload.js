// ################## FEATURE FOR ADDING ADDITIONAL MEDIA ####################

const listAddButton = $('#add-media')
let click_counter = 0
  const addItem = () => {
      click_counter++
      $('#list').append(`<li class="add-media">
      <div id="media-uploader">
        <label class="custom-file-upload">
        <input type="file" id="media-files-${click_counter}" name="filesToUpload[]" multiple>
        </label>
      </div></li>`)
  }
listAddButton.on('click', addItem)

//############# BUTTON FEATURE FOR COVER PHOTO UPLOAD ######################

document.getElementById('cover-photo-button').addEventListener('click', openDialog);
function openDialog() {
  document.getElementById('image_url').click();
}

//################### UPLOAD ################################################

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

    const image_urls = []
    console.log(image_urls);

    for (let i = 0; i < fileList.length; i++) {

        let media_title = 'placeholder';
        const formData = new FormData();

        let file = fileList[i];
        formData.append("file", file.files[0]);

        let cloud_res = await fetch(cloudinary_url, {
            method: "POST",
            body: formData
        })

        let cloud_res_json = await cloud_res.json();


        image_urls.push({
          'title': media_title,
          'url': cloud_res_json.url
        })
      }

    let flask_resp = await fetch('/upload-trail', {
        method: "POST",
        body: JSON.stringify({
            'trail_name': $('#trail_name').val(),
            'location': $('#autocomplete').val(),
            'date': $('#date').val(),
            'difficulty': $('#difficulty').val(),
            'terrain': $('#terrain').val(),
            'miles': $('#miles').val(),
            'hours': $('#hours').val(),
            'minutes': $('#minutes').val(),
            'elevation': $('#elevation').val(),
            'notes': $('#notes').val(),
            "image_urls": image_urls,
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

      if (!flask_resp.ok) {
          alert(`Unable to load files. ${flask_resp.statusText}`)
      }
    window.location = '/feed';
  }

const form = document.querySelector("#upload-trail-form");

form.addEventListener("submit", (evt) => {
  evt.preventDefault();
  addImage()
})